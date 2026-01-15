import streamlit as st

# -----------------------------------------------------------------------------
# 1. 設定頁面配置 (必須是第一行指令)
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="TXT 歌詞庫 (MOA Library)",
    page_icon="✨",
    layout="centered"
)

# -----------------------------------------------------------------------------
# 2. 模擬資料庫 (Database)
# -----------------------------------------------------------------------------
SONG_DATABASE = [
    {
        "id": "deja_vu",
        "title": "Deja Vu",
        "album": "minisode 3: TOMORROW",
        "year": "2024",
        "tags": ["Title", "Emotional", "Rock"],
        "lyrics": [
            ("기억해", "記得嗎"),
            ("과거의 틈 사이로", "在過去的縫隙之間"),
            ("널 보던 나의 눈을", "我看著你的那雙眼睛"),
            ("폐허 속의 모르스부호", "廢墟中的摩斯密碼"),
            ("그 약속을 너는 알잖아", "你知道那個約定的"),
            ("마치 데자뷔", "就像既視感 (Deja Vu)"),
            ("도망쳐 봐도", "即使試著逃跑"),
            ("결국엔 너잖아", "最終還是你啊"),
            ("수만 번의 뒤척임 끝에", "在數萬次的輾轉反側之後"),
            ("다시 만날 우리인 거야", "我們是註定會再次相遇的"),
            ("(Say my name)", "(呼喚我的名字)"),
            ("나를 안아줘", "擁抱我吧"),
            ("약속했던 것처럼", "就像約定過的那樣")
        ]
    },
    {
        "id": "sugar_rush_ride",
        "title": "Sugar Rush Ride",
        "album": "The Name Chapter: TEMPTATION",
        "year": "2023",
        "tags": ["Title", "Dance", "Sexy"],
        "lyrics": [
            ("생각은 곶, 숨을 멈춰", "思緒立即停止，屏住呼吸"),
            ("When you get back", "當你回來時"),
            ("내 맘을 넌, 휩쓸어 가", "你席捲了我的心"),
            ("Sugar rush-ush", "糖分衝擊"),
            ("Sugar rush-ush", "糖分衝擊"),
            ("어느새 난, 이끌려 가", "不知不覺間，我被吸引過去"),
            ("거부할 수가 없어", "無法拒絕"),
            ("달콤한 그 Devilish smile", "那甜美惡魔般的微笑"),
            ("넌 능숙히 잠긴 내 문을 열어", "你熟練地打開我上鎖的門"),
            ("어떡해 저 별이 보여", "怎麼辦 我看見星星了"),
            ("The devil said", "惡魔說道"),
            ("Gimme gimme more", "給我 給我更多")
        ]
    },
    {
        "id": "lovesong",
        "title": "0X1=LOVESONG (I Know I Love You)",
        "album": "The Chaos Chapter: FREEZE",
        "year": "2021",
        "tags": ["Title", "Rock", "Angst"],
        "lyrics": [
            ("I know I love you", "我知道我愛你"),
            ("이 제로의 세계 속", "在這個歸零的世界裡"),
            ("I know you’re my one and only", "我知道你是我的唯一"),
            ("이 끝이 없던 어둠 속", "在這無盡的黑暗中"),
            ("Like oh my god, so holy", "就像，天啊，如此神聖"),
            ("모든 게 다 무너져도", "即使一切都崩塌"),
            ("너를 붙잡고 싶어", "我也想緊緊抓住你"),
            ("Say you love me", "說你愛我"),
            ("Say you love me", "說你愛我"),
            ("세계의 끝까지", "直到世界的盡頭"),
            ("All or nothing", "孤注一擲"),
            ("난 너에게 다 걸고 싶어", "我想把一切都賭在你身上")
        ]
    },
    {
        "id": "run_away",
        "title": "9와 4분의 3 승강장에서 너를 기다려 (Run Away)",
        "album": "The Dream Chapter: MAGIC",
        "year": "2019",
        "tags": ["Title", "Magic", "School"],
        "lyrics": [
            ("나만 빼고 다 행복한 것만 같아", "好像除了我以外 大家都很幸福"),
            ("우는 것보다 웃을 때가 더 아파", "比起哭泣 笑的時候更痛苦"),
            ("맨날 참아보려 해도 버텨보려 해도", "即使每天試著忍耐 試著撐下去"),
            ("그게 잘 안돼", "卻還是做不到"),
            ("지금 내 손을 잡아", "現在抓住我的手"),
            ("도망갈까? run away", "要逃跑嗎？run away"),
            ("나와 함께할 거야", "會和我在一起的"),
            ("마법 같은 밤", "魔法般的夜晚")
        ]
    }
]

