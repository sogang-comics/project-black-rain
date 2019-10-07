define TrueEnding = 0 #트루엔딩 포인트
define BadEnding = 0 #배드엔딩 포인트

transform right:
    xalign 0.95
    yalign 1.0

transform left:
    xalign 0.05
    yalign 1.0

transform slightleft:
    xalign 0.30
    yalign 1.0

transform slightright:
    xalign 0.75
    yalign 1.0

transform moveright:
    linear 0.5 xalign 0.95

transform movecenter:
    linear 0.5 xalign 0.5

transform moveslightright:
    linear 0.5 xalign 0.75

transform moveleft:
    linear 0.5 xalign 0.05

transform moveslightleft:
    linear 0.5 xalign 0.3

define yeongwon = Character('영원', image="yeongwon", color="#c8ffc8", show_two_window = True)
define haneul = Character('하늘', image="haneul", color="#c8ffc8", show_two_window = True)
define hanbyeol = Character('한별', image="hanbyeol", color="#c8ffc8", show_two_window = True)
define hanseol = Character('한설', image="hanseol", color="#c8ffc8", show_two_window = True)
define yeonwoo = Character('연우', image="yeonwoo", color="#c8ffc8", show_two_window = True)
define principal = Character('원장', image="principal", color="#c8ffc8", show_two_window = True)
define overwatch = Character('감시자', image="overwatch", color="#c8ffc8", show_two_window = True)
define keibi = Character('경비원', color="#c8ffc8", show_two_window = True)
define teacher = Character('선생님', image="teacher", color="#c8ffc8", show_two_window = True)
define mstudent = Character('남학생', color="#c8ffc8", show_two_window = True)
define fstudent = Character('여학생', color="#c8ffc8", show_two_window = True)
define haneul2 = Character('??', color="#c8ffc8", show_two_window = True)
define shonen = Character('소년', color="#c8ffc8", show_two_window = True)
define shojo = Character('소녀', color="#c8ffc8", show_two_window = True)

image fstudent idle = "extra/fstudent.png"
image keibi idle = "extra/keibi.png"
image mstudent idle = "extra/mstudent.png"
image teacher idle = "extra/teacher.png"

image hanbyeol fury = "hanbyeol/fury.png"
image hanbyeol fury2 = "hanbyeol/fury2.png"
image hanbyeol happy = "hanbyeol/happy.png"
image hanbyeol happy2 = "hanbyeol/happy2.png"
image hanbyeol idle = "hanbyeol/idle.png"
image hanbyeol idle2 = "hanbyeol/idle2.png"
image hanbyeol sad = "hanbyeol/sad.png"
image hanbyeol sad2 = "hanbyeol/sad2.png"
image hanbyeol serious = "hanbyeol/serious.png"
image hanbyeol serious2 = "hanbyeol/serious2.png"
image hanbyeol shock = "hanbyeol/shock.png"
image hanbyeol shock2 = "hanbyeol/shock2.png"

image haneul fury = "haneul/fury.png"
image haneul happy = "haneul/happy.png"
image haneul happy2 = "haneul/happy2.png"
image haneul idle = "haneul/idle.png"
image haneul sad = "haneul/sad.png"
image haneul serious = "haneul/serious.png"
image haneul shock = "haneul/shock.png"

image haneullong fury = "haneullong/fury.png"
image haneullong happy = "haneullong/happy.png"
image haneullong happy2 = "haneullong/happy2.png"
image haneullong idle = "haneullong/idle.png"
image haneullong sad = "haneullong/sad.png"
image haneullong serious = "haneullong/serious.png"
image haneullong shock = "haneullong/shock.png"

image hanseol happy = "hanseol/happy.png"
image hanseol happy2 = "hanseol/happy2.png"
image hanseol idle = "hanseol/idle.png"
image hanseol idle2 = "hanseol/idle2.png"
image hanseol sad = "hanseol/sad.png"
image hanseol sad2 = "hanseol/sad2.png"
image hanseol shock = "hanseol/shock.png"
image hanseol shock2 = "hanseol/shock2.png"

image overwatch devil = "overwatch/devil.png"
image overwatch fury = "overwatch/fury.png"
image overwatch idle = "overwatch/idle.png"
image overwatch idle2 = "overwatch/idle2.png"

image principal cry = "principal/cry.png"
image principal cry2 = "principal/cry2.png"
image principal happy = "principal/happy.png"
image principal happy2 = "principal/happy2.png"
image principal idle = "principal/idle.png"
image principal idle2 = "principal/idle2.png"
image principal sad = "principal/sad.png"
image principal sad2 = "principal/sad2.png"
image principal sentimental = "principal/sentimental.png"
image principal sentimental2 = "principal/sentimental2.png"
image principal shock = "principal/shock.png"
image principal shock2 = "principal/shock2.png"

image principalglass happy = "principalglass/happy.png"
image principalglass happy2 = "principalglass/happy2.png"
image principalglass idle = "principalglass/idle.png"
image principalglass idle2 =  "principalglass/idle2.png"

image yeonwoo happy = "yeonwoo/happy.png"
image yeonwoo happy2 = "yeonwoo/happy2.png"
image yeonwoo idle = "yeonwoo/idle.png"
image yeonwoo idle2 = "yeonwoo/idle2.png"

image yeongwon blush = "yeongwon/blush.png"
image yeongwon blush2 = "yeongwon/blush2.png"
image yeongwon fury = "yeongwon/fury.png"
image yeongwon fury2 = "yeongwon/fury2.png"
image yeongwon happy = "yeongwon/happy.png"
image yeongwon happy2 = "yeongwon/happy2.png"
image yeongwon idle = "yeongwon/idle.png"
image yeongwon idle2 = "yeongwon/idle2.png"
image yeongwon sad = "yeongwon/sad.png"
image yeongwon sad2 = "yeongwon/sad2.png"
image yeongwon serious = "yeongwon/serious.png"
image yeongwon serious2 = "yeongwon/serious2.png"
image yeongwon shock = "yeongwon/shock.png"
image yeongwon shock2 = "yeongwon/shock2.png"

#brightness adjust
image fstudent idleb = im.MatrixColor("extra/fstudent.png",im.matrix.brightness(-0.2))
image keibi idleb = im.MatrixColor("extra/keibi.png",im.matrix.brightness(-0.2))
image mstudent idleb = im.MatrixColor("extra/mstudent.png",im.matrix.brightness(-0.2))
image teacher idleb = im.MatrixColor("extra/teacher.png",im.matrix.brightness(-0.2))
image hanbyeol furyb = im.MatrixColor("hanbyeol/fury.png",im.matrix.brightness(-0.2))
image hanbyeol fury2b = im.MatrixColor("hanbyeol/fury2.png",im.matrix.brightness(-0.2))
image hanbyeol happyb = im.MatrixColor("hanbyeol/happy.png",im.matrix.brightness(-0.2))
image hanbyeol happy2b = im.MatrixColor("hanbyeol/happy2.png",im.matrix.brightness(-0.2))
image hanbyeol idleb = im.MatrixColor("hanbyeol/idle.png",im.matrix.brightness(-0.2))
image hanbyeol idle2b = im.MatrixColor("hanbyeol/idle2.png",im.matrix.brightness(-0.2))
image hanbyeol sadb = im.MatrixColor("hanbyeol/sad.png",im.matrix.brightness(-0.2))
image hanbyeol sad2b = im.MatrixColor("hanbyeol/sad2.png",im.matrix.brightness(-0.2))
image hanbyeol seriousb = im.MatrixColor("hanbyeol/serious.png",im.matrix.brightness(-0.2))
image hanbyeol serious2b = im.MatrixColor("hanbyeol/serious2.png",im.matrix.brightness(-0.2))
image hanbyeol shockb = im.MatrixColor("hanbyeol/shock.png",im.matrix.brightness(-0.2))
image hanbyeol shock2b = im.MatrixColor("hanbyeol/shock2.png",im.matrix.brightness(-0.2))
image haneul furyb = im.MatrixColor("haneul/fury.png",im.matrix.brightness(-0.2))
image haneul happyb = im.MatrixColor("haneul/happy.png",im.matrix.brightness(-0.2))
image haneul happy2b = im.MatrixColor("haneul/happy2.png",im.matrix.brightness(-0.2))
image haneul idleb = im.MatrixColor("haneul/idle.png",im.matrix.brightness(-0.2))
image haneul sadb = im.MatrixColor("haneul/sad.png",im.matrix.brightness(-0.2))
image haneul seriousb = im.MatrixColor("haneul/serious.png",im.matrix.brightness(-0.2))
image haneul shockb = im.MatrixColor("haneul/shock.png",im.matrix.brightness(-0.2))
image haneullong furyb = im.MatrixColor("haneullong/fury.png",im.matrix.brightness(-0.2))
image haneullong happyb = im.MatrixColor("haneullong/happy.png",im.matrix.brightness(-0.2))
image haneullong happy2b = im.MatrixColor("haneullong/happy2.png",im.matrix.brightness(-0.2))
image haneullong idleb = im.MatrixColor("haneullong/idle.png",im.matrix.brightness(-0.2))
image haneullong sadb = im.MatrixColor("haneullong/sad.png",im.matrix.brightness(-0.2))
image haneullong seriousb = im.MatrixColor("haneullong/serious.png",im.matrix.brightness(-0.2))
image haneullong shockb = im.MatrixColor("haneullong/shock.png",im.matrix.brightness(-0.2))
image hanseol happyb = im.MatrixColor("hanseol/happy.png",im.matrix.brightness(-0.2))
image hanseol happy2b = im.MatrixColor("hanseol/happy2.png",im.matrix.brightness(-0.2))
image hanseol idleb = im.MatrixColor("hanseol/idle.png",im.matrix.brightness(-0.2))
image hanseol idle2b = im.MatrixColor("hanseol/idle2.png",im.matrix.brightness(-0.2))
image hanseol sadb = im.MatrixColor("hanseol/sad.png",im.matrix.brightness(-0.2))
image hanseol sad2b = im.MatrixColor("hanseol/sad2.png",im.matrix.brightness(-0.2))
image hanseol shockb = im.MatrixColor("hanseol/shock.png",im.matrix.brightness(-0.2))
image hanseol shock2b = im.MatrixColor("hanseol/shock2.png",im.matrix.brightness(-0.2))
image overwatch devilb = im.MatrixColor("overwatch/devil.png",im.matrix.brightness(-0.2))
image overwatch furyb = im.MatrixColor("overwatch/fury.png",im.matrix.brightness(-0.2))
image overwatch idleb = im.MatrixColor("overwatch/idle.png",im.matrix.brightness(-0.2))
image overwatch idle2b = im.MatrixColor("overwatch/idle2.png",im.matrix.brightness(-0.2))
image principal cryb = im.MatrixColor("principal/cry.png",im.matrix.brightness(-0.2))
image principal cry2b = im.MatrixColor("principal/cry2.png",im.matrix.brightness(-0.2))
image principal happyb = im.MatrixColor("principal/happy.png",im.matrix.brightness(-0.2))
image principal happy2b = im.MatrixColor("principal/happy2.png",im.matrix.brightness(-0.2))
image principal idleb = im.MatrixColor("principal/idle.png",im.matrix.brightness(-0.2))
image principal idle2b = im.MatrixColor("principal/idle2.png",im.matrix.brightness(-0.2))
image principal sadb = im.MatrixColor("principal/sad.png",im.matrix.brightness(-0.2))
image principal sad2b = im.MatrixColor("principal/sad2.png",im.matrix.brightness(-0.2))
image principal sentimentalb = im.MatrixColor("principal/sentimental.png",im.matrix.brightness(-0.2))
image principal sentimental2b = im.MatrixColor("principal/sentimental2.png",im.matrix.brightness(-0.2))
image principal shockb = im.MatrixColor("principal/shock.png",im.matrix.brightness(-0.2))
image principal shock2b = im.MatrixColor("principal/shock2.png",im.matrix.brightness(-0.2))
image principalglass happyb = im.MatrixColor("principalglass/happy.png",im.matrix.brightness(-0.2))
image principalglass happy2b = im.MatrixColor("principalglass/happy2.png",im.matrix.brightness(-0.2))
image principalglass idleb = im.MatrixColor("principalglass/idle.png",im.matrix.brightness(-0.2))
image principalglass idle2b = im.MatrixColor("principalglass/idle2.png",im.matrix.brightness(-0.2))
image yeonwoo happyb = im.MatrixColor("yeonwoo/happy.png",im.matrix.brightness(-0.2))
image yeonwoo happy2b = im.MatrixColor("yeonwoo/happy2.png",im.matrix.brightness(-0.2))
image yeonwoo idleb = im.MatrixColor("yeonwoo/idle.png",im.matrix.brightness(-0.2))
image yeonwoo idle2b = im.MatrixColor("yeonwoo/idle2.png",im.matrix.brightness(-0.2))
image yeongwon blushb = im.MatrixColor("yeongwon/blush.png",im.matrix.brightness(-0.2))
image yeongwon blush2b = im.MatrixColor("yeongwon/blush2.png",im.matrix.brightness(-0.2))
image yeongwon furyb = im.MatrixColor("yeongwon/fury.png",im.matrix.brightness(-0.2))
image yeongwon fury2b = im.MatrixColor("yeongwon/fury2.png",im.matrix.brightness(-0.2))
image yeongwon happyb = im.MatrixColor("yeongwon/happy.png",im.matrix.brightness(-0.2))
image yeongwon happy2b = im.MatrixColor("yeongwon/happy2.png",im.matrix.brightness(-0.2))
image yeongwon idleb = im.MatrixColor("yeongwon/idle.png",im.matrix.brightness(-0.2))
image yeongwon idle2b = im.MatrixColor("yeongwon/idle2.png",im.matrix.brightness(-0.2))
image yeongwon sadb = im.MatrixColor("yeongwon/sad.png",im.matrix.brightness(-0.2))
image yeongwon sad2b = im.MatrixColor("yeongwon/sad2.png",im.matrix.brightness(-0.2))
image yeongwon seriousb = im.MatrixColor("yeongwon/serious.png",im.matrix.brightness(-0.2))
image yeongwon serious2b = im.MatrixColor("yeongwon/serious2.png",im.matrix.brightness(-0.2))
image yeongwon shockb = im.MatrixColor("yeongwon/shock.png",im.matrix.brightness(-0.2))
image yeongwon shock2b = im.MatrixColor("yeongwon/shock2.png",im.matrix.brightness(-0.2))

#bg
image bg classroom = "background/classroom.jpg"
image bg hallway = "background/hallway.jpg"
image bg hideout = "background/hideout.jpg"
image bg lab = "background/lab.jpg"
image bg oldschool = "background/oldschool.jpg"
image bg school = "background/school.jpg"
image bg sky = "background/sky.jpg"
image bg stairs = "background/stairs.jpg"
image bg what = "background/what.jpg"
image bg what2 = "background/what2.jpg"

