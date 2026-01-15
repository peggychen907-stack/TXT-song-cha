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
            {'ko': 'Yeah, you are my everything', 'ro': 'Yeah, you are my everything', 'zh': '是的，你是我的一切'},
            {'ko': 'Hold me tight', 'ro': 'Hold me tight', 'zh': '緊緊抱住我'},
            {'ko': '달빛이 차오르는 밤', 'ro': 'Dalbichi chaoreuneun bam', 'zh': '月光滿溢的夜晚'},
            {'ko': 'Over the moon', 'ro': 'Over the moon', 'zh': 'Over the moon'},
            {'ko': '내 세상은 너로 가득 차', 'ro': 'Nae sesangeun neoro gadeuk cha', 'zh': '我的世界充滿了你'},
            {'ko': 'So let me love you', 'ro': 'So let me love you', 'zh': '所以讓我愛你'},
            {'ko': 'You make me feel like', 'ro': 'You make me feel like', 'zh': '你讓我感覺像'},
            {'ko': 'Over the moon', 'ro': 'Over the moon', 'zh': 'Over the moon'},
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
            {'ko': '머릿속을 맴도는 얼굴', 'ro': 'Meoritsogeul maemdoneun eolgul', 'zh': '腦海中盤旋的那張臉'},
            {'ko': '나의 미래는 너야', 'ro': 'Naui miraeneun neoya', 'zh': '我的未來就是你'},
            {'ko': 'Say my name', 'ro': 'Say my name', 'zh': '呼喚我的名字'},
            {'ko': '마치 데자뷔', 'ro': 'Machi dejabwi', 'zh': '就像既視感 (Deja Vu)'},
            {'ko': '약속을 너만은 기억할 테니', 'ro': 'Yaksogeul neomaneun gieokhal teni', 'zh': '因為只有你會記得那個約定'},
            {'ko': 'I promise you', 'ro': 'I promise you', 'zh': '我向你保證'},
            {'ko': '몇 번을 반복해도', 'ro': 'Myeot beoneul banbokhaedo', 'zh': '無論重複多少次'},
            {'ko': '나의 미래는 너야', 'ro': 'Naui miraeneun neoya', 'zh': '我的未來就是你'},
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
            {'ko': '내일도 난 제자리야', 'ro': 'Naeildo nan jejariya', 'zh': '明天我也會在原地'},
            {'ko': 'I\'m chasing that feeling', 'ro': 'I\'m chasing that feeling', 'zh': '我在追逐那種感覺'},
            {'ko': '망가진 나라도 괜찮아', 'ro': 'Manggajin narado gwaenchana', 'zh': '即使壞掉的我也可以'},
            {'ko': '죽어 가던 나의 아픔까지', 'ro': 'Jugeo gadeon naui apeumkkaji', 'zh': '連同我漸漸死去的痛苦'},
            {'ko': '사랑할래 chasing that feeling', 'ro': 'Saranghallae chasing that feeling', 'zh': '我要去愛 chasing that feeling'},
            {'ko': 'Chasing that feeling', 'ro': 'Chasing that feeling', 'zh': '追逐那種感覺'},
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
            {'ko': '생각은 멈춰', 'ro': 'Saenggageun meomchwo', 'zh': '停止思考'},
            {'ko': '직감만 남겨', 'ro': 'Jikgamman namgyeo', 'zh': '只留下直覺'},
            {'ko': '거부할 수 없는 이 이끌림', 'ro': 'Geobuhal su eomneun i ikkeullim', 'zh': '這無法抗拒的吸引力'},
            {'ko': 'Gimme gimme more', 'ro': 'Gimme gimme more', 'zh': '給我更多 給我更多'},
            {'ko': 'Sugar rush-ush', 'ro': 'Sugar rush-ush', 'zh': '糖分衝擊'},
            {'ko': 'Sugar rush-ush', 'ro': 'Sugar rush-ush', 'zh': '糖分衝擊'},
            {'ko': '나쁜 넌 liar', 'ro': 'Nappeun neon liar', 'zh': '壞壞的你是 liar'},
            {'ko': '내게 너 뭘 한 거야', 'ro': 'Naege neo mwol han geoya', 'zh': '你對我做了什麼'},
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
            {'ko': '부드러운 파도 앞에 무너져', 'ro': 'Budeureoun pado ape muneojyeo', 'zh': '在溫柔的海浪面前倒塌'},
            {'ko': 'Good boy gone bad', 'ro': 'Good boy gone bad', 'zh': '好男孩變壞了'},
            {'ko': '다 내던져 난', 'ro': 'Da naedeonjyeo nan', 'zh': '我全部拋棄'},
            {'ko': 'Good boy gone bad', 'ro': 'Good boy gone bad', 'zh': '好男孩變壞了'},
            {'ko': '네가 했던 날', 'ro': 'Nega haetdeon nal', 'zh': '你曾愛過的我'},
            {'ko': '가슴팍엔 흉터', 'ro': 'Gaseumpagen hyungteo', 'zh': '胸口的傷疤'},
            {'ko': 'Gone dead', 'ro': 'Gone dead', 'zh': 'Gone dead'},
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
            {'ko': 'Is it a r-run or r-run?', 'ro': 'Is it a r-run or r-run?', 'zh': '是逃跑還是奔跑？'},
            {'ko': '나를 구원해 준 너', 'ro': 'Nareul guwonhae jun neo', 'zh': '拯救了我的你'},
            {'ko': '너와 함께라면 추락도 아름다워', 'ro': 'Neowa hamkkeramyeon churakdo areumdawo', 'zh': '只要和你在一起 墜落也美麗'},
            {'ko': 'I\'m a loser', 'ro': 'I\'m a loser', 'zh': '我是個失敗者'},
        ]
    },
    {
        'id': 'lovesong', 'album_id': 'freeze', 'title': '0X1=LOVESONG (I Know I Love You)', 'korean_title': '0X1=LOVESONG',
        'lyrics': [
            {'ko': 'I know I love you', 'ro': 'I know I love you', 'zh': '我知道我愛你'},
            {'ko': '이 제로의 세계 속', 'ro': 'I jeroui segye sok', 'zh': '在這個歸零的世界裡'},
            {'ko': 'I know you’re my one and only', 'ro': 'I know you’re my one and only', 'zh': '我知道你是我的唯一'},
            {'ko': '이 끝이 없던 어둠 속', 'ro': 'I kkeuchi eopdeon eodum sok', 'zh': '在這無盡的黑暗之中'},
            {'ko': 'Like oh my god, so holy', 'ro': 'Like oh my god, so holy', 'zh': 'Like oh my god, so holy'},
            {'ko': '뭐든 다 내던져 안 될 건 없어', 'ro': 'Mwodeun da naedeonjyeo an doel geon eopseo', 'zh': '拋開一切 沒有什麼是不行的'},
            {'ko': 'I love you', 'ro': 'I love you', 'zh': '我愛你'},
            {'ko': '난 문제 투성이 love sick', 'ro': 'Nan munje tuseongi love sick', 'zh': '我這滿是問題的 love sick'},
            {'ko': '길이 없었어', 'ro': 'Giri eopseosseo', 'zh': '曾經無路可走'},
            {'ko': '죽어도 좋았어', 'ro': 'Jugeodo joasseo', 'zh': '曾經死了也好'},
            {'ko': 'I’m a loser in this game', 'ro': 'I’m a loser in this game', 'zh': '在這場遊戲裡我是個輸家'},
            {'ko': '세계의 유일한 법칙', 'ro': 'Segyeui yuilhan beopchik', 'zh': '世界的唯一法則'},
            {'ko': '나를 구해줘', 'ro': 'Nareul guhaejwo', 'zh': '請拯救我'},
            {'ko': '내 손을 잡아줘', 'ro': 'Nae soneul jabajwo', 'zh': '請抓住我的手'},
            {'ko': 'Please use me like a drug', 'ro': 'Please use me like a drug', 'zh': 'Please use me like a drug'},
            {'ko': 'I know I love you', 'ro': 'I know I love you', 'zh': '我知道我愛你'},
            {'ko': '이 제로의 세계 속', 'ro': 'I jeroui segye sok', 'zh': '在這個歸零的世界裡'},
            {'ko': 'I know you’re my one and only', 'ro': 'I know you’re my one and only', 'zh': '我知道你是我的唯一'},
            {'ko': '구멍 난 영혼에 살이 돋아', 'ro': 'Gumeong nan yeonghone sari doda', 'zh': '破洞的靈魂長出了新肉'},
            {'ko': '얼어붙은 지구 위', 'ro': 'Eoreobuteun jigu wi', 'zh': '在冰凍的地球上'},
            {'ko': 'Say you love me', 'ro': 'Say you love me', 'zh': '說你愛我'},
            {'ko': '세상의 끝까지', 'ro': 'Sesangui kkeutkkaji', 'zh': '直到世界的盡頭'},
            {'ko': 'All or nothing', 'ro': 'All or nothing', 'zh': 'All or nothing'},
            {'ko': 'I give it all to you', 'ro': 'I give it all to you', 'zh': '我把一切都給你'},
            {'ko': 'I know I love you', 'ro': 'I know I love you', 'zh': '我知道我愛你'},
            {'ko': 'Say you love me', 'ro': 'Say you love me', 'zh': '說你愛我'},
            {'ko': '세상의 끝까지', 'ro': 'Sesangui kkeutkkaji', 'zh': '直到世界的盡頭'},
            {'ko': 'All or nothing', 'ro': 'All or nothing', 'zh': 'All or nothing'},
            {'ko': 'I give it all to you', 'ro': 'I give it all to you', 'zh': '我把一切都給你'},
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
            {'ko': '난 어색함이 너무 싫어', 'ro': 'Nan eosaekhami neomu sireo', 'zh': '我非常討厭尷尬'},
            {'ko': '그냥 웃지 baby', 'ro': 'Geunyang utji baby', 'zh': '就笑一笑吧 baby'},
            {'ko': 'Cuz of imagination', 'ro': 'Cuz of imagination', 'zh': '因為想像力'},
            {'ko': '저 하늘의 오렌지빛 마법이', 'ro': 'Jeo haneurui orenjibit mabeobi', 'zh': '那天空中橙色的魔法'},
            {'ko': '끝이 나기 전에', 'ro': 'Kkeuchi nagi jeone', 'zh': '在結束之前'},
            {'ko': 'Cuz of imagination', 'ro': 'Cuz of imagination', 'zh': '因為想像力'},
            {'ko': '그 찰나에', 'ro': 'Geu challae', 'zh': '在那剎那'},
            {'ko': 'Can you feel the rush', 'ro': 'Can you feel the rush', 'zh': 'Can you feel the rush'},
            {'ko': 'Hour, woah woah', 'ro': 'Hour, woah woah', 'zh': 'Hour, woah woah'},
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
            {'ko': '마법은 끝났어', 'ro': 'Mabeobeun kkeunnasseo', 'zh': '魔法結束了'},
            {'ko': 'Can\'t you see me?', 'ro': 'Can\'t you see me?', 'zh': '你看不見我嗎？'},
            {'ko': '마법진은 무너지고', 'ro': 'Mabeopjineun muneojigo', 'zh': '魔法陣崩塌了'},
            {'ko': '구해줘', 'ro': 'Guhaejwo', 'zh': '救救我'},
            {'ko': 'Can\'t you see me?', 'ro': 'Can\'t you see me?', 'zh': '你看不見我嗎？'},
            {'ko': 'Friends don\'t understand me', 'ro': 'Friends don\'t understand me', 'zh': '朋友們不理解我'},
            {'ko': 'Bad bad', 'ro': 'Bad bad', 'zh': 'Bad bad'},
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
            {'ko': '나만 빼고 다 행복한 것만 같아', 'ro': 'Naman ppaego da haengbokhan geonman gata', 'zh': '好像除了我以外大家都很幸福'},
            {'ko': '우는 것보다 웃을 때가 더 아파', 'ro': 'Uneun geotboda useul ttaega deo apa', 'zh': '比起哭泣，笑的時候更痛苦'},
            {'ko': '마법의 주문이 널 위로할지도 몰라', 'ro': 'Mabeobui jumuni neol wirohaljido molla', 'zh': '魔法咒語說不定能安慰你'},
            {'ko': '도망갈까', 'ro': 'Domanggalkka', 'zh': '要逃跑嗎'},
            {'ko': 'Bibbidi babbidi boo', 'ro': 'Bibbidi babbidi boo', 'zh': 'Bibbidi babbidi boo'},
            {'ko': '우리 함께라면', 'ro': 'Uri hamkkeramyeon', 'zh': '如果是我們一起的話'},
            {'ko': '숨겨진 9와 4분의 3에', 'ro': 'Sumgyeojin guwa sabunui same', 'zh': '在隱藏的 9 又 3/4 月台'},
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
            {'ko': '거울 속에서 나를 멍하니 보는 넌', 'ro': 'Geoul sogeseo nareul meonghani boneun neon', 'zh': '鏡子裡呆呆看著我的你'},
            {'ko': '내가 아냐', 'ro': 'Naega anya', 'zh': '不是我'},
            {'ko': '머리에 뿔이 솟아', 'ro': 'Meorie ppuri sosa', 'zh': '頭上長出了角'},
            {'ko': '어떡해', 'ro': 'Eotteokhae', 'zh': '怎麼辦'},
            {'ko': '이 뿔이 너를 부르는 내 신호가 될 테니', 'ro': 'I ppuri neoreul bureuneun nae sinhoga doel teni', 'zh': '這隻角會成為呼喚你的信號'},
            {'ko': 'But I love it', 'ro': 'But I love it', 'zh': '但我喜歡它'},
            {'ko': '넌 내 왕관이 돼', 'ro': 'Neon nae wanggwani dwae', 'zh': '你變成了我的皇冠'},
            {'ko': '두근두근두근', 'ro': 'Dugeundugeundugeun', 'zh': '撲通撲通撲通'},
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