# -----------------------------------------------------------------------------
# 3. 狀態管理 (Session State)
# -----------------------------------------------------------------------------
if 'selected_song' not in st.session_state:
    st.session_state.selected_song = None

def select_song(song):
    st.session_state.selected_song = song

def go_back():
    st.session_state.selected_song = None

# -----------------------------------------------------------------------------
# 4. 樣式 (Custom CSS) - 增加一點 TXT 風格
# -----------------------------------------------------------------------------
st.markdown("""
    <style>
    .stApp {
        background-color: #F8FAFC;
    }
    .song-card {
        padding: 1.5rem;
        border-radius: 10px;
        background-color: white;
        border: 1px solid #E2E8F0;
        margin-bottom: 1rem;
        transition: transform 0.2s;
    }
    .song-card:hover {
        border-color: #3B82F6;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    .lyric-row {
        padding: 10px 0;
        border-bottom: 1px dashed #eee;
    }
    h1 {
        background: -webkit-linear-gradient(45deg, #2563EB, #9333EA);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 5. 主程式邏輯
# -----------------------------------------------------------------------------

# --- HEADER ---
col1, col2 = st.columns([1, 5])
with col1:
    st.markdown("# ✨")
with col2:
    st.markdown("# TXT 歌詞庫")
    st.caption("MOA LIBRARY - Python Edition")

st.divider()

# --- 邏輯判斷：顯示列表還是顯示歌詞 ---

if st.session_state.selected_song is None:
    # === 首頁：搜尋與列表 ===
    
    # 搜尋框
    search_term = st.text_input("🔍 搜尋歌名...", placeholder="輸入 Deja Vu, Run Away...")
    
    # 篩選邏輯
    filtered_songs = []
    if search_term:
        term = search_term.lower()
        filtered_songs = [
            s for s in SONG_DATABASE 
            if term in s['title'].lower() or term in s['album'].lower()
        ]
    else:
        filtered_songs = SONG_DATABASE

    # 顯示結果
    st.markdown(f"**找到 {len(filtered_songs)} 首歌曲**")
    
    for song in filtered_songs:
        # 由於 Streamlit 按鈕不能包住 HTML div，我們用 container 模擬
        with st.container():
            col_info, col_btn = st.columns([4, 1])
            with col_info:
                st.subheader(song['title'])
                st.caption(f"🎵 {song['album']} • {song['year']}")
                st.markdown(" ".join([f"`#{tag}`" for tag in song['tags']]))
            with col_btn:
                # 每個按鈕需要唯一的 key
                if st.button("查看歌詞", key=f"btn_{song['id']}"):
                    select_song(song)
                    st.rerun() # 重新執行以切換頁面
            st.markdown("---")

else:
    # === 內頁：歌詞顯示 ===
    
    song = st.session_state.selected_song
    
    # 返回按鈕
    if st.button("← 返回搜尋"):
        go_back()
        st.rerun()
    
    # 歌曲標題區
    st.markdown(f"""
    <div style="background: linear-gradient(to right, #3B82F6, #9333EA); padding: 20px; border-radius: 12px; color: white; margin-bottom: 20px;">
        <h2 style="margin:0;">{song['title']}</h2>
        <p style="opacity:0.8; margin-top:5px;">{song['album']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 歌詞顯示 (兩欄式)
    col_kr, col_zh = st.columns(2)
    
    with col_kr:
        st.markdown("### 🇰🇷 Korean")
    with col_zh:
        st.markdown("### 🇹🇼 Chinese")
    
    for kr, zh in song['lyrics']:
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f"**{kr}**")
        with c2:
            st.markdown(f"<span style='color:#64748B'>{zh}</span>", unsafe_allow_html=True)
        st.markdown("<hr style='margin: 5px 0; border: none; border-top: 1px dashed #eee;'/>", unsafe_allow_html=True)

    # 頁尾
    st.caption("歌詞僅供學習交流使用 • TOMORROW X TOGETHER")