image bg classroomb = im.MatrixColor("background/classroom.jpg",im.matrix.brightness(-0.2))
image bg hallwayb = im.MatrixColor("background/hallway.jpg",im.matrix.brightness(-0.2))
image bg hideoutb = im.MatrixColor("background/hideout.jpg",im.matrix.brightness(-0.2))
image bg labb = im.MatrixColor("background/lab.jpg",im.matrix.brightness(-0.2))
image bg schoolb = im.MatrixColor("background/school.jpg",im.matrix.brightness(-0.2))
image bg oldschoolb = im.MatrixColor("background/oldschool.jpg",im.matrix.brightness(-0.2))
image bg skyb = im.MatrixColor("background/sky.jpg",im.matrix.brightness(-0.2))
image bg stairsb = im.MatrixColor("background/stairs.jpg",im.matrix.brightness(-0.2))
image bg whatb = im.MatrixColor("background/what.jpg",im.matrix.brightness(-0.2))

#ecg

#start
label scene300: 
    # play music "music/sentimental.mp3" fadeout 1
    scene bg blackscreen with Dissolve(1.0)
    "한설이가 사라졌다. "
    "만나자던 시간이 훌쩍 넘었는데도 나타날 기색을 보이지 않았다."
    "초조한 마음을 진정시키기에는 너무 큰 일이였다."
    "당장이라도 장난스럽게 웃으며 어디에 다녀왔냐고 하는 모습이 눈에 어른거리는 것은 왜일까."
    "하지만 한설이는 여기에 없다. 내 상상일 뿐이다. "
    scene bg classroom with Dissolve(1.0)
    "더욱더 이상한 것은 다른 애들의 태도였다."
    "그 넉살 좋던 한설이가 사라진 것에 대해서 아무도 걱정을 하지 않았다."
    "무드 메이커는 분위기의 흐름을 바꾸어 놓는 힘이 있다. "
    "하지만 무언가 더욱 거대한 힘이 그 흐름을 제자리로 돌려놓고 있다."
    "한설이는 잠시 어딘가로 떠나서, 조금 지나서 돌아온다고 한다."
    "뻔한 거짓말이다. "
    "무언가가 일어났다. "
    "누군가가 움직이고 있다. "
    scene bg hallway with Dissolve(1.0)
    hanbyeol"지금 거기로 올라가면 너까지 위험해지는 거 알고 움직이는 거야?"
        show hanbyeol fury with dissolve
    "지금 당장 최상층으로 달려가려는 나를 붙잡은 것은 다름아닌 한별이였다."
    "눈 하나 깜짝하지 않고 가로막는 한별이를 보고 내가 가장 먼저 느낀 감정은 분노였다."
    yeongwon idle"그럼 어떻게 할 거야! 딴 애도 아니고 너 동생이라고, 정신차려!"
    "막무가내로 뛰어나가려 했지만, 한별이의 확고한 의지를 보고 나서야 진정할 수 있었다."
    hanbyeol idle2"일단 내일.. 다시 물어보는거야.. 아무도 모르도록...응?"
    "한별이의 눈동자는 흔들리고 있었지만 내가 여기서 더 나선다면 한별이를 더욱 불안하게 할 뿐이다."
    "자신의 동생이 없어졌음에도 그렇게 태연하게 나를 막아설 수 있었던 것은-"
    "단언컨대 슬픔과 분노를 짓이기고 태어난 용기가 아닐까."

label scene301: 
    scene bg room with Dissolve(1.0)
    "초점없는 눈으로 무채색의 천장을 바라보며 수 시간, "
    "시간이 흘러가는 것을 인지하지 못한 채, 오늘의 회의 역시 아무런 성과가 없다. "
    "주인을 잃은 한설이의 기숙사에는 적막함만이 감돌았다. "
    "나와 한별이의 무거운 공기는 정적인 분위기를 더욱 심화시킬 뿐. "
    "절망을 이겨내려고 하는 우리들에 손에 남겨진 것은 오직 옛 건물에서 얻은 몇몇 실험 보고서들이다."
    "낡은 종이 조각으로부터 시작된 호기심의 댓가는 너무나 큰 것이였다. "
    "수수께끼의 길잡이가 무언가를 알려주지 않을까, 라고 생각한 내가 바보 같이 느껴졌다. "
    yeongwon"우리 선생님이 무언가를 숨기고 있는게 확실해."
        show hanbyeol sad with dissolve
    hanbyeol"또 그 이야기야? "
    "솔직히 아무것도 모르겠지만, 최대한 가능성을 열어보는 것이 어떨까. "
    hanbyeol idle"기억해봐, 원장이 위층으로 올라갔을 때, 우리 선생은 수업 중이였어. "
    hanbyeol"거의 불가능한 전제라고. 거의.."
    scene bg roomb with Dissolve(1.0)
    "한별이의 목소리는 처음과는 다르게 약간 떨리고 있었다."
    "억지로 합리적 사고를 잃지 않으려는 그 모습에, 다시 한 번 마음을 다잡는다. "
    scene bg room with Dissolve(1.0)
    yeongwon idle "그럼 이 부분을..다시 한번 보자."
    "실험 보고서 3번, 제 14페이지..."
    "우리들에게 가장 많은 답을 주었던 증거들을 다시 한 번 훑어내려간다. "
    "과연 이 정체불명의 실험들은 어떤 과정을 거쳐 이런 결말로 마무리된 것일까. "
    "실험의 인과관계, 증명 절차, 결과..."
    "그리고 사람들의 행방. "
    "분명 한설이는 빛이 들지 않는 저편에서 우리를 기다리고 있겠지."
    with fade (1.0 color="#000000")

label scene302: 
    scene bg hallwaydorm with Dissolve(1.0)
    "한별이의 방에서 빠져나오니 이미 시간은 한참 늦어져 있었다. "
    "몇 번의 제자리걸음을 거쳐 추론을 세웠어도 아직은 불완전할 뿐이였다. "
    "터덜터덜한 발걸음이 무거워진다. "
    "오늘따라 낡은 복도가 더욱 칠흑같이 어두워 보이는 것은 기분 탓일까. "
    "여러가지 생각이 겹쳐 쓸데 없는 걱정이 늘어난다. "
    "경비원이 수상하게 여겨 잡아가지 않을까. "
    "누군가가 나를 보고 있지는 않을까. "
    "내 방으로 가는 길은 더 멀게 느껴진다. "
    "그 순간. "
    yeongwon shock"꺄아-- "
    "목 끝까지 올라온 비명을 삼킨다. "
    "누군가의 인기척이 빠르게 나타났다. "
    haneul2"쉿, 조용히 해"
    "쓸데 없는 걱정이라고 생각했던 내가 잘못이다. "
    "공포에 사로잡혀 제대로 말도 나오지 않는다. "
    haneul2"...왜 그래?"
    "..응?"
    "어디선가 많이 들어본 목소리였다. "
    "여린 실루엣이, 복도 끝의 창문 앞에 앉아 있었다. "
    "얘가 여기 있으면 안되는데,"
    scene bg jeon1 with Dissolve(1.0)
    "하늘이였다. "
    "복도의 엷은 달빛이 그의 은빛 머리칼을 반사시켰다. "
    "아아. 하늘이구나. "
    "까무러칠 정도로 놀라운 방문이였다. "
    "공포감은 이내 누그러져 안도감으로 바뀌었다. "
    "그러나 내가 하늘이를 보고 느낀 첫 번째 감정은, 놀라움도 안도감도 아닌 반가움이였다."
    haneul"어디 있었던 거야~ 한참동안 여기가 네 기숙사가 아닌 줄 알았다고. 게다가..."
    "작은 목소리로 툴툴대는 하늘이를 보니 여러가지 감정이 밀려들어왔다. "
    "이내 눈에 눈물이 맺힌다."
    yeongwon"..."
    "할 말은 너무 많지만, 목이 메여서 말이 나오지 않는다. "

label scene303: 
    scene bg room2 with Dissolve(1.0)
    "하늘이를 방으로 불러들였다. "
    "서서히 머릿속의 안개가 걷히고, 스스로를 다잡을 수 있었다. "
    "헝클어진 머리와 눈 밑까지 내려온 다크서클. "
    "약한 모습을 보여주기 싫어서일까, 얼굴을 붉히며 급히 자신을 정돈했다. "
        show haneul serious with dissolve
    haneul "사실 계속 무서웠다고... 탈출한 사실이 들키면 어떻게 될까..하며.."
    "어두운 방 안의 탓인지 하늘이는 이전보다 더욱 창백해진 것 같다. "
    "하지만 몸 상태에 대해서는 걱정이 되지는 않는다. "
    "하늘이의 보랏빛 눈동자가, 어느 때보다도 빛을 담고 있었기 때문이다. "
    yeongwon sad"왜...위험하게..."
    yeongwon"이런 데를 오려고 한거야..."
    "냉정해져 생각해 보니, 하늘이가 여기에 온 것이 무엇보다 신경쓰였다. "
    "정황상 쫒겨서 온 것은 아닐텐데.."
    haneul happy"이건 뭐랄까...약간의 모험이랄까나~~"
    haneul"음...조금은 위험해도 말이야..."
    haneul"영원이는 언제나 밖을 동경하고 있는데, 나도 가까워졌으려나.."
    "아아. 아직 하늘이는 아무것도 모른다."
    "억지로 힘든 것을 드러내고 있지 않거나..."
    yeongwon"한설이가 사라졌어."
        show haneul serious
    "어떻게 여기 온것인지, 물어보는 것을 건너뛴 채의 한 마디. "
    "내 입에서 대뜸 나온 말은 분명 하늘이에게는 청천벽력이겠지."
    yeongwon"실종되었다고..! 한설이가..."
    "한동안 침묵이 이어진다."
    "침묵을 깨고 싶었지만, 앞으로 더 무슨 말을 해야 할까."
    "하늘이를 걱정하는 마음이라지만, 갑자기 소리쳐버리다니 어떻게 된 것이 분명하다. "
    haneul sad"그런 일이...있었다니..."
    "눈물이 고인 채로 나는 지금까지 있었던 모든 이야기를 해 주었다."
    "처음 탈출이라는 것을 생각했을 때부터, 어제까지 무슨 일이 있었는지. "
    "하늘이의 표정은 원래부터 무채색이였지만 더욱 더 그림자가 드리운 것 같은 느낌이었다."
    "거기에 그치지 않고, 무거운 표정으로 입을 열었다."
    haneul fury"한설이가 잠시 어디로 떠났다니... 잠시가 아니잖아..."
    haneul"몸이 아프다거나 전학을 갔다던가... 단순한 핑계일 뿐이야..."
    scene bg room2b with Dissolve(1.0)
    "하늘이가 이야기해준 특별반의 이야기는 생각보다 더욱 충격적이였다. "
    "특별반이 결성된 이래, 몇몇 학생들이 돌연 수업에 불참하는 경우가 종종 있었고..."
    "그 중에 일부는 다시 돌아왔지만, 다른 몇 명은 다시는 볼 수 없었다고 한다. "
    scene bg room2 with Dissolve(1.0)
    haneul serious"도대체 뭐가 일어나는지 모르겠어..."
    haneul"그것 때문에 연우도..."
    "아는 이름이 뇌리에 스쳐 정신이 번쩍 든다."
    haneul sad"연우를 마지막으로 본 건.. 작년 가을이야."
    haneul"큰 수술을 앞두고 고아원을 떠나 병원으로 떠났지."
    haneul"하지만 시간이 흐르고... 연우의 근황을 못 들은지 벌써 1년째인걸"
    "절망이란 것을 가장 직접적으로 느낄 때는 불길한 예감이 최악의 현실로 다가왔을 때가 아닐까. "
    "그러나 점점 더 확실해져 간다. "
    "이젠 더  이상 괴로움에 잠겨있고 싶지는 않아."
    "머릿속의 퍼즐이 하나하나, 천천히 맞추어지는 느낌이다. "
    yeongwon"한설이랑 연우는, 꼭 돌아올 거야."
    "그래. 이런 고민은 내 전문. "
    "하늘이에게 이런 무겁고 우울한 걱정을 하게 하고 싶진 않아. "
    yeongwon"그 있잖아, 예전부터 같이 있으면 뭐든 다 이루어질 것 같다고 했지?"
    yeongwon"하늘이가 날 찾아 다시 돌아왔으니 말이야, 나머지 두 명도 곧 만날 수 있겠지.."
    yeongwon"단지 약간 오는 시간이 늦은 것 뿐."
    yeongwon"한설이랑 연우.. 항상 지각하더니.. 언제 오려는거야 참..."
    "내뱉은 말은 가면 속의 겉치레 대사일 뿐,"
    "그 말 안에 들어있는 것은 분명 내 마음을 찌르는 슬픔을 깊이 간직하고 있겠지."
    "하늘아, 눈치채지 말아줘. "
    "너에게만은 강한 영원으로 영원히 기억되길. "
    
