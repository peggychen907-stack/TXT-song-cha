import streamlit as st

# --- 設定網頁配置 ---
st.set_page_config(
    page_title="TXT 歌詞庫 (MOA Edition)",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 資料庫 (Data) ---

# 1. 專輯資訊 (按發行時間倒序排列)
ALBUMS = {
    'sanctuary': {
        'title': 'The Star Chapter: SANCTUARY',
        'year': '2024',
        'color': '#A5B4FC' # Indigo-300
    },
    'tomorrow': {
        'title': 'minisode 3: TOMORROW',
        'year': '2024',
        'color': '#FDBA74' # Orange-300
    },
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
    'fight_escape': {
        'title': 'The Chaos Chapter: FIGHT OR ESCAPE',
        'year': '2021',
        'color': '#10B981' # Green (Repackage)
    },
    'freeze': {
        'title': 'The Chaos Chapter: FREEZE',
        'year': '2021',
        'color': '#60A5FA' # Blue
    },
    'blue_hour': {
        'title': 'minisode1 : Blue Hour',
        'year': '2020',
        'color': '#F472B6' # Pink
    },
    'eternity': {
        'title': 'The Dream Chapter: ETERNITY',
        'year': '2020',
        'color': '#A78BFA' # Purple
    },
    'magic': {
        'title': 'The Dream Chapter: MAGIC',
        'year': '2019',
        'color': '#2DD4BF' # Teal
    },
    'star': {
        'title': 'The Dream Chapter: STAR',
        'year': '2019',
        'color': '#FCD34D' # Yellow
    }
}

# 輔助函式：建立歌詞範本 (用於 B-side 歌曲)
def create_placeholder_lyrics():
    return [
        {'ko': '가사가 준비 중입니다.', 'ro': 'Gasaga junbi jungimnida.', 'zh': '(歌詞資料庫擴充中...)'},
        {'ko': 'MOA 여러분이 좋아하는 가사를 채워보세요!', 'ro': 'MOA yeoreobuni joahaneun gasareul chaewoboseyo!', 'zh': '請期待完整歌詞更新！'},
    ]

# 2. 歌曲資料庫 (包含主打歌歌詞與 B-side 曲目)
SONGS = [
    # --- The Star Chapter: SANCTUARY ---
    {
        'id': 'over_the_moon', 'album_id': 'sanctuary', 'title': 'Over The Moon', 'korean_title': 'Over The Moon',
        'lyrics': [
            {'ko': '너와 함께할 미래는 vintage', 'ro': 'Neowa hamkkehal miraeneun vintage', 'zh': '與你共度的未來是 classic vintage'},
            {'ko': '오래될수록 소중해', 'ro': 'Oraedoelsurok sojunghae', 'zh': '越久越珍貴'},
            {'ko': 'Over the moon', 'ro': 'Over the moon', 'zh': 'Over the moon'},
            {'ko': '내 세상은 너로 가득 차', 'ro': 'Nae sesangeun neoro gadeuk cha', 'zh': '我的世界充滿了你'},
        ]
    },
    {'id': 'heaven', 'album_id': 'sanctuary', 'title': 'Heaven', 'korean_title': 'Heaven', 'lyrics': create_placeholder_lyrics()},
    {'id': 'danger', 'album_id': 'sanctuary', 'title': 'Danger', 'korean_title': 'Danger', 'lyrics': create_placeholder_lyrics()},
    {'id': 'resist', 'album_id': 'sanctuary', 'title': 'Resist (Not Gonna Run Away)', 'korean_title': 'Resist', 'lyrics': create_placeholder_lyrics()},
    {'id': 'forty_one', 'album_id': 'sanctuary', 'title': 'Forty One Winks', 'korean_title': 'Forty One Winks', 'lyrics': create_placeholder_lyrics()},
    {'id': 'higher', 'album_id': 'sanctuary', 'title': 'Higher Than Heaven', 'korean_title': 'Higher Than Heaven', 'lyrics': create_placeholder_lyrics()},

    # --- minisode 3: TOMORROW ---
    {
        'id': 'deja_vu', 'album_id': 'tomorrow', 'title': 'Deja Vu', 'korean_title': 'Deja Vu',
        'lyrics': [
            {'ko': '폐허 속의 모르스부호', 'ro': 'Pyeheo sogui moreuseubuho', 'zh': '廢墟中的摩斯密碼'},
            {'ko': '약속을 너만은 기억할 테니', 'ro': 'Yaksogeul neomaneun gieokhal teni', 'zh': '只有你會記得那個約定'},
            {'ko': '마치 데자뷔', 'ro': 'Machi dejabwi', 'zh': '就像既視感 (Deja Vu)'},
            {'ko': 'I promise you', 'ro': 'I promise you', 'zh': '我向你保證'},
        ]
    },
    {'id': 'ill_see_you', 'album_id': 'tomorrow', 'title': "I'll See You There Tomorrow", 'korean_title': '내일에서 기다릴게', 'lyrics': create_placeholder_lyrics()},
    {'id': 'miracle', 'album_id': 'tomorrow', 'title': 'Miracle', 'korean_title': '기적은 너와 내가 함께하는 순간마다 일어나고 있어', 'lyrics': create_placeholder_lyrics()},
    {'id': 'quarter_life', 'album_id': 'tomorrow', 'title': 'Quarter Life', 'korean_title': 'Quarter Life', 'lyrics': create_placeholder_lyrics()},

    # --- The Name Chapter: FREEFALL ---
    {
        'id': 'chasing_feeling', 'album_id': 'freefall', 'title': 'Chasing That Feeling', 'korean_title': 'Chasing That Feeling',
        'lyrics': [
            {'ko': 'Heaven is hiding empty-handed', 'ro': 'Heaven is hiding empty-handed', 'zh': '天堂空手躲藏著'},
            {'ko': '탄 곳이 없는 shooting star', 'ro': 'Tan gosi eomneun shooting star', 'zh': '沒有燃燒殆盡的流星'},
            {'ko': "I'm chasing that feeling", 'ro': "I'm chasing that feeling", 'zh': '我在追逐那種感覺'},
        ]
    },
    {'id': 'growing_pain', 'album_id': 'freefall', 'title': 'Growing Pain', 'korean_title': 'Growing Pain', 'lyrics': create_placeholder_lyrics()},
    {'id': 'back_for_more', 'album_id': 'freefall', 'title': 'Back for More (TXT Ver.)', 'korean_title': 'Back for More', 'lyrics': create_placeholder_lyrics()},
    {'id': 'dreamer', 'album_id': 'freefall', 'title': 'Dreamer', 'korean_title': 'Dreamer', 'lyrics': create_placeholder_lyrics()},
    {'id': 'happily_ever_after', 'album_id': 'freefall', 'title': 'Happily Ever After', 'korean_title': 'Happily Ever After', 'lyrics': create_placeholder_lyrics()},

    # --- The Name Chapter: TEMPTATION ---
    {
        'id': 'sugar_rush_ride', 'album_id': 'temptation', 'title': 'Sugar Rush Ride', 'korean_title': 'Sugar Rush Ride',
        'lyrics': [
            {'ko': '거부할 수 없는 이 이끌림', 'ro': 'Geobuhal su eomneun i ikkeullim', 'zh': '這無法抗拒的吸引力'},
            {'ko': 'Gimme gimme more', 'ro': 'Gimme gimme more', 'zh': '給我更多 給我更多'},
            {'ko': 'Sugar rush-ush', 'ro': 'Sugar rush-ush', 'zh': '糖分衝擊'},
        ]
    },
    {'id': 'devil_by_window', 'album_id': 'temptation', 'title': 'Devil by the Window', 'korean_title': 'Devil by the Window', 'lyrics': create_placeholder_lyrics()},
    {'id': 'happy_fools', 'album_id': 'temptation', 'title': 'Happy Fools (feat. Coi Leray)', 'korean_title': 'Happy Fools', 'lyrics': create_placeholder_lyrics()},
    {'id': 'tinnitus', 'album_id': 'temptation', 'title': 'Tinnitus (Wanna be a rock)', 'korean_title': '돌멩이가 되고 싶어', 'lyrics': create_placeholder_lyrics()},
    {'id': 'farewell_neverland', 'album_id': 'temptation', 'title': 'Farewell, Neverland', 'korean_title': '네버랜드를 떠나며', 'lyrics': create_placeholder_lyrics()},

    # --- minisode 2: Thursday's Child ---
    {
        'id': 'gbgb', 'album_id': 'thursday', 'title': 'Good Boy Gone Bad', 'korean_title': 'Good Boy Gone Bad',
        'lyrics': [
            {'ko': '영원이란 말은 모래성', 'ro': 'Yeongwoniran mareun moraeseong', 'zh': '永遠這個詞就像沙堡'},
            {'ko': 'Good boy gone bad', 'ro': 'Good boy gone bad', 'zh': '好男孩變壞了'},
        ]
    },
    {'id': 'opening_sequence', 'album_id': 'thursday', 'title': 'Opening Sequence', 'korean_title': 'Opening Sequence', 'lyrics': create_placeholder_lyrics()},
    {'id': 'trust_fund_baby', 'album_id': 'thursday', 'title': 'Trust Fund Baby', 'korean_title': 'Trust Fund Baby', 'lyrics': create_placeholder_lyrics()},
    {'id': 'lonely_boy', 'album_id': 'thursday', 'title': 'Lonely Boy', 'korean_title': '네 번째 손가락 위 타투', 'lyrics': create_placeholder_lyrics()},
    {'id': 'thursday_child', 'album_id': 'thursday', 'title': "Thursday's Child Has Far To Go", 'korean_title': 'Thursday\'s Child Has Far To Go', 'lyrics': create_placeholder_lyrics()},

    # --- The Chaos Chapter: FIGHT OR ESCAPE & FREEZE ---
    {
        'id': 'loser_lover', 'album_id': 'fight_escape', 'title': 'LO$ER=LO♡ER', 'korean_title': 'LO$ER=LO♡ER',
        'lyrics': [
            {'ko': 'I\'m a loser', 'ro': 'I\'m a loser', 'zh': '我是個失敗者'},
            {'ko': 'I\'m a lover', 'ro': 'I\'m a lover', 'zh': '我是個愛人'},
            {'ko': 'Lover with a $ dollar sign', 'ro': 'Lover with a $ dollar sign', 'zh': '帶著金錢符號的愛人'},
        ]
    },
    {
        'id': 'lovesong', 'album_id': 'freeze', 'title': '0X1=LOVESONG (I Know I Love You)', 'korean_title': '0X1=LOVESONG',
        'lyrics': [
            {'ko': 'I know I love you', 'ro': 'I know I love you', 'zh': '我知道我愛你'},
            {'ko': '이 제로의 세계 속', 'ro': 'I jeroui segye sok', 'zh': '在這個歸零的世界裡'},
        ]
    },
    {'id': 'anti_romantic', 'album_id': 'freeze', 'title': 'Anti-Romantic', 'korean_title': 'Anti-Romantic', 'lyrics': create_placeholder_lyrics()},
    {'id': 'magic_freeze', 'album_id': 'freeze', 'title': 'Magic', 'korean_title': 'Magic', 'lyrics': create_placeholder_lyrics()},
    {'id': 'ice_cream', 'album_id': 'freeze', 'title': 'Ice Cream', 'korean_title': '소악행', 'lyrics': create_placeholder_lyrics()},
    {'id': 'balance_game', 'album_id': 'freeze', 'title': 'Balance Game', 'korean_title': '밸런스 게임', 'lyrics': create_placeholder_lyrics()},
    {'id': 'frost', 'album_id': 'freeze', 'title': 'Frost', 'korean_title': 'Frost', 'lyrics': create_placeholder_lyrics()},

    # --- minisode1 : Blue Hour ---
    {
        'id': 'blue_hour', 'album_id': 'blue_hour', 'title': 'Blue Hour', 'korean_title': '5시 53분의 하늘에서 발견한 너와 나',
        'lyrics': [
            {'ko': 'Cuz of imagination', 'ro': 'Cuz of imagination', 'zh': '因為想像力'},
            {'ko': '저 하늘의 오렌지빛 마법이', 'ro': 'Jeo haneurui orenjibit mabeobi', 'zh': '那天空中橙色的魔法'},
            {'ko': '끝이 나기 전에', 'ro': 'Kkeuchi nagi jeone', 'zh': '在結束之前'},
        ]
    },
    {'id': 'ghosting', 'album_id': 'blue_hour', 'title': 'Ghosting', 'korean_title': 'Ghosting', 'lyrics': create_placeholder_lyrics()},
    {'id': 'wishlist', 'album_id': 'blue_hour', 'title': 'Wishlist', 'korean_title': 'Wishlist', 'lyrics': create_placeholder_lyrics()},
    {'id': 'we_lost_summer', 'album_id': 'blue_hour', 'title': 'We Lost The Summer', 'korean_title': '날씨를 잃어버렸어', 'lyrics': create_placeholder_lyrics()},
    {'id': 'way_home', 'album_id': 'blue_hour', 'title': 'Way Home', 'korean_title': '하굣길', 'lyrics': create_placeholder_lyrics()},

    # --- The Dream Chapter: ETERNITY ---
    {
        'id': 'cant_you_see_me', 'album_id': 'eternity', 'title': "Can't You See Me?", 'korean_title': '세계가 불타버린 밤, 우린...',
        'lyrics': [
            {'ko': 'Can\'t you see me?', 'ro': 'Can\'t you see me?', 'zh': '你看不見我嗎？'},
            {'ko': '구해줘', 'ro': 'Guhaejwo', 'zh': '救救我'},
        ]
    },
    {'id': 'drama', 'album_id': 'eternity', 'title': 'Drama', 'korean_title': 'Drama', 'lyrics': create_placeholder_lyrics()},
    {'id': 'shampoo_fairy', 'album_id': 'eternity', 'title': 'Fairy of Shampoo', 'korean_title': '샴푸의 요정', 'lyrics': create_placeholder_lyrics()},
    {'id': 'maze_in_mirror', 'album_id': 'eternity', 'title': 'Maze in the Mirror', 'korean_title': '거울 속의 미로', 'lyrics': create_placeholder_lyrics()},
    {'id': 'puma', 'album_id': 'eternity', 'title': 'PUMA', 'korean_title': '동물원을 빠져나온 퓨마', 'lyrics': create_placeholder_lyrics()},
    {'id': 'eternally', 'album_id': 'eternity', 'title': 'Eternally', 'korean_title': 'Eternally', 'lyrics': create_placeholder_lyrics()},

    # --- The Dream Chapter: MAGIC ---
    {
        'id': 'run_away', 'album_id': 'magic', 'title': 'Run Away', 'korean_title': '9와 4분의 3 승강장에서 너를 기다려',
        'lyrics': [
            {'ko': '도망갈까', 'ro': 'Domanggalkka', 'zh': '要逃跑嗎'},
            {'ko': 'Bibbidi babbidi boo', 'ro': 'Bibbidi babbidi boo', 'zh': 'Bibbidi babbidi boo'},
        ]
    },
    {'id': 'new_rules', 'album_id': 'magic', 'title': 'New Rules', 'korean_title': 'New Rules', 'lyrics': create_placeholder_lyrics()},
    {'id': 'roller_coaster', 'album_id': 'magic', 'title': 'Roller Coaster', 'korean_title': '간지러워', 'lyrics': create_placeholder_lyrics()},
    {'id': 'poppin_star', 'album_id': 'magic', 'title': 'Poppin\' Star', 'korean_title': 'Poppin\' Star', 'lyrics': create_placeholder_lyrics()},
    {'id': 'magic_island', 'album_id': 'magic', 'title': 'Magic Island', 'korean_title': 'Magic Island', 'lyrics': create_placeholder_lyrics()},
    {'id': 'angel_or_devil', 'album_id': 'magic', 'title': 'Angel Or Devil', 'korean_title': 'Angel Or Devil', 'lyrics': create_placeholder_lyrics()},

    # --- The Dream Chapter: STAR ---
    {
        'id': 'crown', 'album_id': 'star', 'title': 'CROWN', 'korean_title': '어느날 머리에서 뿔이 자랐다',
        'lyrics': [
            {'ko': '머리에 뿔이 솟아', 'ro': 'Meorie ppuri sosa', 'zh': '頭上長出了角'},
            {'ko': 'But I love it', 'ro': 'But I love it', 'zh': '但我喜歡它'},
            {'ko': '넌 내 왕관이 돼', 'ro': 'Neon nae wanggwani dwae', 'zh': '你變成了我的皇冠'},
        ]
    },
    {'id': 'blue_orangeade', 'album_id': 'star', 'title': 'Blue Orangeade', 'korean_title': 'Blue Orangeade', 'lyrics': create_placeholder_lyrics()},
    {'id': 'our_summer', 'album_id': 'star', 'title': 'Our Summer', 'korean_title': 'Our Summer', 'lyrics': create_placeholder_lyrics()},
    {'id': 'cat_dog', 'album_id': 'star', 'title': 'Cat & Dog', 'korean_title': 'Cat & Dog', 'lyrics': create_placeholder_lyrics()},
    {'id': 'nap_star', 'album_id': 'star', 'title': 'Nap of a star', 'korean_title': '별의 낮잠', 'lyrics': create_placeholder_lyrics()},
]

# --- 狀態管理 (Session State) ---
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
        border: 1px solid #eee;
    }
    .stButton>button:hover {
        border-color: #aaa;
    }
    .album-card {
        padding: 20px;
        border-radius: 12px;
        color: white;
        text-align: center;
        margin-bottom: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: transform 0.2s;
    }
    .album-card:hover {
        transform: translateY(-2px);
    }
    .korean-text { font-size: 1.3rem; font-weight: bold; margin-bottom: 4px; color: #1F2937; }
    .roman-text { font-size: 0.95rem; color: #6B7280; font-style: italic; margin-bottom: 4px; }
    .chinese-text { font-size: 1.0rem; color: #4F46E5; margin-bottom: 15px; font-weight: 500; }
    .song-list-item {
        padding: 10px;
        border-radius: 8px;
        margin-bottom: 8px;
        border: 1px solid #f0f0f0;
    }
</style>
""", unsafe_allow_html=True)

# --- 側邊欄：搜尋與導航 ---
with st.sidebar:
    st.title("TXT 歌詞庫 🎧")
    
    if st.button("🏠 回首頁"):
        go_to_home()
    
    st.divider()
    
    # 搜尋功能
    search_query = st.text_input("🔍 搜尋歌曲...", placeholder="輸入歌名 (中/韓/英)...").lower()
    
    # 收藏夾預覽
    st.subheader("我的收藏 ❤️")
    if st.session_state.favorites:
        fav_songs = [s for s in SONGS if s['id'] in st.session_state.favorites]
        for song in fav_songs:
            if st.button(f"{song['title']}", key=f"fav_{song['id']}"):
                go_to_song(song)
    else:
        st.info("還沒有收藏歌曲")
        
    st.divider()
    st.caption("MOA Forever ✨")

# --- 主頁面邏輯 ---

# 1. 搜尋結果頁面
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
                st.markdown(f'<div style="background-color:{album["color"]}; width:50px; height:50px; border-radius:50%; display:flex; align-items:center; justify-content:center; color:white; font-size:10px;">{album["year"]}</div>', unsafe_allow_html=True)
            with col2:
                st.markdown(f"**{song['title']}**")
                st.caption(f"{song['korean_title']} • {album['title']}")
                if st.button("查看歌詞", key=f"search_{song['id']}"):
                    go_to_song(song)
                    st.rerun()
            st.divider()
    else:
        st.warning("找不到相關歌曲，試試其他關鍵字？")

# 2. 歌詞詳情頁面
elif st.session_state.page == 'lyrics' and st.session_state.selected_song:
    song = st.session_state.selected_song
    album = ALBUMS[song['album_id']]
    
    # 頂部導航
    col_back, col_empty = st.columns([1, 4])
    with col_back:
        if st.button("← 返回列表"):
            go_to_home()
    
    # 專輯封面與標題區 (模擬)
    st.markdown(f"""
    <div style="text-align: center; padding: 20px; background: linear-gradient(to bottom, {album['color']}22, white); border-radius: 20px;">
        <h1 style='margin-bottom: 0;'>{song['title']}</h1>
        <h3 style='color: #666; margin-top: 5px;'>{song['korean_title']}</h3>
        <p style='color: gray; font-size: 0.9em;'>{album['title']} ({album['year']})</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("") # Spacer

    # 控制按鈕 (收藏)
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        is_fav = song['id'] in st.session_state.favorites
        if st.button("❤️ 取消收藏" if is_fav else "🤍 加入收藏", use_container_width=True):
            toggle_favorite(song['id'])
            st.rerun()

    st.divider()
    
    # 顯示選項
    col_opt1, col_opt2 = st.columns(2)
    with col_opt1:
        show_roman = st.checkbox("顯示羅馬拼音 (Romanization)", value=True)
    with col_opt2:
        show_zh = st.checkbox("顯示中文翻譯 (Translation)", value=True)
    
    st.divider()

    # 歌詞渲染
    for line in song['lyrics']:
        st.markdown(f"<div class='korean-text'>{line['ko']}</div>", unsafe_allow_html=True)
        
        if show_roman:
            st.markdown(f"<div class='roman-text'>{line['ro']}</div>", unsafe_allow_html=True)
            
        if show_zh:
            st.markdown(f"<div class='chinese-text'>{line['zh']}</div>", unsafe_allow_html=True)
        
        st.write("") # 空行間隔
    
    if song['lyrics'][0]['ko'] == '가사가 준비 중입니다.':
        st.info("💡 提示：此為 B-side 歌曲範本，您可以在程式碼的 SONGS 列表中填入完整歌詞。")

# 3. 首頁 (專輯牆與列表)
else:
    st.title("Hello, MOA! ✨")
    st.write("請選擇專輯瀏覽歌曲：")
    
    # 取得所有專輯 ID
    album_ids = list(ALBUMS.keys())
    
    # 建立 Tabs (因專輯較多，使用 Tabs 分類顯示可能太擠，這裡改用 Selectbox 或 Expander，或者直接用 Tabs 但要注意數量)
    # 為了美觀，我們將專輯分為「最新發行」和「經典系列」
    
    tab_new, tab_all = st.tabs(["最新發行 (Latest)", "所有專輯 (All Albums)"])
    
    with tab_new:
        # 顯示最新的 3 張專輯
        latest_albums = album_ids[:3]
        for aid in latest_albums:
            album = ALBUMS[aid]
            with st.expander(f"{album['year']} | {album['title']}", expanded=True):
                st.markdown(
                    f"""<div style="height: 5px; background: {album['color']}; border-radius: 5px; margin-bottom: 10px;"></div>""", 
                    unsafe_allow_html=True
                )
                album_songs = [s for s in SONGS if s['album_id'] == aid]
                for song in album_songs:
                     # 簡單列表
                    if st.button(f"🎵 {song['title']}", key=f"new_{song['id']}"):
                        go_to_song(song)
                        st.rerun()

    with tab_all:
        # 顯示所有專輯
        selected_album_id = st.selectbox("選擇專輯:", options=album_ids, format_func=lambda x: ALBUMS[x]['title'])
        
        if selected_album_id:
            album = ALBUMS[selected_album_id]
            st.markdown(
                f"""
                <div class="album-card" style="background: linear-gradient(135deg, {album['color']}, #888);">
                    <h2>{album['title']}</h2>
                    <p>{album['year']}</p>
                </div>
                """, 
                unsafe_allow_html=True
            )
            
            album_songs = [s for s in SONGS if s['album_id'] == selected_album_id]
            
            for song in album_songs:
                c1, c2 = st.columns([4, 1])
                with c1:
                    st.write(f"**{song['title']}**")
                    st.caption(song['korean_title'])
                with c2:
                    if st.button("歌詞", key=f"all_{song['id']}"):
                        go_to_song(song)
                        st.rerun()
                st.divider()
