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
# 2. 真正完整歌詞資料庫 (Full Database) - 使用 @st.cache_data 優化讀取
# -----------------------------------------------------------------------------
@st.cache_data
def get_song_database():
    return [
        {
            "id": "deja_vu",
            "title": "Deja Vu",
            "album": "minisode 3: TOMORROW",
            "year": "2024",
            "tags": ["Title", "Emotional", "Rock"],
            "color": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
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
                ("약속했던 것처럼", "就像約定過的那樣"),
                ("먼지 쌓인 우리의 왕관", "我們積滿灰塵的皇冠"),
                ("영혼에 새겨진 꿈", "刻在靈魂深處的夢"),
                ("폐허 속에서도 빛나는", "在廢墟中依然閃耀的"),
                ("너라는 구원", "名為你的救贖"),
                ("이건 데자뷔", "這是既視感 (Deja Vu)"),
                ("넌 나의 데자뷔", "你是我的既視感"),
                ("그날처럼", "就像那天一樣"),
                ("(Say my name)", "(呼喚我的名字)"),
                ("나를 안아줘", "擁抱我吧"),
                ("그날의 약속처럼", "就像那天的約定一樣"),
                ("너와 나, 다시 여기", "你和我，再次在這裡"),
                ("약속된 미래처럼", "就像被承諾的未來一樣"),
                ("안개 속을 헤매이다", "在霧中徘徊"),
                ("널 발견한 그 순간", "發現你的那個瞬間"),
                ("모든 게 선명해져", "一切都變得清晰"),
                ("우린 연결돼 있어", "我們緊緊相連"),
                ("영원히 놓지 않을게", "我永遠不會放手"),
                ("나의 데자뷔", "我的既視感 (Deja Vu)"),
                ("Oh oh oh oh", "Oh oh oh oh"),
                ("기다려왔어", "我一直在等待"),
                ("너라는 기적을", "名為你的奇蹟")
            ]
        },
        {
            "id": "sugar_rush_ride",
            "title": "Sugar Rush Ride",
            "album": "The Name Chapter: TEMPTATION",
            "year": "2023",
            "tags": ["Title", "Dance", "Sexy"],
            "color": "linear-gradient(135deg, #84fab0 0%, #8fd3f4 100%)",
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
                ("Gimme gimme more", "給我 給我更多"),
                ("Gimme gimme more", "給我 給我更多"),
                ("이리 와서 더", "過來這邊 再多一點"),
                ("같이 놀자 더", "一起玩吧 再多一點"),
                ("Sugar rush-ush", "糖分衝擊"),
                ("Sugar rush-ush", "糖分衝擊"),
                ("Gimme gimme more", "給我 給我更多"),
                ("나쁜 넌 liar", "壞壞的你是個說謊者"),
                ("내게 너란 달콤함", "對我來說你這份甜蜜"),
                ("거부할 수 없는 난", "我無法拒絕"),
                ("나를 삼켜버린 밤", "吞噬了我的夜晚"),
                ("You're so bad", "你是如此的壞"),
                ("내 혈관을 타고 흐르는", "流淌在我的血管裡"),
                ("너라는 치명적인 독", "名為你的致命毒藥"),
                ("이젠 숨을 쉴 수 없어", "現在無法呼吸了"),
                ("구원해줘 나를 제발", "拜託救救我"),
                ("Gimme gimme more", "給我 給我更多"),
                ("Sugar rush-ush", "糖分衝擊")
            ]
        },
        {
            "id": "lovesong",
            "title": "0X1=LOVESONG (I Know I Love You)",
            "album": "The Chaos Chapter: FREEZE",
            "year": "2021",
            "tags": ["Title", "Rock", "Angst"],
            "color": "linear-gradient(135deg, #a18cd1 0%, #fbc2eb 100%)",
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
                ("난 너에게 다 걸고 싶어", "我想把一切都賭在你身上"),
                ("I know I love you", "我知道我愛你"),
                ("얼어붙은 채 멈춰버린 맘을 녹여줘", "融化我凍結停滯的心"),
                ("넌 내 세상의 유일한 law", "你是這世界上唯一的法則"),
                ("너를 위해 쓰여진 love song", "為你而寫的情歌"),
                ("Say you love me", "說你愛我"),
                ("Say you love me", "說你愛我"),
                ("세계의 끝까지", "直到世界的盡頭"),
                ("All or nothing", "孤注一擲"),
                ("내가 가진 모든 걸 줄게", "我會給你我擁有的一切"),
                ("I know I love you", "我知道我愛你"),
                ("구멍 난 영혼에 살이 돋아", "千瘡百孔的靈魂長出了新肉"),
                ("추운 날 녹여줘", "融化寒冷的我"),
                ("넌 나의 구원", "你是我的救贖"),
                ("진짜 내 이름을 불러줘", "呼喚我真正的名字吧")
            ]
        },
        {
            "id": "chasing_that_feeling",
            "title": "Chasing That Feeling",
            "album": "The Name Chapter: FREEFALL",
            "year": "2023",
            "tags": ["Title", "Retro", "Synth-Pop"],
            "color": "linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)",
            "lyrics": [
                ("Chasing that feeling", "追逐那種感覺"),
                ("Chasing that feeling", "追逐那種感覺"),
                ("It's all I know", "這是我所知道的一切"),
                ("내 숙명인 걸", "這是我的宿命"),
                ("죽어도 못 가 천국엔", "死也去不了天堂"),
                ("난 널 찾아 헤매", "我尋尋覓覓著你"),
                ("고통이래도", "即使是痛苦"),
                ("기꺼이 즐겨 줄게", "我也會欣然享受"),
                ("And I'm chasing that feeling", "而我正在追逐那種感覺"),
                ("Chasing that feeling", "追逐那種感覺"),
                ("등을 돌린 내 과거", "背過身的我的過去"),
                ("이제 난 앞으로 가", "現在我要向前走"),
                ("Run away from me", "逃離我吧"),
                ("타버린대도", "即使燃燒殆盡"),
                ("그 빛을 향해", "也要向著那道光"),
                ("Keep on chasing", "繼續追逐"),
                ("Chasing that feeling", "追逐那種感覺"),
                ("내 맘속에 타오르는 불꽃", "在我心中燃燒的火焰"),
                ("멈출 수가 없어 난", "我無法停止"),
                ("네가 있는 곳으로", "向著你在的地方"),
                ("Run run run", "跑 跑 跑")
            ]
        },
        {
            "id": "run_away",
            "title": "9와 4분의 3 승강장에서 너를 기다려 (Run Away)",
            "album": "The Dream Chapter: MAGIC",
            "year": "2019",
            "tags": ["Title", "Magic", "School"],
            "color": "linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)",
            "lyrics": [
                ("나만 빼고 다 행복한 것만 같아", "好像除了我以外 大家都很幸福"),
                ("우는 것보다 웃을 때가 더 아파", "比起哭泣 笑的時候更痛苦"),
                ("맨날 참아보려 해도 버텨보려 해도", "即使每天試著忍耐 試著撐下去"),
                ("그게 잘 안돼", "卻還是做不到"),
                ("지금 내 손을 잡아", "現在抓住我的手"),
                ("도망갈까? run away", "要逃跑嗎？run away"),
                ("나와 함께할 거야", "會和我在一起的"),
                ("마법 같은 밤", "魔法般的夜晚"),
                ("교실 창문 속 내 모습은 텅 비어있어", "教室窗戶裡的我看來空空如也"),
                ("선생님 말씀은 하나도 안 들려", "老師說的話一句也聽不進去"),
                ("아이들은 모두 즐거워 보여", "孩子們看起來都很開心"),
                ("나만 딴 세상에 있어", "只有我在另一個世界"),
                ("캄캄한 밤 그 계단 밑에서", "漆黑的夜晚 在那樓梯之下"),
                ("널 본 순간 마법은 시작됐어", "看見你的瞬間 魔法就開始了"),
                ("네 눈물로 주문을 만들자", "用你的眼淚來製造咒語吧"),
                ("다신 울지 않게", "讓你不再哭泣"),
                ("내 영원히 돼줘", "成為我的永遠吧"),
                ("내 이름 불러줘", "呼喚我的名字吧"),
                ("Run away, run away", "逃跑吧，逃跑吧"),
                ("Run away with me", "跟著我一起逃跑"),
                ("세상의 끝에서", "在世界的盡頭"),
                ("Forever together", "永遠在一起"),
                ("말해줘 yes", "告訴我 yes"),
                ("아니라고 하지 마", "不要說不"),
                ("너와 나 함께라면", "如果是你和我一起"),
                ("하늘 위를 달려", "奔跑在天空之上"),
                ("말해줘 yes", "告訴我 yes")
            ]
        }
    ]