label scene304:
    scene bg room2 with Dissolve(1.0)
    "몇 개월만의 만남일까나, 이후에도 정적 속의 이야기는 이어졌다. "
    "우선 하늘이의 깜짝 방문의 원인부터. "
    "하늘이를 포함한 특수반 학생들의 키에는 정리되지 않은 여러 정보들이 들어 있다고 한다. "
    "이전에는 기숙사를 빠져나와 다른 곳으로 들어갈 시도를 누가 했으려나?"
    "하지만 하늘이의 키는 특별반의 잠겨있던 문을 열어버렸고..."
    "결국 하늘이의 시도에 의해 기숙사 입구로 들어갈 수 있게 되어, 맨 끝의 내 방 앞까지 올수 있었다는 것."
        show haneul happy with dissolve
    haneul "...내가 너무 성급했던 걸지도 몰라.. 많이 놀라지 않았어?"
    yeongwon idle2"모험심은 인정해 줄게, 설마했지만 정말 깜짝 놀랐다구."
    yeongwon"그렇지만...오늘은 너무 위험한 것 같았어. 걸리면 어떡하려 했어?"
    haneul"그래도 요즘은 무언가 일이 잘 되고 있는지, 밖에 나가는 건 별로 크게 걸릴 일 없다고 할까~"
    haneul"앞으로 얼마간은 다시 볼 수 있지 않으려나 말이야~"
    haneul"...키 정보의 사용 기록을 지울 수 있는지는 잘 모르겠지만..."
    "역시 위험해 보인다."
    "하늘이는 어느 때보다 진지하지만, 그 그림자 뒷면에 숨겨진 두려움은 어쩔 수 없다."
    "차오르는 눈물을 머금고 하늘이에게 당부한다."
    yeongwon"야, 하늘!"
    yeongwon"너는 그래도...자만의 특수 클래스 우등생이잖아?"
    yeongwon"그 우등생 님이 이렇게 일탈이라니 큰일이네, 큰일!"
    yeongwon"이런 일반 학생의 기숙사까지 들어오시다니, 정말...중대한 원칙 위반이라구.."
    "아까부터 마음에도 없는 소리가 나온다."
    "그렇지만 한설이를 생각하며 다시 마음을 다잡는다."
    yeongwon"네가 지금 곁에 있어도, 곁에 없어도, 언젠가는 다시 만날 수 있을거야."
    yeongwon"그때까지만..."
    "다잡는 것은 마음만이 아닌, 여리다 여린 하늘이의 손. "
    haneul happy2"....."
    "참, 이상한 곳에 쑥쓰러움이 많다니깐, 하늘이는. "
    "일부러 눈을 피하는 듯한 표정은 분명히 버릇이였지. "
    haneul"미안...해..."
    haneul"괜한 말로 걱정시켜 버린 것 같아서..."
    yeongwon"아냐, 오히려 쓸데없는 걱정이 줄어 버렸는걸,"
    yeongwon"이제 아무 일 없이 돌아가기만 하면 말이야 "
    haneul"항상 그런것만 신경쓴다니까, 영원이는.."
    "문이 열리고, 빛이 새어나간다. "
    haneul"보이지 않는 곳에서라도, 도움이 되기 위해서,"
    haneul"언제나 열심히 하고 있을테니까, 걱정하지 말아줘"
    yeongwon"물론, 잘 들어가"
    "그리고..."
    yeongwon sad"'다시 만나고 싶어'"
    "하마터면 밖으로 새어나갈 뻔 했다. "
    "문은 아무 소리도 내지 않은 채 조용하게 닫혀간다. "
    "기분 탓이려나, 눈물이 흐를 것 같아 고개를 들었다. "
    "창문 너머로 밝게 빛나던 달빛은 언제 그랬냐는 듯, 구름 사이로 자취를 감춰버린 지 오래. "
    "오늘의 밤하늘은 하늘이의 편이였을까. "
    with Fade(3, color="#000000")

label scene305:
    scene bg blackscreen with Dissolve(1.0)
    "한설이가 사라진 뒤 며칠."
    "인간심리가 그런 것일까. 불안도 초조함도 이제는 차분해져 냉정함으로 변해버렸다."
    "내 인생에서 제일 신경이 곤두선 나날이라고 감히 생각해본다."
    scene bg classroom with Dissolve(1.0)
    "반 친구들에게는 태연한 척, 원장에게는 포커 페이스, 그러나 방과후 한별이와의 비밀의 추리교실."
    "마치 비가 오는 흔들다리를 걷는 듯한 매일매일,"
    "하지만 우산을 똑바로 들지 않으면 젖어 버리는걸."
    "한설이가 어디로 갔는지 찾아낼 수 있다면...."
    scene bg room with Dissolve(1.0)
        show hanbyeol idle with dissolve
    hanbyeol"이 기록이 작성된 위치와 장소, 내용을 보자면..."
    hanbyeol"만약 한설이가 최상층에 있다면, 결국 후보지는 여기 하나밖에 없네."
    "한별이의 능력에는 언제나 감탄을 금치 못한다. "
    yeongwon idle"후보지가 하나라면..."
    hanbyeol shock"이제는 행동에 옮길 때야."
    scene bg roomb with Dissolve(1.0)        
    "하지만 어딘지 모르게, 무언가가 공중에 붕 떠있는 듯한 느낌을 받는다. "
    "머릿속에 있던 생각을 행동으로 옮기는 건 의외로 쉬울지도 모른다. "
    "그렇지만 무언가 주변의 공기가 나를 짓누르고 있다. "
    "중압감."
    scene bg room with Dissolve(1.0)
    yeongwon serious"아직은 증거가 부족해. 이것만 보고 있다가는 아무 결과도 나오지 않는걸."
    yeongwon"지하실 왼쪽에 아직 보지 못한 자료들이 있었어."
    yeongwon"그때까지만 시간을 가지고...찾아보자"
    scene bg roomb with Dissolve(1.0)        
    "마음이 약해진다. "
    "우산의 틈새로 비바람의 물방울이 새어 버리고 있다. "
    "마치 흔들다리의 줄이 끊어져, 보이지 않는 바닥으로 떨어져 버릴 것과 같은 느낌."
    hanbyeol sad2"내가 아는 너는 목적지가 보이면 그 길로 전력질주하는 사람이라고 생각했어"
    hanbyeol"그치만 조금은 바뀌었구나, 영원"
    "사람은 언제나 바뀐다. 그것이 어떤 것이라도. "
    "하지만 그 말의 어딘가에 숨겨진 본심을 찾아내게 된다면, 그건 어떻게 받아들여야 할까. "
    hanbyeol idle2"적당히 얼버무리는 건 별로 좋다고 생각하지 않는데."
    hanbyeol"언제나 결단력 있게 행동하는 너를 난 항상 믿고 있어 "
    "책임감을 느낀다. "
    hanbyeol happy2"잘 생각해 줘,"
    "의무감을 느낀다. "
    "그래. 스타트를 끊는 것은 언제나 내가 할 일이였어. "
    scene bg blackscreen with Dissolve(1.0)        
   "신중함은 내 전문 분야가 아닐 것이다. "
    "그럴 것이다. 아마도. "
    "아마도라는 말은 불확실성에 대한 변치않는 보험일 것이다. "
    "확정된 미래를 내다보는 것이 불가능한 것은 정해져 있다. "
    "그래서일까, 시간은 우리들의 결정을 비웃듯 흘러간다. "
    scene bg room2 with Dissolve(1.0)        
    yeongwon serious"......"
    "침대 머리맡을 등지고 바닥에 주저앉는다. "
    "시계 소리조차도 정적을 깨는 방. "
    "아무리 늦어버린 밤이라고 해도 나만을 제외하고 시간이 멈춰버린 것 같다.  "
    "이대로 정적에 스며들어 잠들어 버린다면 시간을 멈출 수 있을까. "
    scene bg room2b with Dissolve(1.0)        
    "알고 있다. "
    "미룬다고 되는 일은 단 하나도 없는 것을. "
    "그러나 열쇠는 문고리에 맞지 않는다. "
    "달려나가는 우리들에게 닫힌 문은 웃어주지 않는다. "
    scene bg room2 with Dissolve(1.0)        
    "침대 밑으로 무심코 손을 뻗는다. "
    "손에 잡힌 것은 낡은 일기장, 현 씨의 노트이다."
    "그러나 더이상 다 닳아버린 앞 페이지에는 눈이 가지 않는다. "
    "중간 페이지의 뒷부분을 펼친다. "
    "비가 거세게 내리친다면, 우산을 펼치는 것은 바로 우리들이 될 것이다."
    "뒷장의 무수한 빈 종이를 맞이하기 전, 최종일의 마지막 문장. "
    "어느 때보다 현실적이게 마음을 울린다. "
    scene bg room2b with Dissolve(1.0)        
    "무섭다. "
    "내 일기장의 마지막 페이지는 언제일까. "
    "누군가가 내 일기장의 뒷면을 찢어가고 있지는 않을까. "
    "아무도 아무것도 가르쳐주지 않는 이 현실 속에서, 나는--"
    #play sound "sound/knock.mp3"
    "사고회로가 끊어지고 시간은 흘러간다."
    "한별이는 이 늦은 시간에 뭘 전하러 온 건지. "
    "붕 뜬 기분을 가라앉히고 일기장을 덮는다.  "
    "'아까는 네 기분을 몰라봤었네'"
    "문을 열면, 이 이야기를 하려고 했었다. "
    "하지만, 문이 열린 뒤 나는 아무 말도 할 수 없었다. "
        show haneul happy with dissolve
    "......"
    "못 본지 아주 오래된 것은 아니였다. "
    "이야기를 한 지 불과 얼마 되지 않았던 느낌이다. "
    "그래서 난, 말없이 은빛으로 빛나는 그를 끌어않았다. "
    "마음을 얼리던 모든 것들이 누그러져, 물방울이 되어 떨어진다. "
    "하늘이를 더 가까이에 두고 싶어. "
    "지금은 이 생각만 하게 해 주세요. "
    "내 기분을 아이러니하게도 너무 잘 알아준, 하늘이가 앞에 있다는 걸. "

label scene306:
    scene bg room2 with Dissolve(1.0)        
        show haneul happy with dissolve
    haneul"이렇게 다시 보니... 영원이는 정말 많은 걸 해왔구나..."
    "막상 하늘이를 다시 만나게 되었지만 저번처럼 까무러칠듯 놀랍지는 않았다. "
    yeongwon idle2"이제야 내 업적을 인정하는 거야? 그거 참~"
    yeongwon"특수반도 별거 없구먼, 안 그러십니까? 우등생 하늘 씨~"
    haneul"푸훗, 그게 뭐야? "
    "되살아난 기운을 가벼운 웃음으로 되돌려받는다. "
    "분명히, 이 재회는 예상되어있던 것은 아니였다. "
    "하지만 마음 속 깊이 느낄 수 있었다. "
    "하늘이와는 언젠가 다시 만날 수 있을 것이라고. "
    yeongwon sad2"어쩌면...당연한 것이였을 지도 몰라..."
    yeongwon"같은 교실에서 수업을 듣고, 같은 옥상에서 바람을 맞고, 같은 곳을 바라보며 걷는다는 것은."
    yeongwon"언제부터 어긋나버린 걸까."
    "문득 어린 시절이 떠오른다. "
    "누구에게도 방해받지 않고 어떤 누구보다 소중했던 우리들의 기억."
    "하지만 지금 와서 떠올려봤자 무의미일까나. "
    haneul happy2"자유라는 건 뭘까, 영원아?"
    haneul"이 고아원이 지어지기 전에는, 누군가가 이곳에 있지 않았을까. "
    haneul"적어도 저 유리창문 밖만을 바라보지 않았을 거야..."
    "부러진 날개로 태어난 새는, 나는 법조차 배우지 못한다. "
    "하늘 위에서 비치는 새들의 그림자만을 보며 동경할 뿐. "
    haneul sad"자라면서 우리들이 갈라지는 것은 운명이려니, 하고 생각했었지."
    haneul"하지만 왜 다들 어디론가 사라져 버리는 걸까... "
    haneul"우리한테 인사 정도는 남겨줄 수 있었는데..."
    "고개를 숙인 채로 창문에 기대어 있는 하늘, "
    "무언가를 이야기해주고 싶지만, 마음속이 복잡해 쉽사리 말이 나오지 않는다. "
    haneul happy2"지금까지의 나는 이런 건에 대해 단지 슬퍼하고만 있었어."
    haneul"하지만 지금은 아니야. "
    haneul"네가...정말 많은 것을 나에게 알려주었는걸. "
    "창문 사이로 비스듬히 밤하늘의 구름이 개인다. "
    "나를 향해 돌아본 하늘이의 얼굴이 더욱 밝아 보인다. "
    haneul happy"언제나 너를 의존해왔고 나를 밝혀주었어. "
    haneul"항상...고마워."
    yeongwon"으...응.."
    haneul"이건..그리고 그에 대한 내 마음이야. "
        hide haneul with dissolve
    "복잡하던 머릿속이 사고를 멈춘다. "
    "이건...무슨 상황인 거지?"
    "생각할 겨를도 없이, 하늘이는 내 손을 살며시 잡았다."
    "그리고..."
    "..."
    "무언가와 함께, 하늘이의 손은 다시 내 손에서 멀어져갔다."
    "무심코 손에 쥐어진 무언가를 본다. "
    "두꺼운 종이와 같은, 노트 크기의 물건 하나. "
    "그래, 이건--"
    yeongwon idle "염소고아원 상위구역 출입허가카드, 이름 영원.."
    "순간 사고회로가 엇나간 느낌이 든 것은 기분 탓일거야. "
    "하지만 이내 하늘이가 건네준 것이 무엇인지, 바로 알 수 있었다. "
    "백색의 카드보드에 빛나는 은색의 칩. "
    "특별반의 랜덤 데이터를 사용한 하늘이의 걸작임이 분명하다. "
    "내 사진은 도대체 어디서 구한 거야."
        show haneul sad with dissolve
    haneul"한설이도, 연우도.. 우리들 앞에서 사라져버려.. "
    haneul"너무나 그런 것들이 싫어서, 모두를 지켜내고 싶어서, "
    haneul"꼭, 5명이서 만날 수 있도록.. 마치 예전처럼. "
    "자유의 갈망, 우리들의 추억, 모두에게로의 의지..."
    "단연컨대, 하늘이로부터의 가장 중요한 마음을 담은 것임이 분명하다. "
    "그런데, 그런데 말이지..."
    "어째서 한쪽 마음이 비어버린 느낌이다. "
    "한설이와 한별이, 그리고 선생님들과 모든 사람들..."
    "마치 한 발을 내디디면 굴러떨어져 버릴 것 같은 불균형한 평형상태의 나. "
    "그리고..."
    "왠지 모르게, 한쪽 마음이 빈 것은 마냥 그것만은 아닌 것일지도 모른다고 생각했다. "
    yeongwon idle2"정말 감사합니다, 하늘 씨, 최고의 제품을 만들어 주셨네요."
    yeongwon"저에게 주실 마음은 그것 뿐인가요? "
    "의지할 곳이 필요했을지도 모른다. "
    "같은 감정을 공유하고 싶은 마음이 커진것인지도 모른다. "
    "그 때문일까, 초조해져 부아가 치민다. "
    "비록 하늘이를 등지고 토라진 체를 하고 있지만 말이다. "
    haneul"..."
    "나는 무엇을 원하고 있을까. "
    "솔직히 잘 모르겠다. "
    "하지만..."
    "내 어께에 손을 올린 하늘이는, 나보다 더 솔직한 것 같다. "
    yeongwon shock"..!!"
    "한쪽 어께를 잡힌 나는 순식간에, 하늘이와 마주보게 되었다. "
    "이내,"
    "따뜻한 감촉이 입술 주변을 감싼다."
    "눈이 부시다. "
    "바로 앞의 은색의 별빛은, 눈치없게도 밝게 빛나고 있었다."
    "눈을 감을까도 생각했지만, 이 둘도 없는 빛을 스스로 지우는 것은 너무 아까운걸. "
    "그 시간은 오래가지 못하고- "
    "바로, 내 눈 앞에는 새빨개진 얼굴의 하늘이가 있을 뿐이였다."
    haneul happy"헤헷, 거짓말. "
    haneul"이건, 너에 대한 진짜 내 마음. "
    haneul"5명을 다 지켜내자고 한 우리의 마음과는 별개로, 너만은 내가 반드시 지켜내고 싶은데."
    yeongwon"......."
    "왜 나는 항상 나에게 솔직하지 못한 걸까. "
    "생애 처음 받아보는 고백에, 감히 입이 떨어지지를 않았다. "
    haneul happy2"아...다...답은..천천히 줘도 되니까...."
    haneul"너..너무...무모했으려나....."
    yeongwon sad2"왜... "
    yeongwon"왜 이제서야 말해주는 거야..."
    "말없이 하늘이를 끌어안았다. "
    "그리움에 사무쳐서, 마음이 따뜻해져서..."
    "그리고, 너무나도 사랑하고 싶어서. "
    yeongwon idle"언제나 생각해왔어, 하늘이와 떨어져버리면 어떡하지, 라고.."
    yeongwon"하지만 이제는 괜찮아. "
    yeongwon"우리들은 어디에 있어도, 떨어지는 일은 절대로 없을 거니까..."
    "시간은 우리들의 곁으로 흐르고 달빛은 점점 저물어간다. "
    "이대로라면 얼마든지 있어도 돼."
    "오늘만은 내 곁을 떠나지 말아줘. "

