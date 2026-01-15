import streamlit as st

# --- 設定網頁配置 ---
st.set_page_config(
    page_title="TXT 歌詞庫 (MOA Edition)",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 資料庫 (Data) ---

# 1. 專輯資訊
ALBUMS = {
    'sanctuary': { 'title': 'The Star Chapter: SANCTUARY', 'year': '2024', 'color': '#A5B4FC' },
    'tomorrow': { 'title': 'minisode 3: TOMORROW', 'year': '2024', 'color': '#FDBA74' },
    'freefall': { 'title': 'The Name Chapter: FREEFALL', 'year': '2023', 'color': '#818CF8' },
    'temptation': { 'title': 'The Name Chapter: TEMPTATION', 'year': '2023', 'color': '#34D399' },
    'thursday': { 'title': "minisode 2: Thursday's Child", 'year': '2022', 'color': '#F87171' },
    'fight_escape': { 'title': 'The Chaos Chapter: FIGHT OR ESCAPE', 'year': '2021', 'color': '#10B981' },
    'freeze': { 'title': 'The Chaos Chapter: FREEZE', 'year': '2021', 'color': '#60A5FA' },
    'blue_hour': { 'title': 'minisode1 : Blue Hour', 'year': '2020', 'color': '#F472B6' },
    'eternity': { 'title': 'The Dream Chapter: ETERNITY', 'year': '2020', 'color': '#A78BFA' },
    'magic': { 'title': 'The Dream Chapter: MAGIC', 'year': '2019', 'color': '#2DD4BF' },
    'star': { 'title': 'The Dream Chapter: STAR', 'year': '2019', 'color': '#FCD34D' }
}

# 輔助函式：建立 B-side 歌曲範本
def create_placeholder_lyrics():
    return [
        {'ko': '가사가 준비 중입니다.', 'ro': 'Gasaga junbi jungimnida.', 'zh': '(歌詞資料庫擴充中...)'},
        {'ko': '곧 업데이트 될 예정입니다.', 'ro': 'Got eopdeiteu doel yejeongimnida.', 'zh': '即將更新完整歌詞'},
    ]

# 2. 歌曲資料庫 (主打歌全歌詞 + B-side 列表)
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
            {'ko': '내 세상은 너로 가득 차', 'ro': 'Nae sesangeun neoro gadeuk cha', 'zh': '我的世界充滿了你'},
            {'ko': 'So let me love you', 'ro': 'So let me love you', 'zh': '所以讓我愛你'},
            {'ko': 'Over the moon', 'ro': 'Over the moon', 'zh': 'Over the moon'},
            {'ko': '반짝이는 우리 둘만의 frame', 'ro': 'Banjjagineun uri dulmanui frame', 'zh': '閃耀著只屬於我們兩人的 frame'},
            {'ko': '영원히 널 사랑해', 'ro': 'Yeongwonhi neol saranghae', 'zh': '永遠愛你'},
        ]
    },
    {'id': 'heaven', 'album_id': 'sanctuary', 'title': 'Heaven', 'korean_title': 'Heaven', 'lyrics': create_placeholder_lyrics()},
    {'id': 'danger', 'album_id': 'sanctuary', 'title': 'Danger', 'korean_title': 'Danger', 'lyrics': create_placeholder_lyrics()},
    
    # --- minisode 3: TOMORROW ---
    {
        'id': 'deja_vu', 'album_id': 'tomorrow', 'title': 'Deja Vu', 'korean_title': 'Deja Vu',
        'lyrics': [
            {'ko': '폐허 속의 모르스부호', 'ro': 'Pyeheo sogui moreuseubuho', 'zh': '廢墟中的摩斯密碼'},
            {'ko': '머릿속을 맴도는 얼굴', 'ro': 'Meoritsogeul maemdoneun eolgul', 'zh': '腦海中盤旋的那張臉'},
            {'ko': '약속을 너만은 기억할 테니', 'ro': 'Yaksogeul neomaneun gieokhal teni', 'zh': '因為只有你會記得那個約定'},
            {'ko': '나의 미래는 너야', 'ro': 'Naui miraeneun neoya', 'zh': '我的未來就是你'},
            {'ko': 'Say my name', 'ro': 'Say my name', 'zh': '呼喚我的名字'},
            {'ko': '마치 데자뷔', 'ro': 'Machi dejabwi', 'zh': '就像既視感 (Deja Vu)'},
            {'ko': '도망쳐 봐도 결국엔 너야', 'ro': 'Domangchyeo bwado gyeolgugen neoya', 'zh': '就算逃跑 結局依然是你'},
            {'ko': '비극의 오르페우스', 'ro': 'Bigeugui oreupeuseu', 'zh': '悲劇的奧菲斯'},
            {'ko': 'I promise you', 'ro': 'I promise you', 'zh': '我向你保證'},
            {'ko': '몇 번을 반복해도', 'ro': 'Myeot beoneul banbokhaedo', 'zh': '無論重複多少次'},
            {'ko': '나의 미래는 너야', 'ro': 'Naui miraeneun neoya', 'zh': '我的未來就是你'},
        ]
    },
    {'id': 'ill_see_you', 'album_id': 'tomorrow', 'title': "I'll See You There Tomorrow", 'korean_title': '내일에서 기다릴게', 'lyrics': create_placeholder_lyrics()},

    # --- The Name Chapter: FREEFALL ---
    {
        'id': 'chasing_feeling', 'album_id': 'freefall', 'title': 'Chasing That Feeling', 'korean_title': 'Chasing That Feeling',
        'lyrics': [
            {'ko': 'Heaven is hiding empty-handed', 'ro': 'Heaven is hiding empty-handed', 'zh': '天堂空手躲藏著'},
            {'ko': '탄 곳이 없는 shooting star', 'ro': 'Tan gosi eomneun shooting star', 'zh': '沒有燃燒殆盡的流星'},
            {'ko': '내일도 난 제자리야', 'ro': 'Naeildo nan jejariya', 'zh': '明天我也會在原地'},
            {'ko': '달콤한 신기루는 굿바이', 'ro': 'Dalkomhan singiruneun gutbai', 'zh': '與甜蜜的海市蜃樓說再見'},
            {'ko': 'I\'m chasing that feeling', 'ro': 'I\'m chasing that feeling', 'zh': '我在追逐那種感覺'},
            {'ko': '망가진 나라도 괜찮아', 'ro': 'Manggajin narado gwaenchana', 'zh': '即使壞掉的我也可以'},
            {'ko': '죽어 가던 나의 아픔까지', 'ro': 'Jugeo gadeon naui apeumkkaji', 'zh': '連同我漸漸死去的痛苦'},
            {'ko': '사랑할래 chasing that feeling', 'ro': 'Saranghallae chasing that feeling', 'zh': '我要去愛 chasing that feeling'},
            {'ko': 'And I won\'t stop', 'ro': 'And I won\'t stop', 'zh': '我不會停止'},
            {'ko': 'Chasing that feeling', 'ro': 'Chasing that feeling', 'zh': '追逐那種感覺'},
        ]
    },
    {'id': 'back_for_more', 'album_id': 'freefall', 'title': 'Back for More (TXT Ver.)', 'korean_title': 'Back for More', 'lyrics': create_placeholder_lyrics()},

    # --- The Name Chapter: TEMPTATION ---
    {
        'id': 'sugar_rush_ride', 'album_id': 'temptation', 'title': 'Sugar Rush Ride', 'korean_title': 'Sugar Rush Ride',
        'lyrics': [
            {'ko': '생각은 멈춰', 'ro': 'Saenggageun meomchwo', 'zh': '停止思考'},
            {'ko': '직감만 남겨', 'ro': 'Jikgamman namgyeo', 'zh': '只留下直覺'},
            {'ko': '거부할 수 없는 이 이끌림', 'ro': 'Geobuhal su eomneun i ikkeullim', 'zh': '這無法抗拒的吸引力'},
            {'ko': '달콤함 그 틈으로 데려가', 'ro': 'Dalkomham geu teumeuro deryeoga', 'zh': '帶我到那甜蜜的縫隙中'},
            {'ko': 'Gimme gimme more', 'ro': 'Gimme gimme more', 'zh': '給我更多 給我更多'},
            {'ko': 'Gimme gimme more', 'ro': 'Gimme gimme more', 'zh': '給我更多 給我更多'},
            {'ko': 'Sugar rush-ush', 'ro': 'Sugar rush-ush', 'zh': '糖分衝擊'},
            {'ko': 'Sugar rush-ush', 'ro': 'Sugar rush-ush', 'zh': '糖分衝擊'},
            {'ko': '나쁜 넌 liar', 'ro': 'Nappeun neon liar', 'zh': '壞壞的你是 liar'},
            {'ko': '내게 너 뭘 한 거야', 'ro': 'Naege neo mwol han geoya', 'zh': '你對我做了什麼'},
            {'ko': 'Come a little closer', 'ro': 'Come a little closer', 'zh': '再靠近一點'},
            {'ko': '넌 속삭여 "삼켜버려"', 'ro': 'Neon soksagyeo "samkyeobeoryeo"', 'zh': '你低語著「吞下去吧」'},
            {'ko': 'Sugar rush-ush', 'ro': 'Sugar rush-ush', 'zh': '糖分衝擊'},
        ]
    },

    # --- minisode 2: Thursday's Child ---
    {
        'id': 'gbgb', 'album_id': 'thursday', 'title': 'Good Boy Gone Bad', 'korean_title': 'Good Boy Gone Bad',
        'lyrics': [
            {'ko': '영원이란 말은 모래성', 'ro': 'Yeongwoniran mareun moraeseong', 'zh': '永遠這個詞就像沙堡'},
            {'ko': '부드러운 파도 앞에 무너져', 'ro': 'Budeureoun pado ape muneojyeo', 'zh': '在溫柔的海浪面前倒塌'},
            {'ko': 'Every day, every night', 'ro': 'Every day, every night', 'zh': '日日夜夜'},
            {'ko': '사랑이란 놈의 지독한 장난', 'ro': 'Sarangiran nomui jidokhan jangnan', 'zh': '愛情這傢伙的殘忍惡作劇'},
            {'ko': 'Good boy gone bad', 'ro': 'Good boy gone bad', 'zh': '好男孩變壞了'},
            {'ko': '다 내던져 난', 'ro': 'Da naedeonjyeo nan', 'zh': '我全部拋棄'},
            {'ko': 'Good boy gone bad', 'ro': 'Good boy gone bad', 'zh': '好男孩變壞了'},
            {'ko': '네가 했던 날', 'ro': 'Nega haetdeon nal', 'zh': '你曾愛過的我'},
            {'ko': '가슴팍엔 흉터', 'ro': 'Gaseumpagen hyungteo', 'zh': '胸口的傷疤'},
            {'ko': 'Gone dead', 'ro': 'Gone dead', 'zh': 'Gone dead'},
            {'ko': '난 날 쐈어 bang bang', 'ro': 'Nan nal swasseo bang bang', 'zh': '我對自己開了槍 bang bang'},
            {'ko': '더 삐뚤어져 난', 'ro': 'Deo ppittureojyeo nan', 'zh': '我變得更加扭曲'},
        ]
    },

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
            {'ko': '기꺼이 sinking', 'ro': 'Gikkeoi sinking', 'zh': '心甘情願 sinking'},
            {'ko': '너를 그리는 shining', 'ro': 'Neoreul geurineun shining', 'zh': '描繪著你的 shining'},
            {'ko': 'I\'m a loser', 'ro': 'I\'m a loser', 'zh': '我是個失敗者'},
            {'ko': 'Crying, crying, crying', 'ro': 'Crying, crying, crying', 'zh': 'Crying, crying, crying'},
            {'ko': '이젠 널 잊겠단 lie', 'ro': 'Ijen neol itgetdan lie', 'zh': '現在說要忘記你是 lie'},
            {'ko': 'Run, run, run', 'ro': 'Run, run, run', 'zh': 'Run, run, run'},
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
            {'ko': '구멍 난 영혼에 살이 돋아', 'ro': 'Gumeong nan yeonghone sari doda', 'zh': '破洞的靈魂長出了新肉'},
            {'ko': '얼어붙은 지구 위', 'ro': 'Eoreobuteun jigu wi', 'zh': '在冰凍的地球上'},
            {'ko': 'Say you love me', 'ro': 'Say you love me', 'zh': '說你愛我'},
            {'ko': '세상의 끝까지', 'ro': 'Sesangui kkeutkkaji', 'zh': '直到世界的盡頭'},
            {'ko': 'All or nothing', 'ro': 'All or nothing', 'zh': 'All or nothing'},
            {'ko': 'I give it all to you', 'ro': 'I give it all to you', 'zh': '我把一切都給你'},
            {'ko': 'I know I love you', 'ro': 'I know I love you', 'zh': '我知道我愛你'},
        ]
    },

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
            {'ko': '너는 나의 special', 'ro': 'Neoneun naui special', 'zh': '你是我的 special'},
            {'ko': '하나뿐인 내 special', 'ro': 'Hanappunin nae special', 'zh': '唯一的我的 special'},
            {'ko': '꿈의 문이 열리고', 'ro': 'Kkumui muni yeolligo', 'zh': '夢想之門開啟'},
            {'ko': '추억 속의 널 부르고', 'ro': 'Chueok sogui neol bureugo', 'zh': '呼喚記憶中的你'},
            {'ko': '멈춰버린 시간', 'ro': 'Meomchwobeorin sigan', 'zh': '停滯的時間'},
            {'ko': '경계선 그 사이로', 'ro': 'Gyeonggyeseon geu sairo', 'zh': '在分界線之間'},
            {'ko': '돌아서고 싶지 않아', 'ro': 'Doraseogo sipji ana', 'zh': '不想轉身離去'},
        ]
    },

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
            {'ko': '내 영원의 약속은', 'ro': 'Nae yeongwonui yaksogeun', 'zh': '我永遠的約定'},
            {'ko': '모래성처럼 무너져', 'ro': 'Moraeseongcheoreom muneojyeo', 'zh': '像沙堡一樣崩塌'},
            {'ko': 'Who\'s a liar', 'ro': 'Who\'s a liar', 'zh': 'Who\'s a liar'},
            {'ko': '불타버린 밤', 'ro': 'Bultabeorin bam', 'zh': '燃燒殆盡的夜晚'},
            {'ko': 'Together, together', 'ro': 'Together, together', 'zh': 'Together, together'},
            {'ko': 'We are forever, forever', 'ro': 'We are forever, forever', 'zh': 'We are forever, forever'},
            {'ko': 'You know', 'ro': 'You know', 'zh': 'You know'},
        ]
    },

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
            {'ko': '함께해줘', 'ro': 'Hamkkehaejwo', 'zh': '請跟我在一起'},
            {'ko': '캄캄한 밤의 계단', 'ro': 'Kamkamhan bamui gyedan', 'zh': '漆黑夜晚的樓梯'},
            {'ko': '마법의 기차를 타', 'ro': 'Mabeobui gichareul ta', 'zh': '搭上魔法列車'},
            {'ko': '내 영원이 돼줘', 'ro': 'Nae yeongwoni dwaejwo', 'zh': '成為我的永遠吧'},
            {'ko': '내 이름을 불러줘', 'ro': 'Nae ireumeul bulleojwo', 'zh': '請呼喚我的名字'},
            {'ko': 'Run away, run away', 'ro': 'Run away, run away', 'zh': 'Run away, run away'},
        ]
    },

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
            {'ko': '세상은 대체 왜 이래', 'ro': 'Sesangeun daeche wae irae', 'zh': '這世界到底是怎麼了'},
            {'ko': '구해줘', 'ro': 'Guhaejwo', 'zh': '救救我'},
            {'ko': '사실은 아직도 난', 'ro': 'Sasireun ajikdo nan', 'zh': '其實我依然'},
            {'ko': '조금 불안해', 'ro': 'Jogeum buranhae', 'zh': '有點不安'},
            {'ko': 'Who you?', 'ro': 'Who you?', 'zh': 'Who you?'},
            {'ko': 'I\'m a boy with a horn', 'ro': 'I\'m a boy with a horn', 'zh': '我是個長著角的男孩'},
        ]
    },
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
    
    # 專輯封面與標題區
    st.markdown(f"""
    <div style="text-align: center; padding: 20px; background: linear-gradient(to bottom, {album['color']}22, white); border-radius: 20px;">
        <h1 style='margin-bottom: 0;'>{song['title']}</h1>
        <h3 style='color: #666; margin-top: 5px;'>{song['korean_title']}</h3>
        <p style='color: gray; font-size: 0.9em;'>{album['title']} ({album['year']})</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("") 

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
        
        st.write("") 
    
    if song['lyrics'][0]['ko'] == '가사가 준비 중입니다.':
        st.info("💡 提示：非主打歌(B-side) 的完整歌詞將陸續更新，目前僅提供主打歌全曲。")

# 3. 首頁 (專輯牆與列表)
else:
    st.title("Hello, MOA! ✨")
    st.write("請選擇專輯瀏覽歌曲：")
    
    album_ids = list(ALBUMS.keys())
    
    tab_new, tab_all = st.tabs(["最新發行 (Latest)", "所有專輯 (All Albums)"])
    
    with tab_new:
        # 顯示最新的 3 張專輯
        latest_albums = album_ids[:3]
        for aid in latest_albums:
            album = ALBUMS[aid]
            with st.expander(f"{album['year']} | {album['title']}", expanded=True):
                st.markdown(f"""<div style="height: 5px; background: {album['color']}; border-radius: 5px; margin-bottom: 10px;"></div>""", unsafe_allow_html=True)
                album_songs = [s for s in SONGS if s['album_id'] == aid]
                for song in album_songs:
                    if st.button(f"🎵 {song['title']}", key=f"new_{song['id']}"):
                        go_to_song(song)
                        st.rerun()

    with tab_all:
        # 顯示所有專輯
        selected_album_id = st.selectbox("選擇專輯:", options=album_ids, format_func=lambda x: ALBUMS[x]['title'])
        
        if selected_album_id:
            album = ALBUMS[selected_album_id]
            st.markdown(f"""
                <div class="album-card" style="background: linear-gradient(135deg, {album['color']}, #888);">
                    <h2>{album['title']}</h2>
                    <p>{album['year']}</p>
                </div>
                """, unsafe_allow_html=True)
            
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