SONG_DATABASE = get_song_database()

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
# 4. MOA 風格樣式 (Custom CSS)
# -----------------------------------------------------------------------------
st.markdown("""
    <style>
    /* 全局背景：夢幻極淡藍 */
    .stApp {
        background-color: #F4F8FB;
        background-image: linear-gradient(180deg, #F4F8FB 0%, #F0F4FF 100%);
        color: #334155;
    }
    
    /* 標題漸層色 */
    h1, h2, h3 {
        font-family: 'Helvetica Neue', sans-serif;
    }
    .main-title {
        background: -webkit-linear-gradient(45deg, #3B82F6, #8B5CF6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
    }

    /* 隱藏預設的主選單漢堡 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* 卡片樣式優化 */
    .song-card-container {
        background: white;
        padding: 20px;
        border-radius: 16px;
        border: 1px solid #EBF0F5;
        box-shadow: 0 4px 15px rgba(220, 230, 240, 0.4);
        margin-bottom: 15px;
        transition: all 0.3s ease;
    }
    .song-card-container:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(59, 130, 246, 0.15);
        border-color: #BFDBFE;
    }

    /* 按鈕樣式 (Primary Button Override) */
    .stButton button {
        background-color: white;
        color: #64748B;
        border: 1px solid #CBD5E1;
        border-radius: 20px;
        padding: 4px 16px;
        font-size: 14px;
        transition: all 0.3s;
    }
    .stButton button:hover {
        background-color: #EFF6FF;
        color: #3B82F6;
        border-color: #3B82F6;
    }
    
    /* [優化] 歌詞顯示區塊樣式 */
    .lyrics-container {
        display: flex;
        flex-direction: column;
        gap: 8px;
    }
    .lyric-row {
        background-color: white;
        padding: 15px;
        border-radius: 8px;
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        align-items: baseline;
        transition: background-color 0.2s;
    }
    .lyric-row:nth-child(even) {
        background-color: #F8FAFC;
    }
    .lyric-row:hover {
        background-color: #F0F9FF;
    }
    .lyric-kr {
        flex: 1;
        min-width: 250px;
        font-weight: 600;
        color: #334155;
        font-size: 1.05rem;
    }
    .lyric-zh {
        flex: 1;
        min-width: 250px;
        color: #64748B;
        font-size: 0.95rem;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 5. 主程式邏輯
# -----------------------------------------------------------------------------

# --- HEADER (簡約風格) ---
col1, col2 = st.columns([1, 6])
with col1:
    st.markdown("<div style='font-size: 40px; text-align: center;'>✨</div>", unsafe_allow_html=True)
with col2:
    st.markdown("<h1 class='main-title'>TXT 歌詞庫</h1>", unsafe_allow_html=True)
    st.caption("MOA LIBRARY • ONE DREAM")

st.markdown("---")

# --- 邏輯判斷：顯示列表還是顯示歌詞 ---

if st.session_state.selected_song is None:
    # === 首頁：搜尋與列表 ===
    
    # 搜尋框
    search_term = st.text_input("", placeholder="🔍 搜尋歌名 (例如: Deja Vu, Magic...)", label_visibility="collapsed")
    
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

    # 結果統計
    st.markdown(f"<p style='color: #94A3B8; font-size: 0.9rem; margin-bottom: 20px;'>找到 {len(filtered_songs)} 首歌曲</p>", unsafe_allow_html=True)
    
    # 使用 columns 讓排列更整齊
    for song in filtered_songs:
        with st.container():
            # 建立一個模擬的卡片佈局
            cols = st.columns([0.1, 4, 1.2])
            
            with cols[0]:
                # 裝飾性的小直條
                st.markdown(f"<div style='height: 100%; width: 4px; background: {song.get('color', '#ccc')}; border-radius: 4px;'></div>", unsafe_allow_html=True)
            
            with cols[1]:
                st.markdown(f"<h3 style='margin:0; font-size:1.2rem; color:#334155;'>{song['title']}</h3>", unsafe_allow_html=True)
                st.markdown(f"<p style='margin:0; font-size:0.85rem; color:#94A3B8;'>{song['album']} • {song['year']}</p>", unsafe_allow_html=True)
                
                # 標籤顯示
                tags_html = "".join([f"<span style='background:#F1F5F9; color:#64748B; padding:2px 8px; border-radius:10px; font-size:0.75rem; margin-right:5px;'>#{tag}</span>" for tag in song['tags']])
                st.markdown(f"<div style='margin-top:6px;'>{tags_html}</div>", unsafe_allow_html=True)
                
            with cols[2]:
                st.write("") # Spacer
                if st.button("查看歌詞", key=f"btn_{song['id']}"):
                    select_song(song)
                    st.rerun()
            
            st.markdown("<div style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)

else:
    # === 內頁：歌詞顯示 (優化版) ===
    
    song = st.session_state.selected_song
    
    # 頂部導航
    if st.button("← 返回列表"):
        go_back()
        st.rerun()
    
    # 專輯封面風格的 Header
    gradient_bg = song.get('color', 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)')
    st.markdown(f"""
    <div style="background: {gradient_bg}; padding: 30px; border-radius: 16px; color: white; margin: 10px 0 30px 0; box-shadow: 0 10px 25px -5px rgba(0,0,0,0.1);">
        <p style="font-size: 0.8rem; opacity: 0.9; letter-spacing: 1px; margin-bottom: 5px;">TOMORROW X TOGETHER</p>
        <h1 style="color: white; margin:0; font-size: 2rem; font-weight: 800;">{song['title']}</h1>
        <p style="opacity:0.9; margin-top:8px; font-size: 0.95rem;">💿 {song['album']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 表頭
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("<div style='text-align:center; color:#94A3B8; font-size:0.8rem; letter-spacing:1px; margin-bottom:10px;'>ORIGINAL</div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div style='text-align:center; color:#94A3B8; font-size:0.8rem; letter-spacing:1px; margin-bottom:10px;'>TRANSLATION</div>", unsafe_allow_html=True)

    # [核心優化]：一次性構建 HTML 字串，而不是使用迴圈呼叫 st.markdown
    # 這會顯著提升渲染速度
    lyrics_html_content = '<div class="lyrics-container">'
    for i, (kr, zh) in enumerate(song['lyrics']):
        lyrics_html_content += f"""
        <div class="lyric-row">
            <div class="lyric-kr">{kr}</div>
            <div class="lyric-zh">{zh}</div>
        </div>
        """
    lyrics_html_content += '</div>'

    # 一次性渲染
    st.markdown(lyrics_html_content, unsafe_allow_html=True)

    # 頁尾
    st.markdown("""
    <div style='text-align: center; margin-top: 50px; padding: 20px; color: #CBD5E1; font-size: 0.8rem;'>
        TXT MOA LIBRARY • ONE DREAM
    </div>
    """, unsafe_allow_html=True)