label scene307: 
    scene bg room2bright with Dissolve(1.0)        
    yeongwon idle"..."
    "아침의 선명한 햇빛 한 줄이 나를 깨운다. "
    "어제 마지막으로 기억나는 게 무엇이었을까."
    "연분홍빛 기억이였지만 생각하면 금방 얼굴이 화악, 달아오른다. "
    "도대체 난 뭘 한거야.."
    "분위기에 홀렸던 것이 아닐까. "
    "어제 있었던 일을 되돌아보니 새삼 부끄러워진다. "
    "그러나 그 부끄러움도 모두 우리들을 위한 서약이였다. "
    "'다음 벨이 울리는 저녁날에 다시 만나자'"
    "하늘이가 떠나기 전 고한 다음을 위한 기약. "
    "조용히 남기고 간 그의 흔적을 다시 한번 되짚어본다. "
    "책상 위에는 매끄러운 은색 칩의 출입증이 자태를 뽐낸다. "
    "마침내 우리들의 의지를 잇는 데에 큰 도움이 되겠지. "
    "그리고 아마 실수로 남겨놓고 갔을 것인, 또 하나의 흔적. "
    yeongwon"이 손수건, 아직도 가지고 다니는구나..."
    "새삼 시간의 흐름을 깨닫는다. "
    "하늘이의 티셔츠만큼 컸던 손수건이, 이제는 내 손 안에 사뿐히 잡힌다. "
    "잃어버려서 애타게 찾고 있을 하늘이라지만, 이젠 미소가 절로 난다. "
    "다음 번에 제대로 가져다 줘야지. "
    "내가 자랑하는 최고의 선물과 함께. "
    "오늘은 정말로 오랫만에, 맛있는 아침을 먹을 수 있을 것 같아. "

label scene308:
    scene bg room with Dissolve(1.0)        
    yeongwon idle2"자, 그럼 여기서! 중대 발표가 있겠습니다. "
    yeongwon"한설이를 찾아나가는 모임 회장, 한별이에게 알려드립니다!"
    yeongwon"신기술의 도입으로 드디어, 단박에 올라갈 수 있는 경로가 마련되었습니다~"
    "한별이에게 등록된 카드를 건넨다. "
    "천천히 카드를 읽어보던 한별이, 이내 눈이 휘둥그레진다. "
        show hanbyeol shock2 with dissolve
    hanbyeol"이런 건...어디서 얻었어? 만들었어? "
    yeongwon"사실, 어제 하늘이가 기숙사로 들어와서~"
    yeongwon"나를 존경한다나...특수반 카드가 힘이 될거라고... 헤헤.."
    hanbyeol happy2"......"
    hanbyeol"세상에, 하루종일 붕 뜨듯이 이상하다 했는데, 그런 일이 있었을 줄이야..."
    "눈가가 떨리고 있어, 한설. "
    "먼지가 앉은 실험 레포트를 다시 펼치고, 펜이 지나가며 선을 만든다. "
    "마치 한동안 죽어있던 우리들의 눈동자가 다시금 살아난 것과 같이. "
    "그리고 마침내--"
    "한설이 구출작전의 일자가 정해졌다."
    "지난 작전은 실수고, 이번 작전이 진짜. "
    "드디어 원장에게 한 대, 큰 반격을 선사할 때가 왔다. "
    "제발, 내딛는 발걸음에 축복이 있기를. "
    "한설이와 연우, 그리고 사랑하는 하늘이에게 축복을. "

label scene309:
    scene bg blackscreen with Dissolve(1.0)                
    "시간이란 건 참 빠르게 흘러간다. "
    "그 시간이 우리에게 소중하다고 생각할수록 말이다. "
    "멈추어 가던 내 시계는 다시 한번 빠르게 태엽을 감는다. "
    "모두를 되찾기 위한 둘도 없는 여정. "
    scene bg room2 with Dissolve(1.0)        
    "드디어 내일, 작전의 때가 도래했다. "
    "증거는 완벽하고 연습은 충분하다. "
    "건물 구조와 행선지 경로를 몇 번이나 머릿속에 시뮬레이트 해 본다. "
    "그럼, 되었을까나.  "
    "보고서를 덮고, 붉은 손수건을 손에 맨다. "
    scene bg skysunset with Dissolve(1.0)        
    "늦가을의 오렌지색으로 물든 하늘을 바라보며 걷는다. "
    "오늘따라 차폐 우산으로부터 생긴, 반투명한 그림자가 더 옅어 보인다. "
    "따가운 햇빛은 바람을 타고 씻겨져가기라도 하는 것일까. "
    "그렇게 생각하는 도중에, 무심코 도착해 버렸다. "
    scene bg oldschool with Dissolve(1.0)        
    "우리 다섯 명의 추억과 의지가 잠든 곳. "
    "그리고, 마지막 벨이 울리는 저녁날의 약속장소.  "
    "언제나 작은 의자에 앉아, 책을 읽고 있던 하늘이를 떠올린다. "
    "그걸 다시 본다면, 이제야 우리의 일상을 되찾아가는 것인가는 생각이 들지도. "
    scene bg ajit with Dissolve(1.0)        
    "아지트의 문을 열고 안을 들여다본다. "
    "그러나, 그 안은 어두컴컴한 채로 비어 있었다. "
    "아직 시간이 조금 빠르긴 하지. "
    "불을 켜고, 의자에 앉아 벽에 기댄다. "
    "빈 노트에 글자를 썼다가 선을 그어 지운다. "
    "낡은 의자의 나무 끄트머리를 건드렸더니, 툭 하고 부러져 버렸다. "
    "오렌지색 하늘은 자취를 감추고, 감색 하늘만이 박명을 내고 있을 뿐. "
    "하지만 내가 보고 싶은 하늘은 어디로 간 걸까. "
    scene bg skydark with Dissolve(1.0)        
    "30분, 한 시간..."
    "무언가 이상하다. "
    "잊어버리지는 않았을 터이다. "
    "쪽지가 있었으면 애초에 찾아봤을 것이다. "
    "또 갑자기 바쁜 일이 생겼겠지, 라고 생각하기에는 너무 시기가 적절하지 않다. "
    "혹시 내 기숙사를 찾아왔던 것을 누군가가 눈치챈 것이 아닐까? "
    "아니면, 위장용 카드를 만들어 준 것이 걸렸다던가. "
    "한번 시작된 걱정은, 언제나 또다른 걱정을 낳는다. "
    "그러나 만들어진 불안감이 더 큰 초조함과 불편함을 낳는다면 큰 문제가 될 수 있다. "
    scene bg ajit with Dissolve(1.0)        
    "머피의 효과라고 하던가. "
    "이런 생각은 하지 말자. "
    "초조함을 억지로 틀어막고 아지트의 불을 끈다. "
    "내일의 작전에 집중하라는 계시일지도 모른다."
    "'이런 이별이 되는 것은 너무 치사해'"
    "아아, 자꾸 이런 생각이 떠오르는 건 왜일까. "
    "기숙사에 돌아가서 푹 쉬는게 좋겠다. "

label scene310:
    scene bg dorm with Dissolve(1.0)        
    "아직 한밤중은 아니였지만 해가 짧아진 탓일까. 기숙사는 더 어두워 보였다. "
    "경비원에게 들키지 않도록 살금살금 입구 쪽으로 향한다. "
    "그런데, 무언가 수상하다. "
    "못 보던 거대한 실루엣의 무언가가 기숙사 옆에 놓여 있었다. "
    "단지 밤이라 검게 보이는 것이 아닌, 무광의 칠흑색. "
    "마치 빨리 들어가라고 나를 압박하는 것 같다. "
    scene bg blackscreen with Dissolve(1.0)                
    "안에 도착해서 쉽사리 어둠 속으로 스며들어, 올라가는 계단에 올라탄다. "
    scene bg stairs with Dissolve(1.0)                
    "그 때, "
    "귀를 때리는 강렬한 파열음에, 황급히 몸을 숨긴다. "
    yeongwon shock"뭐, 뭐야..!"
    "유리 조각이 산산조각나고 건물 벽이 흔들린다. "
    "이내 사이렌 소리와 함께 자극적인 빨간 불빛이 깜빡거린다. "
    "건물 1층 좌단 외부침입 감지. 건물 1층 좌단 외부침입 감지. 신속히 대피 및 이동할것. "
    "비상 사태. "
    "밤의 기숙사에 이런 큰 사고가 일어난 적은 없었다. "
    "너무나 갑작스럽게 일어난 일이였다."
    "내 자신이 있었다는 걸 숨기기 위해, 황급히 층계참을 가로질러 복도로 향한다. "
    scene bg stairsb with Dissolve(1.0)                
    "그런데, "
    "하늘이는, 오늘 만나는 장소를 헷갈린 걸까? "
    "총소리가 들린다. "
    "숨이 제대로 삼켜지지 않는다. "
    "머리가 갑자기 뜨거워져, 죽을 기세로 계단을 뛰쳐올라간다. "
    scene bg hallwaydorm with Dissolve(1.0)                
    "하늘이가 이곳에 왔다 갔을 수도 있어. "
    "아니면, 왔다가--"
        show hanbyeol shock2 with dissolve
    hanbyeol"영원! 어딜 간거야!"
    "모두가 우왕좌왕하고 있는 복도 사이로 한별이가 보인다. "
    yeongwon"하...하늘이는? 혹시 하늘이 봤어? "
    hanbyeol serious"걔를 왜 찾아, 여기 있을 리가 없잖아!"
    hanbyeol shock"그것보다 비상상황이라고, 곧 선생님들이 반장을 찾을 거야. "
    hanbyeol"네가 이탈을 한 걸 안다면, 일이 복잡해질 수도 있어..."
    "그래, 비상상황 행동강령을 일단 지키는 게 먼저야.."
    scene bg hallwaydormb with Dissolve(1.0)                
    "모두들을 대피시키고, 선생님들과 이야기를 하는 사이에도 집중은 딴 데 쏠려 있었다. "
    "하늘이는 무사할까. "
    "오늘 하늘이는 왜 안 보였을까. "
    "그리고... 내일 우리들은 과연 어떻게 될까. "
    "미래의 결과는, 아무도 모른다. "

label scene311:
    scene bg blackscreen with Dissolve(1.0)                
    "결과부터 이야기하자면, 우리들의 작전은 수정이 불가피하였다. "
    "밤새도록 상황은 수습된 듯 하지만, 그에 따른 뒷조사가 이루어지는 듯 했다. "
    "소지품 검사, 사건 목격진술 등..."
    "유리로 만들어진 보이지 않는 길을 따라 걷고 있다. "
    "결국 나온 결론은 난방기기 관리 소홀로 인한 폭발사고. "
    "거짓말, 난 총소리를 들었는데. "
    "이제는 무엇이 거짓말인지도 모르겠다. "
    "아니, 그냥 내가 아직 무사한 것이 누군가로부터의 거짓말인지도 모른다. "
    scene bg hallway with Dissolve(1.0)
    yeongwon idle"그럼, 가볼게요 선생님. "
        show teacher with dissolve
    teacher"그래, 지금 너무 분위기가 어수선하네."
    teacher"우리 반은 그래도 영원이 덕분에 덜 위축되는 것 같아. "
    teacher"항상 고마워, 영원아. "
        hide teacher with dissolve
    "그 이후로는 아무것도 일어나지 않았다. "
    "하지만 원래대로라면, 우리가 무언가를 일으켜야 했었다. "
    "그럴 작정이였다. "
    "하지만, 거짓말같게도 아무것도 할 수 없었다. "
    scene bg room with Dissolve(1.0)
        show hanbyeol sad2 with dissolve                
    hanbyeol"벌써 초겨울이 다 되어가는데, 아무것도 할 수 없다니..."
    "한별이의 방에 들어가면, 창문을 바라보는 한별이만이 나를 맞이한다. "
    yeongwon serious"상황이 너무 좋지 않은걸..."
    yeongwon"이제 한밤중에도 계단 주변에는 불을 켜놓도록 바뀐 것 같아. "
    yeongwon"로비는 말할 것도 없고..."
    yeongwon"......"
    "더이상 말하는 것은 구차한 변명일지니."
    "내가 달리는 만큼, 종착점은 더 멀어진다. "
    hanbyeol"오늘로 벌써 한달 가까이 밀려버렸어..."
    hanbyeol"정말 어떻게 해야 좋을까..."
    scene bg roomb with Dissolve(1.0)                
    "위로를 해 주고 싶지만, 기운이 나지 않는다. "
    "내가 무슨 말을 한다고 해도, 쌓여 온 그리움과 아픔은 사라지지 않는 걸까. "
    "안경에 비친 한설이의 눈은, 약간 부어 있는 듯한 느낌이였다. "
    scene bg room2b with Dissolve(1.0)                
    "마지막으로 발걸음이 무겁지 않을 때는 언제였을까. "
    "힘겹지 않고 스트레스 받지 않는 날이 왜 일상적이지 않다고 생각하게 되었을까. "
    "여느때와 같은 기숙사의 적막함은 이제 익숙해졌다. "
    "정적의 선율을 깨는 풀벌레 소리, 창가의 엷은 바람소리. "
    "전부 내 일상의 이레귤러적인 존재. "
    scene bg blackscreen with Dissolve(1.0)                
    "침대에 누워 무의식적으로 눈을 감는다. "
    "하늘이에 대한 걱정, "
    "한설이에 대한 불안감. "
    "모든 것이 섞여 블랙홀 속으로 빨려들어간다. "
    "대신 무언가 마약에라도 홀린 듯, 행복한 상상만이 떠오른다. "
    "마치 오래된 꿈과 같은 이야기. "
    "하지만 이런 현실 속에서 일어난 거짓말같은 이야기. "
    "지금부터 영원히, 이런 상상만을 할 수 있게 해 주세요. "
    "하늘이만을 보고싶은 것은, 제멋대로인 걸까."
 
