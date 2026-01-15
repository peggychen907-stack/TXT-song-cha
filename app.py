import streamlit as st
import pandas as pd

# --- 設定網頁配置 ---
st.set_page_config(
    page_title="TXT 歌詞庫 (MOA Edition)",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 模擬資料庫 (Mock Data) ---
# 這裡包含了專輯資訊與歌曲歌詞
ALBUMS = {
    'freefall': {
        'title': 'The Name Chapter: FREEFALL',
        'year': '2023',
        'color': '#818CF8' # Indigo
    },
    'temptation': {
        'title': 'The Name Chapter: TEMPTATION',
        'year': '2023',
        'color': '#34D399' # Emerald
    },
    'thursday': {
        'title': "minisode 2: Thursday's Child",
        'year': '2022',
        'color': '#F87171' # Red
    },
    'freeze': {
        'title': 'The Chaos Chapter: FREEZE',
        'year': '2021',
        'color': '#60A5FA' # Blue
    },
    'magic': {
        'title': 'The Dream Chapter: MAGIC',
        'year': '2019',
        'color': '#2DD4BF' # Teal
    }
}

SONGS = [
    {
        'id': 'chasing_feeling',
        'album_id': 'freefall',
        'title': 'Chasing That Feeling',
        'korean_title': 'Chasing That Feeling',
        'lyrics': [
            {'ko': 'Heaven is hiding empty-handed', 'ro': 'Heaven is hiding empty-handed', 'zh': '天堂空手躲藏著'},
            {'ko': '탄 곳이 없는 shooting star', 'ro': 'Tan gosi eomneun shooting star', 'zh': '沒有燃燒殆盡的流星'},
            {'ko': '내일도 난 제자리야', 'ro': 'Naeildo nan jejariya', 'zh': '明天我也會在原地'},
            {'ko': "I'm chasing that feeling", 'ro': "I'm chasing that feeling", 'zh': '我在追逐那種感覺'},
            {'ko': '망가진 나라도 괜찮아', 'ro': 'Manggajin narado gwaenchana', 'zh': '即使壞掉的我也可以'},
        ]
    },
    {
        'id': 'sugar_rush_ride',
        'album_id': 'temptation',
        'title': 'Sugar Rush Ride',
        'korean_title': 'Sugar Rush Ride',
        'lyrics': [
            {'ko': '생각은 멈춰', 'ro': 'Saenggageun meomchwo', 'zh': '停止思考'},
            {'ko': '직감만 남겨', 'ro': 'Jikgamman namgyeo', 'zh': '只留下直覺'},
            {'ko': '거부할 수 없는 이 이끌림', 'ro': 'Geobuhal su eomneun i ikkeullim', 'zh': '這無法抗拒的吸引力'},
            {'ko': 'Gimme gimme more', 'ro': 'Gimme gimme more', 'zh': '給我更多 給我更多'},
            {'ko': 'Sugar rush-ush', 'ro': 'Sugar rush-ush', 'zh': '糖分衝擊'},
        ]
    },
    {
        'id': 'gbgb',
        'album_id': 'thursday',
        'title': 'Good Boy Gone Bad',
        'korean_title': 'Good Boy Gone Bad',
        'lyrics': [
            {'ko': '영원이란 말은 모래성', 'ro': 'Yeongwoniran mareun moraeseong', 'zh': '永遠這個詞就像沙堡'},
            {'ko': '부드러운 파도 앞에 무너져', 'ro': 'Budeureoun pado ape muneojyeo', 'zh': '在溫柔的海浪面前倒塌'},
            {'ko': 'Good boy gone bad', 'ro': 'Good boy gone bad', 'zh': '好男孩變壞了'},
        ]
    },
    {
        'id': 'lovesong',
        'album_id': 'freeze',
        'title': '0X1=LOVESONG (I Know I Love You)',
        'korean_title': '0X1=LOVESONG',
        'lyrics': [
            {'ko': 'I know I love you', 'ro': 'I know I love you', 'zh': '我知道我愛你'},
            {'ko': '이 제로의 세계 속', 'ro': 'I jeroui segye sok', 'zh': '在這個歸零的世界裡'},
            {'ko': 'I know you’re my one and only', 'ro': 'I know you’re my one and only', 'zh': '我知道你是我的唯一'},
        ]
    },
    {
        'id': 'run_away',
        'album_id': 'magic',
        'title': '9 and Three Quarters (Run Away)',
        'korean_title': '9와 4분의 3 승강장에서 너를 기다려',
        'lyrics': [
            {'ko': '나만 빼고 다 행복한 것만 같아', 'ro': 'Naman ppaego da haengbokhan geonman gata', 'zh': '好像除了我以外大家都很幸福'},
            {'ko': '우는 것보다 웃을 때가 더 아파', 'ro': 'Uneun geotboda useul ttaega deo apa', 'zh': '比起哭泣，笑的時候更痛苦'},
            {'ko': '도망갈까', 'ro': 'Domanggalkka', 'zh': '要逃跑嗎'},
        ]
    }
]

# --- 狀態管理 (Session State) ---
# 用來記錄使用者目前的頁面位置和選擇的歌曲
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'selected_song' not in st.session_state:
    st.session_state.selected_song = None
if 'favorites' not in st.session_state:
    st.session_state.favorites = []

# --- 輔助函式 ---
def go_to_home():
    st.session_state.page = 'home'
    st.session_state.selected_song = None

def go_to_song(song):
    st.session_state.selected_song = song
    st.session_state.page = 'lyrics'

def toggle_favorite(song_id):
    if song_id in st.session_state.favorites:
        st.session_state.favorites.remove(song_id)
    else:
        st.session_state.favorites.append(song_id)

# --- CSS 樣式自訂 ---
st.markdown("""
<style>
    .stButton>button {
        width: 100%;
        border-radius: 20px;
    }
    .album-card {
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .korean-text { font-size: 1.2rem; font-weight: bold; margin-bottom: 2px; }
    .roman-text { font-size: 0.9rem; color: #666; font-style: italic; margin-bottom: 2px; }
    .chinese-text { font-size: 1.0rem; color: #4F46E5; margin-bottom: 15px; }
</style>
""", unsafe_allow_html=True)

# --- 側邊欄：搜尋與導航 ---
with st.sidebar:
    st.title("TXT 歌詞庫 🎧")
    
    if st.button("🏠 回首頁"):
        go_to_home()
    
    st.divider()
    
    # 搜尋功能
    search_query = st.text_input("🔍 搜尋歌曲...", placeholder="輸入歌名...").lower()
    
    # 收藏夾預覽
    st.subheader("我的收藏 ❤️")
    if st.session_state.favorites:
        fav_songs = [s for s in SONGS if s['id'] in st.session_state.favorites]
        for song in fav_songs:
            if st.button(f"{song['title']}", key=f"fav_{song['id']}"):
                go_to_song(song)
    else:
        st.info("還沒有收藏歌曲")

# --- 主頁面邏輯 ---

# 1. 如果有搜尋關鍵字，直接顯示搜尋結果
if search_query:
    st.subheader(f"搜尋結果: '{search_query}'")
    results = [
        s for s in SONGS 
        if search_query in s['title'].lower() or search_query in s['korean_title'].lower()
    ]
    
    if results:
        for song in results:
            album = ALBUMS[song['album_id']]
            col1, col2 = st.columns([1, 4])
            with col1:
                st.markdown(f'<div style="background-color:{album["color"]}; width:50px; height:50px; border-radius:50%;"></div>', unsafe_allow_html=True)
            with col2:
                st.write(f"**{song['title']}**")
                st.caption(f"{song['korean_title']} • {album['title']}")
                if st.button("查看歌詞", key=f"search_{song['id']}"):
                    go_to_song(song)
                    st.rerun()
            st.divider()
    else:
        st.warning("找不到相關歌曲")

# 2. 歌詞頁面 (當選擇了歌曲)
elif st.session_state.page == 'lyrics' and st.session_state.selected_song:
    song = st.session_state.selected_song
    album = ALBUMS[song['album_id']]
    
    # 頂部導航
    if st.button("← 返回列表"):
        go_to_home()
    
    # 標題區
    st.markdown(f"<h1 style='text-align: center;'>{song['title']}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; color: gray;'>{album['title']} ({album['year']})</p>", unsafe_allow_html=True)
    
    # 控制按鈕 (收藏 & 顯示設定)
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        is_fav = song['id'] in st.session_state.favorites
        fav_label = "❤️ 取消收藏" if is_fav else "🤍 加入收藏"
        if st.button(fav_label, use_container_width=True):
            toggle_favorite(song['id'])
            st.rerun()

    st.divider()
    
    # 顯示選項
    col_opt1, col_opt2 = st.columns(2)
    with col_opt1:
        show_roman = st.checkbox("顯示羅馬拼音", value=True)
    with col_opt2:
        show_zh = st.checkbox("顯示中文翻譯", value=True)
    
    st.divider()

    # 歌詞渲染
    for line in song['lyrics']:
        st.markdown(f"<div class='korean-text'>{line['ko']}</div>", unsafe_allow_html=True)
        
        if show_roman:
            st.markdown(f"<div class='roman-text'>{line['ro']}</div>", unsafe_allow_html=True)
            
        if show_zh:
            st.markdown(f"<div class='chinese-text'>{line['zh']}</div>", unsafe_allow_html=True)
        
        st.write("") # 空行間隔

# 3. 首頁 (專輯與歌曲列表)
else:
    st.title("Hello, MOA! ✨")
    st.write("請選擇一張專輯或使用左側搜尋：")
    
    # 這裡將專輯以頁籤 (Tabs) 方式呈現
    album_ids = list(ALBUMS.keys())
    tabs = st.tabs([ALBUMS[aid]['title'] for aid in album_ids])
    
    for idx, tab in enumerate(tabs):
        album_id = album_ids[idx]
        album = ALBUMS[album_id]
        
        with tab:
            # 專輯卡片視覺
            st.markdown(
                f"""
                <div class="album-card" style="background: linear-gradient(135deg, {album['color']}, #888);">
                    <h2>{album['title']}</h2>
                    <p>{album['year']}</p>
                </div>
                """, 
                unsafe_allow_html=True
            )
            
            # 該專輯的歌曲列表
            album_songs = [s for s in SONGS if s['album_id'] == album_id]
            
            if album_songs:
                for song in album_songs:
                    c1, c2 = st.columns([4, 1])
                    with c1:
                        st.subheader(song['title'])
                        st.caption(song['korean_title'])
                    with c2:
                        if st.button("歌詞 👉", key=f"btn_{song['id']}"):
                            go_to_song(song)
                            st.rerun()
                    st.divider()
            else:
                st.info("此專輯暫無收錄歌曲。")