label scene312:
    scene bg sky with Dissolve(1.0)                
    "한별이는 요새 부쩍, 허공만을 바라볼 때가 잦다. "
    "물론 이전부터, 하늘을 초점 없이 바라보는 것은 내 쪽이 아니였을까. "
    "어지럽게 펼쳐진 종이들 가운데에, 우리는 말 없이 마주보고 앉아 있었다. "
    scene bg roomb with Dissolve(1.0)     
        show hanbyeol sad with dissolve                                   
    hanbyeol"이제는 해야할 것 같아."
    hanbyeol"한설이...만나러 가야지..."
        hide hanbyeol with dissolve                                   
    "저물어가는 해는 우리들의 얼굴에 그림자를 드리운다. "
    "더이상 핑계를 댈 수는 없었다. "
    "지금이라도 실행에 옮길 수밖에 없었다. "
    "내가 하자고 했던 일이다. "
    "분명히 내가 이루어내야 할 일이다. "
    scene bg background with Dissolve(1.0)                
    "어째서, 이렇게 되어버린 걸까. "
    "시간은 눈치없이 계속 흘러가지만, 우리에게 잡을 권한 따위는 없다. "

label scene313:
    scene bg hallwaydormb with Dissolve(1.0)                
    "푸르스름한 불빛조차 사라져버린 어두운 밤,"
    "정적만이 감도는 복도에 한 발짝, 엷은 발소리가 어둠 속에 숨는다. "
    "제대로 볼 수 있는 것은 없다. "
    "다만 한별이와 서로 의지하며 앞으로 나아갈 뿐."
    "왼쪽 복도의 끝에 붙어, 계단으로 내려갈 준비를 한다. "
    scene bg roomb with Dissolve(1.0)      
        show hanbyeol idle with dissolve                                             
    hanbyeol"이 날, 바로 경비원 한 명이 비는 날이야. "
    hanbyeol"한 시간 동안은 교대할 인원이 줄어드니, 이쪽을 감시할 수 있을 리 없지. "
        hide hanbyeol with dissolve                                   
    scene bg hallwaydormb with Dissolve(1.0)                
    "계단의 소등 시간을 틈타, 재빨리 숨어들어간다. "
    scene bg stairs with Dissolve(1.0)                
    "이전과는 다른 환한 로비에 자동으로 몸이 움츠러든다. "
    "너무나 눈이 부시다. "
    "그러나 이 빛은 거짓을 만들기 위한 위선의 빛. "
    "로비의 깨져 있는 유리와 벽은, 아직도 두꺼운 천으로 가려져 있다. "
    yeongwon idle"저쪽으로!"
    "정시가 약간 지난 지금, 인수인계가 되기 전의 잠깐의 틈. "
    "지금이야말로 진실을 위한 그림자가 숨어들어갈 때이다. "
    scene bg dorm with Dissolve(1.0)                
    "계단의 문을 뒤쪽으로 밀고 나와, 평소와 반대 방향으로 돌아나간다. "
    "사각지대만을 밟고 지나간 우리는 곧바로 본관 쪽의 루트로 향할 수 있었다. "
        show hanbyeol fury with dissolve                                   
    hanbyeol"......반드시.."
    hanbyeol"...반드시, 내가 구해낼 거야."
    "작게, 말소리가 들린 것 같았다. "

label scene314:
    scene bg schooldark with Dissolve(1.0)                
    "매일 이곳으로 다니지만, 역시 어둠이란 것은 모든 것을 낮설게 만든다. "
    "머릿속의 지도를 다시 떠올려본다. "
    "제일 윗층의 교실, 교실과 원장실을 잇는 계단, 교실 주변의 사각지대. "
    "-인증 되었습니다, 보안 레벨 A-"
    "1층의 문이 열리며, 작전의 본격적인 시작을 알린다. "
    scene bg hallwaydark with Dissolve(1.0)                
    "맨 아랫층에서 저층을 올라가는 건 상대적으로 쉽다. "
    "뒷문으로 들어가면 바로 나오는 인적 없는 계단. "
    "2층으로 올라가는 것까지는 자유롭지만, 그 윗층부터의 길에는 철제 블라인드가 단단히 자물쇠에 걸려 있다. "
    scene bg roomb with Dissolve(1.0)
        show hanbyeol idle with dissolve                                             
    hanbyeol "보통 사람들이 생각하듯이, 구식 자물쇠의 키는 일반적으로 그 주변의 어딘가에 숨겨져 있지. "
    hanbyeol"이 경우에는, 바로 이곳. "
    hanbyeol"사람의 심리는 단순하다고 생각하지 않아?"
        hide hanbyeol with dissolve                                   
    scene bg hallwaydark with Dissolve(1.0)                
    "미리 조사한 대로, 교무실 뒷문 옆 서류 보관함 뒤쪽을 살짝 열어본다. "
    "녹이 슬대로 슬어 있는 낡은 키가 보인다. "
    "조심스레 블라인드의 한쪽 구석을 연 뒤, 위로 살짝 들어 헤쳐나간다. "
    yeongwon"...영차..."
        show hanbyeol idle with dissolve                                             
    hanbyeol sad"......"
    "한별이는 평상시보다도 더욱 안정된 모습인 듯 보였다. "
    "역시, 그녀를 여기까지 데리고 온 것은 불굴의 용기가 아닐까."
    "하지만 심호흡이 짧아지고 심장이 빠르게 뛰는 걸 감추지는 못한다. "
    "그렇다. 연기하고 있다. "
    hanbyeol"여기서는, 전에 말한 대로...기억하지? "
    yeongwon"자, 움직이자. "
        hide hanbyeol with dissolve
    scene bg blackscreen with Dissolve(1.0)                
    "계획은 수백번 다시 고쳐 그릴 수 있지만, 실행은 단 한번 뿐. "
    "교실이 있는 층의 제일 꼭대기 층으로 간다. "
    "가장 구석에 있는 것은--"
    scene bg hallway2dark with Dissolve(1.0)
    "도서실이다. "
    "이래뵈어도 우리가 접근할 수 있는 시설 중, 가장 최첨단의 기술이 적용된 곳. "
    "이곳에서 데이터베이스 열람용의 관리자 카드를 꺼내기만 하면, 원장실의 모든 자료에 접근할 수 있다. "
    scene bg roomb with Dissolve(1.0)
        show hanbyeol idle with dissolve                                                             
    hanbyeol"먼저, 내가 도서실이 있는 층의 전원을 완전히 꺼 버릴거야. "
    hanbyeol"아주 잠시나마, 서고의 잠금장치가 무력화되는 거지. "
    hanbyeol"그대로 네가 서고 안으로 들어가서, 관리자 카드를 꺼내오는 거야. "
    hanbyeol"그때는 네 카드를 믿을 수 밖에 없겠네. "
        hide hanbyeol with dissolve                                   
    scene bg hallway2dark with Dissolve(1.0)
    "도서실의 거대한 유리문 앞에 선다. "
    "한별이의 준비는, 아직이려나, "
    "그때였다. "
    "푸른 빛을 내며 깜빡거리던 유리문의 정중앙이, 아무 소리도 내지 않고 침묵했다. "
    "타이밍은 지금이다. "
    "우리에게 허용된 단순간의 어둠을 타고, 바로 안으로 숨어들어간다. "
    scene bg library with Dissolve(1.0)
    "언젠가 찾은 적이 있는 것 같은 도서실 안쪽의 오래된 서고, "
    "매케한 곰팡이 냄새로 가득한 이 가운데, 비밀이 숨겨져 있다. "
    "어디로 간 거지."
    "시간이 없다. "
    "그 때, 책꽂이 사이로 희미한 빛이 새어나온다. "
    "한눈에 봐도 튼튼해보이는 철제 캐비넷의 위로 불빛이 점멸한다. "
    "이제 활약을 할 때가 왔다. "
    "매끄러운 은빛의, 특제의 보안 칩."
    "키 카드를 접촉한다. "
    "-오류, 등록되지 않은 사용자 이름입니다- "
    "어?"
    "-오류, 등록되지 않은 사용자 이름입니다- "
    "-인식 오류를 2회 감지하였습니다. 3회 오류시 권한이 제한됩니다. -"
    "어긋났다. "
    "계획의 틀어짐. "
    "한 번만 더 카드를 인식한다면, 무슨 일이 일어날지 장담하기 어렵다. "
    "기숙사 방문으로만 카드를 시험해봤던 건 큰 잘못이였을까. "
    "......"
    "방법을 생각해내야 한다. "
    "하지만 어떻게?"
    "지금이라도 한 발짝을 앞으로 내디딘다면, 낭떠러지에서 떨어질 것이다. "
    "애초에 벼랑 위에서 길을 그려봤자, 샛길이란 건 존재할 수 없을 터. "
    "푸른빛 LED가 눈동자를 향하여 빛난다. "
    "마치 진실이라는 것은 네게 있을 수 없어, 라고 말하는 것과 같이. "
    "들이닥치는 불안감. "
    "이 이후에는 어떻게 될까. "
    "상정 범위 내이다, 라고 생각하면 될까나. "
    "맞아, 우리는 아직 길을 벗어나지 않았어. "
    "데이터베이스 출입이 없어도, 자료를 수집할 수는 있을 것이다. "
    "이 일은 없던 것으로 하자. "
    "책의 산더미를 뒤로 하고, 서서히 뒷걸음질친다. "
    scene bg blackscreen with Dissolve(1.0)                
    "도서관 옆의 전기실로 쏜살같이 움직인다. "
    "한별이와 만나, 최상층의 원장실로 올라가기만 하면 되는 것이다. "
    "그럴 것이였다. "
    scene bg hallway2dark with Dissolve(1.0)
    "하지만 누군가가 이렇게 이야기하였다. "
    "이미 한 걸 완전히 되돌리는 것은, 불가능하다고. "
    "옆에서 무언가가, 움직이는 소리가 났다. "
    "붉은 색 불빛이 켜진다. "
    "전기실 옆의 엘리베이터. "
    "움직이고 있다. "
    "1층에, 멈춰선다. "
    "다만 그곳에 멈춰선 것은 아니다. "
    "불빛의 신호가, 역삼각형에서 정삼각형으로 바뀐다. "
    "날 지켜보고 있다. "
    "그러나, 발을 움직일 수 없다. "
    "붉은 색 불빛이, 더 높은 숫자를 가리킨다. "
    yeongwon"꺄악--"
    with vpunch
    "누군가가 손목을 끌어잡았다. "
    "한별이였다. "
    "전기실에 숨어있던 한별이는 그대로, 뒤도 돌아보지 않고 계단 쪽을 향해 달렸다. "

label scene314_0:
    scene bg stairsdark with Dissolve(1.0)
    "상상하지 않던 의외의 사건은 왜 항상 연달아 일어나는지, 이에 대해서는 증명된 바가 없다.  "
    "하지만 그것이 부정적인 힘을 가진다면, 그런 힘이 존재하는 것이 분명하다. "
    "그럴 것이다. 아마도. "
    "만약 그 자리에 그대로 있었다면, 어떤 일이 일어났을 지. "
    "머릿속의 사고회로가 모조리 끊어진 것 같다. "
        show hanbyeol shock2 with dissolve                                                             
    hanbyeol"하마터면 위험할 뻔 했어. "
    hanbyeol"관리자 카드는 가지고 왔어? "
    yeongwon"......"
    "대답하는 것을 주저한다. "
    "단순히 실패를 이야기할 자신이 없는 걸까.  "
    "아니면 우리들의 여정이 방해받는다는 것이 두려워져 버린걸까. "
    hanbyeol shock"만약 없다고 해도, 카드키랑 주변 자료들로 충분히 한설이가 어딨는지 알 수 있을거야. "
    hanbyeol"자, 이제 마지막만 남았어. "
    "한별이의 손가락이 비스듬한 위쪽을 가리킨다. "
    "칠흑과도 같은 어둠 속 여정의 끝이다. "
        hide hanbyeol with dissolve                                   
    "계단을 타고 바로 위쪽, 복도를 지나치면 바로 원장실. "
    "올라간다면 되돌릴 수 없다. "
    "나는, 한별이의 손을 잡고..."
    menu:
        "...나아가자.":
            jump scene314_1
        "......":
            jump scene314_2

    label scene314_1:
        "그대로, 위로 한 발짝 내딛었다. "
        "진실에 더욱 다가간다. "
        "우리들의 추억을 모두 지키기 위해서. "
        "원장이 마음대로 하게 두진 않을거야. "
        "마지막 계단에 오르고, 문고리에 손을 올린다. "
        "-인증 되었습니다, 보안 레벨 D-"
        "문이 열리고, 처음 본 것은--"
    scene bg hallwaylight with Dissolve(1.0)
        "빛이였다. "
        "너무 많은 빛이 들어와 눈이 부시다. "
            with Fade(0.1, 0.1, 0.1, color="#FFFFFF")
        "원장실 복도에 놓여진 수많은 조명들이, 한데 켜져 밝게 빛나고 있었다. "
        "온몸이 부르르 떨린다. "
        "원장실 가까이에 있는 한 줄기의 빛에 주목한다. "
        "백색 파동이 일렁이며 진실을 교란시키는 걸까. "
        "누군가의 그림자가 보인 듯 한 느낌이 들었다. "
            with Fade(0.1, 0.1, 0.1, color="#FFFFFF")            
        "눈을 깜빡이니, 그의 그림자는 감쪽같이 사라졌다. "
        "푸른 빛 신호가 멀리서 깜빡이는 듯한 느낌이 들었다. "
        "곧 사라질, 내 눈에만 보이는 환영인 걸까. "
        "한 줄기의 빛이, 이쪽으로 와서 나를 비추는 듯 한 느낌이 들었다. "
            with Fade(0.1, 0.1, 0.1, color="#FFFFFF")
        "마치 사진을 찍기 전 받는 스포트라이트. "
        "하지만 나는 과연 피사체일까, 아니면 과녁일까. "
        "다시 고개를 들고, 앞을 똑바로 본다. "
            with Fade(0.1, 0.1, 0.1, color="#FFFFFF")
            with pause(1.0)
            with Fade(0.1, 0.1, 0.1, color="#FFFFFF")
    scene bg hallwaylight_dooropen with Dissolve(1.0)
        "원장실의 문은, 활짝 열려 있었다. "
        yeongwon shock"아아아아아악---!"
        "앞으로 나아가지 못한 내 다리는, 그대로 180도 돌아--"
        "정신을 차려보니, 한별이를 끌고 계단 밑으로 달리고 있었다. "
        jump scene315
    
    label scene314_2:
        yeongwon"......"
        "그저, 잡고 있었던 것은 나를 위해서.  "
        "살을 에는 공포심에 몸을 지탱할 수가 없다. "
        "주변이 모두 검은 낭떠러지로 메워진 것 같은 느낌이다. "
        "한 발짝을 내딛어 밟게 되는 종착점은 과연 어디인 걸까. "
        "멀리서 엘리베이터가 지르는 괴성이 들린 듯 하였다. "
        "내 상상이라고 해도 뭐든지 좋아.  "
        "제발, 내 목을 죄진 말아줘. "
            show hanbyeol shock2 with dissolve                                   
        hanbyeol"영...원아.?"
        yeongwon"......"
        "마치 지탱할 곳을 잃은 나무토막처럼 균형을 잃는다. "
        "아래를 향하는 고개. "
        hanbyeol"뭐...하는 거야... 빨리 일어나..."
        yeongwon"처음부터...미친 짓이였어..."
        yeongwon"우리들이 고작 이 정도로 뭔가를 이뤄내자고 하다니, 착각도 정도가 있지... "
        yeongwon"이제 우리도..."
        yeongwon"한설이의... 뒤를 따라갈지-"
        hanbyeol fury"개소리 하지마!!!"
        "한순간에 일어난 일이였다. "
        "목덜미에서 위로 잡아당기는 충격에 목이 매달린다.  "
        scene bg jeon2 with Dissolve(1.0)
        "이윽고 보이는 것은 위쪽에서 내려다보는 강렬한 초록 빛의 분노. "
        hanbyeol"뭐라고, 뒤를 따라간다고? 그게 네가 할 소리야? "
        hanbyeol"너가 여기서 잘한게 뭐가 있다고...!!"
        hanbyeol"네가 계획을 세웠으면 끝까지 책임져야 될 거 아니야..."
        hanbyeol"모두를 위한 자유? 세계를 위한 정의? 웃기지 말라고 해..!!!"
        hanbyeol"하지도 못 할 일을 크게 벌려놓기나 하고, 한설이는 실종되기나 하고..."
        hanbyeol"그래 놓고 위험하다고 내빼려고, 거짓말하고 도망가려고..."
        "초록빛의 색은 점점 짙어지고 있었다. "
        "밀려오는 위기감, 계획의 실패, 그리고 우리들의 우정의 산산조각."
        "그것을 보는 난 정말 놀랍게도, 아무 말도 할 수 없었다. "
        "오직 할 수 있는 것은, 고개를 돌리고 침묵하는 것일 뿐. "
        hanbyeol"한설이는...희생당한 거야......그때...그때......가지만 않았더라면..."
        hanbyeol"버려진 난, 어떻게 할건데..."
        "파르르 떨리는 눈동자가, 이내 힘을 잃는다. "
        "분노는 이내 슬픔으로 바뀌어, 한설이의 눈가를 적신다. "
        "그 때였다. "
        scene bg stairsdark with Dissolve(1.0)
        "마치 괴수가 포효하는 듯한 소리를 내며, 발소리가 들린다. "
        "귀로부터 공포가 엄습한다. "
        "이렇게 큰 소리를 내며 싸웠는데, 누군가가 눈치채지 못하는 것이 이상하다. "
        "우리들은 너나할 것 없이, 혼비백산하여 도망쳤다."
        jump scene316

label scene315:
    scene bg stairsdark with Dissolve(1.0)
    "어떻게 되든 좋다. "
    "이 결과가 어떨지 나는 알 수 없다. "
    "하지만, 나는 노려지고 있다. "
    "이건 확실하다. "
        show hanbyeol shock with dissolve                                   
    hanbyeol"뭐 하는거야!! 갑자기 왜 도망친 거야..."
    yeongwon shock"저...저기를 어떻게 가라는 거야!"
    "불규칙한 숨을 내뱉으며 힘겹게 이야기한다. "
    yeongwon"빛이 우리를 비추고, 누군가가 있고, 문은 갑자기 열리고..."
    yeongwon"이대로라면 우리는 저 곳에 잡혀가, 나올 수 없게 되어 버린-"
    hanbyeol shock2"무슨 소리야, 영원아?"
    hanbyeol"애초부터 원장실 불은 꺼져 있고 잠겨 있었잖아. "
    scene bg blackscreen with Dissolve(1.0)
    "......?"
    "나는 지금, 무엇을 보고 있을까."
    "앞에 있는 사람은, 한별이일까. "
    scene bg stairsdark with Dissolve(1.0)
    hanbyeol"일단, 일단 올라가서 문 앞에 있어, 내가 카드키로 안에 들어갈 거야. "
    yeongwon"안 돼, 돌아가야 돼. "
    yeongwon"곧 원장이 이리로 내려올 거야, 날 잡아 가둘 거야..."
    "처음부터 이런 일을 하는 것이 아니였다. "
    "모험심이라고 시작하기에는 감당할 수 없는 일이였다. "
    "정의감이라고 치부하기에는 나는 아무것도 아닌 사람이였다. "
    hanbyeol fury2"카드 키 이리 줘!!"
    hanbyeol"혼자라도 다녀올 거니깐..."
    yeongwon"안돼, 가지 마!"
    yeongwon"가면 너 죽어...안돼..."
    "아무것도 하지 못하는, 다리가 풀려 주저앉은 나. "
    "그리고 수 개월 내내 쌓여가던, 한별이 마음 속의 검은 물질. "
    "한계치를 넘겨 담겨있던 그것은, 드디어 임계점을 맞았다. "
    hanbyeol fury"야, 영원!!"
    "한순간에 일어난 일이였다. "
    with vpunch
    "목덜미 쪽에 강한 충격이 느껴진다. "
    scene bg jeon2 with Dissolve(1.0)
    "이윽고 보이는 것은 지근거리에서 바라보는 강렬한 초록 빛의 분노. "
    hanbyeol"뭐라고, 너가 죽는다니 뭐라니, 말할 자격이 있어? "
    hanbyeol"너가 여기서 잘한게 뭐가 있다고...!!"
    hanbyeol"네가 계획을 세웠으면 끝까지 책임져야 될 거 아니야..."
    hanbyeol"모두를 위한 자유? 세계를 위한 정의? 웃기지 말라고 해..!!!"
    hanbyeol"하지도 못 할 일을 크게 벌려놓기나 하고, 한설이는 실종되기나 하고..."
    hanbyeol"그래 놓고 위험하다고 내빼려고, 거짓말하고 도망가려고..."
    "초록빛의 색은 점점 짙어지고 있었다. "
    "밀려오는 위기감, 계획의 실패, 그리고 우리들의 우정의 산산조각."
    "그것을 보는 난 정말 놀랍게도, 아무 말도 할 수 없었다. "
    "오직 할 수 있는 것은, 고개를 돌리고 침묵하는 것일 뿐. "
    hanbyeol"한설이는...희생당한 거야......그때...그때......가지만 않았더라면..."
    hanbyeol"버려진 난, 어떻게 할건데..."
    "파르르 떨리는 눈동자가, 이내 힘을 잃는다. "
    "분노는 이내 슬픔으로 바뀌어, 한설이의 눈가를 적신다. "
    "그 때였다. "
    scene bg stairsdark with Dissolve(1.0)
    "마치 괴수가 포효하는 듯한 소리를 내며, 발소리가 들린다. "
    "귀로부터 공포가 엄습한다. "
    "이렇게 큰 소리를 내며 싸웠는데, 누군가가 눈치채지 못하는 것이 이상하다. "
    "우리들은 너나할 것 없이, 혼비백산하여 도망쳤다."
 
label scene316:
    scene bg dorm with Dissolve(1.0)
    "정신을 차려 보니, 옆에 한별이는 없었다. "
    "본관을 빠져나온다고 해도 안심이 되지 않는다. "
    "길목에서 감시하고 있지는 않을까. "
    "기숙사 로비의 경비원이 나만을 지켜보고 있는 건 아닐까. "
    "내 기숙사 방에, 누군가가 숨어 있는 건 아닐까. "
    "소리를 들을 수 있을 정도로, 심장이 크게 뛴다. "
    "벌써 도착한 곳은 기숙사 앞. "
    "기숙사 로비의 사각지대에는, 이미 경비원들이 배치된 상태였다. "
    "어느 쪽으로 돌아가지, 라고 생각하던 와중에, "
    "발소리가 들려, 황급히 몸을 숨긴다. "
    "한별이도 기숙사로 온 걸까. "
    "잡히지 않고, 아무 일 없이 돌아온 게 분명하다. "
    "확신에 찬 나는, 가까워진 발소리의 사람을 본다. "
    "그러나, 나랑 시야가 맞은 사람은-"
    "뜬금없게도, 한설이네 반 담임선생님이였다. "
        show overwatch fury with dissolve                                   
    overwatch"어? 너 누구니?"
    overwatch"혹시 2반 반장 아니니? 왜 이런 곳에 있어? "
    "어둠 속에서 모습을 드러내는 나를 보고, 손전등을 비춘다. "
    "만신창이에 땀범벅인 내 모습을 보고, 누구라도 수상하다고 생각하지 않을까. "
    yeongwon idle"아...하하하..."
    yeongwon"사실 그 누군가가 약간 상태가 안 좋은데, 오늘은 제가 당번에다 반장이라서요..."
    yeongwon"이...일단 제가 위에 계신 분한텐 이야기 해놓긴 했는데, 일단 오래 걸리는 일이다 보니 힘들기도 해서 잠깐 쉬려고..."
    "내가 생각해도 급조한 티가 너무 많이 난다. "
    "평소 같았으면 좀 더 좋은 변명을 생각해 낼 수 있었을 것이다. "
    "결국, 이렇게 들켜버리는 건가..."
    overwatch idle"아, 알겠어. 너희 반 담임선생님 쪽에도 아는 내용이면 상관 없겠네. "
    overwatch"나는 오늘 당직이라서, 혹시 필요한 일 있으면 부르고. "
    overwatch"그리고 한밤중에는 로비 쪽으로 나오면 안 되는 거, 알고 있지? 다음부터는 잘 지켜줘. "
    "......"
    "의심받지 않아서 다행이다. "
    "선생님의 지시에 따라, 기숙사 쪽으로 돌아간다. "
    "그러나, 발을 옮기기 전에 제멋대로 말이 튀어나온다. "
    yeongwon sad"선생님,"
    yeongwon"한설이는 혹시 언제 돌아올지...아시나요...?"
    "끝까지 사고회로가 망가진 채, 반복적인 정보만을 원한다. "
    overwatch idle2"정확히는 잘 모르겠지만 말이야..."
    overwatch"나도, 빨리 만날 수 있었으면..."
    "그러나, 돌아온 것은 항상 언제와는 다른 대답. "
    "어디로 잠시 떠났다는 말은, 거짓말이구나. "
    "마지막의 말은 잘 들리지 않았지만, 한 가지 확실한 사실은, "
    "분명히 그의 얼굴에는 짙게 그림자가 드리워져 있었다는 것이다. "

label scene317:
    scene bg room2 with Dissolve(1.0)
    "기숙사 방에 들어온 동시에, 바닥에 몸이 아무렇게나 떨어진다. "
    "쓰러지는 몸이 문에 기대어져 고개가 아래로 향한다. "
    "책임감, 평정심, 통찰력, 모험심,"
    "모든 것이 떨어져 아래를 향한다. "
    "나는 언제부터 이런 무모한 짓을 시작해 왔을까."
    "매일매일을 어떤 심정으로 살아왔는지 전혀 짐작이 가지 않는다. "
    scene bg room2b with Dissolve(1.0)
    "아무것도 할 수 없다. "
    "최상층에서 웃는 모습의 한설이의 곁으로부터 도망쳤다.  "
    "나와의 약속을 굳게 지키던, 한별이의 믿음으로부터 도망쳤다. "
    "내 자신으로부터 도망쳤다. "
    with vpunch
    "눈 앞의 구깃구깃해진 옷자락과 넥타이 리본을 찢어버릴 기세로 움켜쥔다. "
    "나를 향한 한별이의 분노를 다시 한 번 상기시키기 위해서,"
    "그리고 단지 나대는 무능력자로부터의, 의미 없는 화풀이를 하기 위해서. "
    scene bg blackscreen with Dissolve(1.0)
    "죄악의 그림자가 손끝을 타고 드리운다. "
    "그림자는 순식간에 심장을 움켜쥐어 모든 것을 얽맨다. "
    "숨을 쉬기가 힘들다. "
    "마음 속에서 말소리가 들린다. "
    "\"한설이는 죽었어.\"\" 
    "\"나 때문에.\"\" 
    "..."
    "누구세요?"
    with Fade(3, color="#666666")
    "나는 어디로 가는 걸까?"
    "나는 어디에 이끌리는 걸까."
    "나는... 어디에 있는 걸까."
    scene bg hallwaydormb with Dissolve(1.0)
    "너무나 익숙한 곳, 그러나 이런 위화감은 없었다."
    "한기가 느껴진다. 나는 이런 곳을 언제 와 보았는가."
    "하지만 두리번두리번거리던 나는 소스라치게 놀랄 수 밖에 없었다."
    "어둠 속에서 떠다니는 실루엣들, "
    "창문으로 희미하게 새어나오는 뿌연 달빛,"
    "그리고 옆을 보니--"
    "한설이가 나를 보고 있었다."
    "아아, 이런 현실이 왜 나한테 다가오는 거야."
    "오만 가지 감정이 뒤섞여 나온 나의 반응은 놀랍게도 무응답이였다."
    "한설이가 나를 부르려고 하고 있다."
    "어둠 속의 실루엣들이 우리를 감싸려고 한다."
    "한설이 뒤로 누군가의 실루엣이 보인다."
    "실루엣이 나를 가리킨다."
    "손가락이 올라간다."
    "이러지 마, 안돼,"
    "내 손가락은 정확히 한설이를 가리키며--"
    #play sound "sound/gunfire.mp3"

label scene318:
    scene bg blackscreen with Dissolve(1.0)
    "무단 결석을 했다. "
    "아무도 찾아오지 않았다. "
    "걱정되기 보다는 안도감 쪽이라고 생각한다. "
    "하루에도 몇 번씩 누군가가 들어닥치는 망상에 시달린다. "
    scene bg room2b with Dissolve(1.0)
    "밖으로 나가지 않은 지 며칠이 지났을까."
    "이제는 어떻게 되어도 상관없어. "
    "억지를 부리고, 남을 멋대로 이용하고, 누군가의 발목을 부러트린 나에게는 자격이 없는 걸. "
    "머리가 어지럽고 눈앞이 희미해진다. "
    "제대로 된 것을 먹지 않은지 수 일, "
    "침대 밑의 인공배양 통조림을 향해 손을 뻗는다. "
    "그러나, 내 눈 앞에 떨어진 것은--"
    "이전에 침대 밑에 고이 모셔놓았던, 너덜너덜해진 일기장이다. "
    "\"비가 거세게 내리친다면, 우산을 펼치는 것은 바로 우리들이 될 것이다.\""
    "심장박동이 느껴질 정도로 빨라진다. "
    "페이지를 펼치는 나를 누군가가 잡아내지는 않는 걸까? "
    "손에 들린 일기장은 사람들을 잡아내기 위한 미끼가 아니였을까. "
    "영혼만은 아무도 모르는 곳으로 끌려가 있는 나는 만들어낸 허상이 아닐까.  "
    "무섭다. "
    "누군가가 날 보고 있다. "
    scene bg blackscreen with Dissolve(1.0)
    "두려워서 이불 속에 파묻혀 눈을 감는다. "
    "날 보지 말아줘. "
    "눈치채지 말아줘, "
    "내가 잘못했으니 나를 제발 용서해줘. "
    "쏟아지는 비를 그냥 맞은 탓일까. "
    "속이 쓰라려 일어날 수 없게 된다. "
    "아무 것도 일어나지 않았던 세계를 상상해본다. "
    scene bg ki1 with Dissolve(1.0) #기 회상cg사용
    "하늘이와 헤어질 일도 없고, 한설이가 실종될 일도 전부 없는."
    "아니, 이 고아원도, 우산인지 오존층인지 할 것도 없는 세계가 더 좋겠다. "
    "하지만 아무 것도 일어나지 않았을 리가 없다. "
    "그렇게 믿고 싶은 것 뿐인 단순한 망상이다. "
    "나만이라도 아무것도 일어나지 않은 것과 같은 원래대로의 일상을,"
    "그렇다면 모두를 바라보지 않고 살아갈 수 있을까. "
    scene bg blackscreen with Dissolve(1.0) 
    "어린 시절 5명의 추억을 없애버린 채로, 등을 돌린 채로 떠나가버리면 어떨까. "
    "그것은 분명, 내 자신을 부정하는 것보다 더욱 가혹할 것이다. "
    "하지만, 지금을 원래대로 돌릴 수 있는 법은 남아있을 터이다. "

label scene319:
    scene bg hallwaydormb with Dissolve(1.0) 
    "기숙사 전원이 아무도 없을 시간,"
    "마찰음을 내는 문의 소리도 신경쓰인다. "
    "초겨울의 쓸쓸한 바람을 타고 무심코 걷는다. "
    scene bg oldschoolb with Dissolve(1.0) 
    "이윽고 도달한 그곳에는 긴 그림자가 드리워져 있었다. "
    "우리들의 시작의 장소, 모든 것이 시작된 곳. "
    "그리고, 이제는 모든 것을 끝내야 할 장소. "
    scene bg skysunset with Dissolve(1.0) 
    "가장 아래쪽으로 향하는 길에 선다. "
    "어둑어둑해서 실루엣만 보이는 지하실 문을 걸어잠근다. "
    "누구도 비를 맞지 않도록, 그리고 그 누군가의 마지막 페이지를 완성할 수 있도록. "
    "기숙사의 실험 보고서는 모두 종이 조각으로 만들어 버렸다."
    scene bg oldclassroom with Dissolve(1.0) 
    "이제 남은 것은 단 하나. "
    "회벽색 톤의 교실에 뿌연 먼지가 가라앉아 있다. "
    "손에 들린 건 색깔이 바래서 무슨 색깔이였는지도 모를 노트 한 권. "
    yeongwon sad"현 씨, 미안해요."
    yeongwon"당신의 의지가 전해진 사람이 고작 나여서."
    "부서진 책상 사이에 가라앉은 틈이 보인다. "
    "저 자리에 일기장을 둔다면, 현 씨는 언젠가 이걸 가지러 올까."
    "그렇다면 이 무능력하기만한 한 소녀의 손을 거쳤다는 것을 숨길 수 있으려나. "
    "지평선 밑으로 사라지는 태양에 눈길이 간다. "
    "녹슨 창문틀과 깨어진 유리가 저녁놀에 비쳐 어렴풋이 빛난다. "
    "그래, 원래대로 돌아가면 되는 거야. "
    "이걸로 된 거야..."
    "그러나, 다시 한번 알 수 있게 되었지만--"
    "다시 풀어진 실을 감는 건 불가능하다. "
    yeongwon"???"
    "아지트 로비로부터의 발소리가 정적을 깬다. "
    "급히 몸을 숨기고 창문을 주시한다. "
    "얼마 안되는 빛을 머금은 은빛 머리칼의 소년, "
    "그리고 그보다 반 발짝 앞서 걷는, 기분나쁠 정도로 순백의 긴 가운을 입은 여자. "
        show principal idleb at right with dissolve
        show haneul sadb at left with dissolve
    "하늘과, 원장이다. "
    "왜 저 두사람이 여기에, 라고 생각하기 전에 자동반사적으로 손끝이 파르르 떨린다. "
    "하늘이가 안전하다는 안도감의 몇십 배, 원장으로부터의 공포심이 분위기를 압도한다. "
        hide principal with dissolve
        hide haneul with dissolve                                                                      
    "동요하고 있다."
    "긴장하지 마, 영원. 자주 있던 일이잖아. "
    "잠시를 고민하던 나는-"
    "그 자리에 숨기로 하였다. "
    "지금 나간다면 더욱 수상하게 보일 뿐이다. "
    "가만히 숨을 죽이고 귀를 기울인다. "
    "이러한 상황을 두려워하였지만, 막상 상황에 맞닥들이니 마음이 이상하게만치 편안해졌다. "
        show principal idle with dissolve                                   
    principal"이제 마지막 단계만 남았구나, 하늘아. "
    principal"오늘이 무사히 지나간다면, 우리들의 세계는 큰 도약을 맺을 수 있겠지."
    principal"지금까지 수고했어. "
    "원장은 무슨 말을 하고 있는 거지? "
    "하늘이는 아무 말이 없다. "
    principal happy"실전 테스트라고 이야기했지만, 사실 별 건 없다고 생각하면 좋아. "
    principal"여기에 와보는 건 처음이지? "
    principal"별 것 없어. 그냥 예전에 쓰던 교실이였을 뿐이니까. "
    "터벅터벅 발소리가 조용한 구교사를 울린다. "
        hide principal with dissolve                                   
    "발소리는 점점 멀어지며, 이내 문의 자물쇠를 푸는 소리가 들린다."
    "숨 죽인채 상황을 지켜보는 나를 뒤로하고 문은 열린다. "
    "저게 움직이는 것을 본 건 지금이 처음이다. "
    "문 뒤로 사라지는 둘과 함께 통로에서 빛이 사라진다. "
    "이제 더 이상 보는 사람이 없을거야. "
    "제자리에 일기장을 돌려놓고, 돌아가면 되는 거겠지?"
    "나는, 그러나--"
    with vpunch
    scene bg blackscreen with Dissolve(1.0) 
    "닫히는 문을 잡아열어, 계단 안쪽으로 들어갔다. "
    "아무리 구제불능인 나라도, 모두를 다 지켜내지 못한 나라도, "
    "하늘이, 너만은 내가 지켜낼거야. "
    "원장이 빼앗아 가도록 두지 않을거야. "
    "그렇게 결심한 뒤, 천천히 어둠 속의 빛으로 첫 발짝을 내딛는다. "
    with Fade(3, color="#666666")

label scene320:
    scene bg blackscreen with Dissolve(1.0)         
    "계단은 꽤나 아래쪽까지 이어져 있었다. "
    "제대로 먹지도 걸어다니지도 않은 탓에 몇 번이나 허공에 발을 디딜 뻔 했다. "
    scene bg hallwaydark with Dissolve(1.0) 
    "그리고 도착한 이곳은 어두컴컴한 구교사 창고 앞."
    "이어져 있는 둔탁한 철문의 실루엣이 엷은 빛에 어른거린다. "
    principal happy"겁 먹을 필요는 없어, 지금까지 많은 시련을 이겨냈잖아?"
    principal"오래 걸리지는 않을 거야.."
    "이런 곳에 최신식 생체인증 시스템이라니, 역시 수상하다. "
        hide principal with dissolve                                   
    "철문은 눈이 부실때까지 열리고, 천천히 닫힌다. "
    "문의 틈새로 발을 내딛는다. "
    with Fade(3, color="#FFFFFF")
    scene bg lab with Dissolve(1.0)         
    "그리고, 깨닫는다. "
    "이곳에 들어온 것이 사활을 건 모험이였다는 것을. "
    "괴리적일만큼 미래적인 공간이 시야를 감싼다. "
    "정황상 실험실인 것이 명백한 상황. "
    "탁 트인 공간에 눈이 부셔 재빨리 선반 사이로 몸을 피한다. "
    "빛이 덜 드는 곳을 찾아 숨을 돌린다. "
    "이런 곳이 있다는 것, 여기서 무엇을 한다는 것 자체가 상식을 뛰어넘는 아이러니가 아닌가. "
    "정갈한 철재 뒤에 커다란 박스와 장비들이 숨겨져 있다. "
        show principal idleb at right with dissolve
        show haneul sadb at left with dissolve
    principal"여기서 몇 개의 문장을 소리내서 읽을 거야, "
    principal"저번에 했던 실험이랑 큰 차이는 없지만 내용이 약간 다를 테니까. "
    principal"자세한 건 이 안쪽에 쓰여진 걸 참고하렴, 그럼."
    "의미를 알 수 없는 정체불명이다. "
    "모두들을 가두어놓고 저런 정신병자 같은 실험이나 하고 있는걸까?"
    "하늘이는 원장이 있는 곳으로, 한 발짝 더 다가간다. "
    "장비와 박스 때문에 잘 보이지 않는다. "
        hide principal with dissolve  
        hide haneul with dissolve                                 
    "그러나 하늘이는 투명한 유리상자 안에 들어가 완전히 시야 밖을 벗어났다. "
    "이윽고 내 초점이 방해하는 물건들로 맞추어졌다. "
    scene bg labb with Dissolve(1.0)         
    "반투명의 플라스틱 상자에 담긴 수많은 주사기들. "
    "포화 산화수소 용액..?"
    "U-235...차폐막 무력화용...?"
    "듣도 보도 못한 것이다. "
    "원장의 테이블에 있는 것은, 같은 모양의 상자들. "
    "커다란 쇳덩이가 검은색의 벽을 이루고 투명한 주사기가 푸른 빛을 내뿜는다. "
    scene bg lab with Dissolve(1.0)
        show principal idleb with dissolve         
    principal"그럼 첫번째 데이터 분석을 시작할게, 하늘. "
    "보통 위험한 곳이 아닌 것 같다. "
    "여기서 하늘이를 지킨다던가 살린다던가 하는게 가능한 것일까. "
    principal happy2"그리고, 그 전에..."
        hide principal with dissolve
    "아, 꺼졌다.  "
    "이것도 실험인 걸까. "
    "뭐가 잘못된 걸까. "
    "기분 나쁜 정적이다. "
    "기분 나쁜 정적이 깨진다. "
    with pause(2.0)
        show principal happy2
    principal"우리 반장 친구, 왜 여기 있을까?"
    "불이 켜진다. "
    "뭐가 잘못된 걸까."
    "아아, 자포자기다--"
        hide principal with dissolve
    "선반 쪽을 돌아 문 쪽으로 달린다. "
    "거리로 생각하면 내가 더 가까워...!"
    "라고 생각하던 순간. "
    "털썩, 하고 다리에 힘이 빠졌다. "
    with vpunch
        show principal happy2 with dissolve
    principal"컨디션 불량이라더니, 이런 데는 어떻게 온 거야?"
    "흰 가운의 그림자가 점점 나를 앗아간다. "
    "위에서 올려다보는 그녀의 모습은 마치 죽음의 천사."
    "가운 주머니에 꽃힌 무수한 주사바늘이 반짝인다. "
    yeongwon serious"하늘이를...하늘이한테 도대체 뭘 하려는 거야...!"
    yeongwon"한설이를, 연우를..."
    yeongwon"그리고 하늘이마저...  "
    "넘어진 나에게, 원장의 얼굴이 가까워져온다. "
    with vpunch
    principal"아무것도 하지 않았어."
    principal"왜냐면 모든 게 다 괜찮아 질거거든. "
    "공포심에 뒷걸음치려고 안간힘을 쓴다. "
    "옷 사이로 툭 하고, 무언가가 떨어진다. "
    "원래 자리로 돌아가는 것을 잊어버린 그의 유산. "
    "일기장이 나에게 속삭인다. "
    "결국 당신의 여정은 여기까지군요. "
    "그러나, "
    principal shock"......!"
    "원장은 더이상 가까워져오지 않았다. "
    "대신, 무언가에 홀린 듯, 너덜너덜한 종이 뭉치를 바라보고 있었다. "
    "도대체 어떻게 된 사람인 걸까."
    "원장도 이 일기장에 대해서 알고 있는걸까."
    "일단 여기서 빠져갈 수 있는 상황을 만들어야 한다."
    principal"멈춰."
    principal"어차피 도망쳐봤자 문은 닫혀 있으니까."
    "한 박자를 추스른 원장은, 나를 똑바로 쳐다보고 말했다. "
    principal cry"이 노트, 누구 건지 너는 아니? "
    "...뭐라고..?"
    "어디에서 주웠냐는 질문이 아니라, 그런 질문을 한다고?"
    "그 말을 신호로, 핑 하는 신호가 머리를 울렸다. "
    yeongwon"...이전부터, 알고 있지 않았나요."
    show principal sentimental
    "이것은, 원장한테 거는, "
    yeongwon"제가 누구고, 뭘 해왔고,"
    yeongwon"왜 여기에 있는지 말이에요. "
    "내 인생 최대의 내기. "
    yeongwon"안 그런가요?"
    yeongwon"연 씨."

label scene321:
    scene bg sky with Dissolve(1.0)         
    "이 이야기는, 한 소년과 소녀의 이야기. "
    "소녀는 언제나 몸이 약해, 언제나 방 안에 갇혀 있었다. "
    "그러나, 그 소녀에게 한 소년이 찾아왔다. "
    "소년이 동경한 것은 바깥 세계. "
    "소년은 소녀를 이끌고, 밖의 세계를 탐험했다. "
    scene bg oldschool with Dissolve(1.0)         
    shonen"어때, 밖으로 나오니 좋지? "
    shojo"우와..."
    shojo"모든 게 다 신기해..."
    shonen"내가 나중에 더 자란다면..."
    shonen"저 유리창 밖을 나가, 뛰어다니고 싶은걸."
    shojo"정말 대단해...!"
    scene bg sky with Dissolve(1.0)         
    "그러나 소녀는 소년 없이는, 밖에 나갈 수 없었다. "
    "그 대신 소녀가 가까이 한 것은, 책이였다. "
    "말과 문장이 겹쳐지며 방 안에서도 광활한 밖을 그려내는 마법. "
    "소녀는 소년에게 책을 읽어주며 책의 아름다움을 전했다. "
    "이렇게 소년소녀는 여러 세계를 경험하며, 성숙해져 나간다. "
    "그러나 어른들은 그들에게 뛰어놀 공간을 주지 않았다. "
    "시간이 지나 강제적으로 떨어지게 된 그들. "
    "그러나 바깥을 동경하는 소년소녀는, 언제나 새장에 만족하지 않는다. "
    scene bg jeon3_1 with Dissolve(1.0)         
    "어른의 눈을 피해, 그들은 계속 함께한다. "
    "소녀가 들고 온 책을 읽거나, 소년을 같이 따라다니는 일상의 연속."
    "그러나 그 일상은 오래 지속될 수 없었다. "
    "지속되는 건강 악화로 인해 자유로워지지 못한 소녀, "
    "그녀를 기다리는 건, 소년이였다. "
    "어느 날, 오랫만에 소녀를 만난 소년은 이야기를 건넨다. "
    shonen"이 세계에서 우리는, 왜 자유롭지 못한 걸까? "
    shojo"......"
    shojo"예전의 세계는, 모든 것이 다 신기해 보였지. "
    shonen"어릴 적에는, 우리가 자유롭고 모든 걸 할 수 있다고 생각했어. "
    shonen"마치 책 속의 세계처럼. "
    shonen"하지만 그게 아닌 걸 깨닳은 건, 나한텐 너무 슬픈 일이였어. "
    "소녀를 보고, 소년은 자유를 깨우친다. "
    "원없이 뛰어다니고 하늘을 날아다닐 수 있는 자유. "
    "그러나, 소년은 자유를 빼앗긴 쓰라림을 느끼고 있다. "
    "그리고 생각한다. "
    "우리들만의 자유를 지켜나가면, 빼앗길 일도 없을 것이라고. "
    shojo"책을 써 본다면, 어떨까? "
    shonen"내가...그런 게 가능할까? "
    shojo"물론, 가능하고말고. "
    "우리들이 원없이 뛰놀수 있도록, "
    "방해하는 것을 생각해내고, 하고 싶은 걸 적어나가자. "
    "책을 쓴다면, 우리가 원하는 걸 얻을 수 있을 거야. "
    shojo"마치, 우산을 쓰면, 햇볕을 막을 수 있듯이. "
    scene bg sky with Dissolve(1.0)         
    "그렇게, 소년의 첫 책은 희망차게 시작을 알렸다. "
    "우리들만의 자유의 상징. 우산과 함께. "
    shonen"아, 여기에 네 이름을 바로 적는 건 좀 그렇지 않아? "
    shojo"내가 등장인물인 거야? "
    shojo"나를 등장시키고 싶다면, 이름은 '연' 으로 했으면 좋겠는걸. "
    shonen"...왜?"
    shojo"딱히, 아무 의미도 없어. "
    shojo"지금은... 말이지."

label scene322:
    scene bg blackscreen with Dissolve(1.0)         
    "그 이후, 거짓말같이 일이 흘러가기 시작했다. "
    "나는 아무런 처벌이나 징계를 받지 않고, 바로 구교사로부터 기숙사로 보내졌다. "
    "물론, 구교사에서 보았던 모든 것들에 대해 아무에게도 말하지 않는 조건이 붙었다. "
    "하늘이의 안전을 걸고, 약속했다. "
    "그 전에 대담하게도, 내 쪽에서도 한 가지 조건을 걸었다. "
    scene bg labb with Dissolve(1.0)         
    yeongwon serious"한설이가 어디 갔는지, 지금은 무엇을 하고 있는지..."
    yeongwon"확실하게 듣고 싶습니다."
    "한설이에 관해서는, 제대로 이야기를 들을 수 있도록. "
    yeongwon"또... 한별이에게 이 사실을 제대로 알려줬으면, 좋겠습니다. "
    "그리고 누구보다도 진실을 알고 싶은 사람에게, 잘 전달될 수 있도록."
        show principal sentimental2 with dissolve
    principal"안 그래도 이렇게 된 이상, 내 쪽에서 부르려고 했는데 말이야. "
    principal"같이 온다면, 상관없겠지. "
    scene bg skydark with Dissolve(1.0)         
    "기한은 단 하루. "
    "길고도 긴 오늘에도 벌써 짙은 어둠이 깔렸다. "
    "그날 이후, 한설이와 대화는 커녕 얼굴을 본적조차 없었다. "
    "내가 무단 결석을 해서 걱정해주고 있을까?"
    "아니면 오히려 겁쟁이같이 기숙사에 숨어 있는 나에게, 더욱 분노하고 있는 것은 아닐까. "
    "이제 곧 시간이 다가온다. "
    scene bg hallwaydormb with Dissolve(1.0)         
    "한별이의 기숙사 방문쪽으로, 서서히 다가간다. "
    "내가 아는 한별이가 맞다면, 지금 그녀는 방 안에 없다. "
    "항상 이 시간에 기숙사의 어딘가로 사라져 버리는 건 왜일까. "
    "초점 없는 눈빛을 하늘에 맞추며, 바람을 쐬러 가는 거일 지도 모른다. "
    "철두철미한 한별이의 루틴이라면, 곧 같은 시간에 돌아올 것이다. "
    "그때까지, 기다린다. "
    "......"
    "오늘은, 평소보다 더 늦게 돌아오는 것 같다. "
    "단순히 내가 시간 감각이 없어진 건지도 모른다. "
    "그 때, 나타난 건 복도 끝으로부터 다가오는 작은 체구의 실루엣이였다. "
    "너풀거리는 원복에 긴 생머리는, 틀림없는 한별이였다. "
    "마지막으로 본 것보다 훨씬 더 야위어 있는 것 같았다. "
    "한 발짝 더 앞으로 다가간다. "
    "그리고 한 발짝, 앞으로 한 발짝만 더..."
    yeongwon sad"하...한별아."
    "누군가와 대화를 했던 게 너무 오랫만이였기 때문일까. "
    "입 안에서 말이 헛나오는 느낌이다. "
    "한별이는 동요하지 않고, 나를 무시해 지나치려고 하는 것 같다. "
    yeongwon"네가 꼭 들어줬으면 하는 이야기가...있어."
    yeongwon"한설이가, 어디에 있는지..."
        show hanbyeol fury with dissolve
    hanbyeol"그 이름..."
    hanbyeol"함부로 부르지 마..."
    "감히 눈을 마주칠 수가 없다. "
    yeongwon"......"
    yeongwon"원장이, 우리들과 이야기하고 싶다고 해. "
    "문을 열고 나를 지나치려는 한별이의 발소리가 뚝 하고 끊긴다. "
    "약간은 고개를 내 쪽을 향하고, 그러나 나를 바라보지는 않고, "
    hanbyeol"여기선, 더 이야기를 못하겠네. "
    hanbyeol"일단, 방으로 들어와..."
    "조용히, 우리들을 간직한 문이 다시 열렸다. "

label scene323:
    scene bg roomb with Dissolve(1.0)         
    "한별이의 방은, 여러모로 많이 달라져 있었다. "
    "정리정돈을 깔끔하게 하는 한별이라고는 생각할 수 없을 정도로, "
    "이전보다 방이 아주 더러워져 있었다. "
        show hanbyeol sad with dissolve
    hanbyeol"다시 한번만 이야기해 줄래."
    hanbyeol"한설이에 관한, 그 내용. "
    "창문을 향하고 있던 한별이의 몸이, 곧 정면으로 나와 마주본다. "
    "힘겹게 나를 바라보는 그녀의 눈동자. "
    "한별이의 눈을 맞추기까지, 이렇게 용기가 필요했던 건 처음이다. "
    "그러나, 언제까지고 이런 관계를 유지할 수는 없다. "
    yeongwon sad"원장이 우리한테 한설이에 대해 이야기해주려고 한대. "
    yeongwon"너도 꼭 들어줬으면 한다고. "
    "그러나 중요한 것은 이게 아니다. "
        hide hanbyeol with dissolve
    yeongwon"하지만, 한설이 이야기를 하기 전에, 이 이야기를 들어 줘. "
    "한 발짝 다가가서, "
    yeongwon"그날 있었던 일은, 모든 게 내 탓이야. "
    "친구로서의 최대의 예의를 담아, 정중히 고개를 숙인다. "
    yeongwon"내가 잘못했어, 한별아. "
    yeongwon"혼자 뛰쳐나가질 않나, 못 하겠다고 약한 소리를 하질 않나..."
    "분명히 한별이는 한설이가 어디 있느냐를 듣고 싶었을 터. "
    "영 다른 말을 하는 내가 못마땅할 수도 있을 것이다. "
    yeongwon"내가 책임을 끝까지 질테니까, 끝까지 찾아낼 거니까. "
    "그러니... 사과하고 싶어. "
    "하지만, 이 이야기를 꼭 해주고 싶었다. "
    "한별이는 아무 말도 없는 채, 나만을 응시하고 있었다. "
    yeongwon"우리들, 다시 예전처럼 돌아가자. "
    "산산조각난 우정의 파편을 다시 주워담는다. "
    "다시 한 발짝, 한별이에게 다가간다. "
    yeongwon"지금까지 담아왔던 모든 기분, 모든 감정, "
    yeongwon"전부, 한 데에 담아 나를 때려. "
    yeongwon"그리고, 이제는 새로운 출발인 거야.."
    "조용히 고개를 숙이고, 눈을 감는다. "
    "우리들은, 서로 다시 이루어나갈 수 있을까. "
    "하나의 목표를 보며, 예전처럼 다시 나아갈 수 있을까. "
    "이윽고, "
    with vpunch
    "충격이 느껴졌다. "
    "하지만 얼얼한 충격이 아닌, 매우 따뜻하고 푹신한 충격. "
    "눈을 뜬다. "
    "한별이는, 내 앞에 서 있는 대신에- "
    "내게 다가와, 나를 껴안고 있었다. "
    yeongwon"......"
        show hanbyeol serious2 with dissolve
    hanbyeol"때리다니... 내가 널 때릴 수 있다고 생각해..?"
    hanbyeol"웃기지 마..."
    hanbyeol sad2"무리하게 움직이자고 한 것도... 매번 불안해하고 초조해했던 것도..."
    hanbyeol"애초에 먼저 너한테, 그렇게 심한 짓을 한 것도 나인데..."
    hanbyeol"너한테 그런 심한 짓을 할 수 있을 리가 없잖아... "
    "아아. "
    "다리에 힘이 풀린다."
    "모든 마음의 벽이 무너진다. "
    hanbyeol"미안해...정말 미안해..."
    hanbyeol"그리고...다시 나에게 돌아와 줘서 너무 고마워..."
    yeongwon sad"으으.."
    "눈앞에 있는 작은 한별이의 어께가 흐려진다. "
    "마지막으로, 마음의 문을 걸어잠그던 제방이 터져나온다. "
    yeongwon"으으....윽...으아아아아아아앙..."
    scene bg blackscreen with Dissolve(1.0)         
    "너나 할 것 없이 눈물을 흘린다. "
    "비가 세차게 내린 뒤에는, 땅이 굳어진다. "
    "그래. 이걸로 된 거야. "
    "우리는 다시, 마지막을 향한 여행길에 오른다. "

label scene324:
    scene bg sky with Dissolve(1.0)         
    "이 이야기는, 이미 커버린 소년과 소녀의 이야기. "
    "성실하고 총명한 소녀는 반장이 되었지만, "
    "항상 수업에 나오지도 않는 소년은 문제아가 되어 버렸다. "
    "그러나 그 둘의 어릴 적으로부터의 관계는 변함이 없어, "
    "시간이 지날수록 그들의 사이는 더욱 깊어진다. "
    scene bg jeon3_1 with Dissolve(1.0)         
    shonen"책이란 것을 단순히 쓰기만 한다는 거는, 너무 지루해. "
    shojo"하지만, 그건 이젠 이루어질수 없는 상상인걸. "
    shojo"이제는 우리들에게 주어진 것으로, 우리들만의 미래를 만들어갈 뿐. "
    "자유란 것이 있어도, 그건 책 안에서의 이야기일 뿐. "
    shonen"하지만, 우리들이 책의 주인공이 된다면 어떨까? "
    "그러나 어디까지나 상상이였던 이야기를 현실로 끌고 오는 것."
    "이 중에 누구도, 진지하게 생각하지 않았던 것. "
    scene bg sky with Dissolve(1.0)         
    "소년은, 언제나 자유를 동경해온 것이다."
    "소년의 책에 내용이 써내려가진다.  "
    "언제라도 타오를것만 같은, 자유의 불꽃. "
    "그러나, 소녀의 책에는 더이상 자유라는 글자는 없었다. "
    "이미 빛이 바래, 흐려진 잉크처럼 지워져버린 글자. "
    "소년소녀는 엇갈린다. "
    "소년의 책에 소녀는 점점 자취를 감춘다. "
    "그리고, 결정적인 사건이 발생한다. "
    scene bg classroom with Dissolve(1.0)         
    mstudent"저...저게 무슨 일이야?!"
    fstudent"빨리 선생님 불러와!!"
    "모두를 구속으로부터 해방시키겠다는, 감히 소설의 주인공과 같은 소년의 마음. "
    "그러나, 그 생각은 반대로 모두를 재앙으로 이끌었다. "
    scene bg jeon3_2 with Dissolve(1.0)         
    "출입 시스템을 열어버리겠다고 생각했던 소년은, "
    "감히 아무도 건드리지 못한 차폐막에 손을 대버리고 말았다. "
    "하늘에 구멍이 뚫렸다. "
    "내리쬐는 햇빛은, 그대로 소녀에게 쏟아졌다. "
    "그 이후, 아무도 소년을 본 적은 없다. "
    "소년소녀가 살던 터는, 폐허가 되어 버렸다. "
    "소녀가 처음으로 본, 자유를 갈망하던 자의 최후. "
    "햇빛이 내리쬐지 않는다고 해도, 우산 따위로는 막을 수 없어. "
    "자유라는 글자는, 소녀의 마음속에서 영원히 지워져 버린 걸까. "
    scene bg jeon3_3 with Dissolve(1.0)         
    "소녀는 반장을 뛰어넘어, 계단을 올라간다. "
    "이미 어딘가로 떠나버린 소년을 생각하며. "
    "그리움의 빈자리를 다른 것으로 채우기 위해. "
    "이윽고, 어른이 된 소녀는-"
    "소년에 관한 이야기가 나오면 이렇게 이야기한다."
    shojo"하지만, 나는 그가,"
    shojo"정말로 싫은걸. "
    scene bg blackscreen with Dissolve(1.0)         
    "마음에도 없는 이야기를 하는 건, 모든 상처받은 이들의 공통."
    "소녀의 마음은, 언젠가부터 부서져 있었다. " 
