# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define u = Character("???")
define m = Character("minqwq")
define mo = Character("Mio")
define s = Character("Safari")


# 游戏在此开始。
label splashscreen:
    $ renpy.movie_cutscene("startup.mp4")
    return

label start:
    stop music fadeout 3.0
    scene space_hl2

    u "今天没有太阳...不过，该醒了，minqwq。"
    u "...你的生活将从此开始。"
    "minimalmio@localhost ~ > elworld @gensokyo start"

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为 bg room.png 或 bg room.jpg）来显示。

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。

    # show mio_p22.png

    # 此处显示各行对话。
    #
    # 播放神秘小音乐
    scene extreme_hill_afternoon

    play music hmforest

    with fade
    u "抱歉----麻烦能打扰一下吗？"
    "我听到一个可爱的声音叫住了我。"
    show mio p22
    with moveinright
    u "厕...厕所在哪里？"
    m "这条路前面有个分岔路口，你左转应该就能看到了。"
    hide mio
    with moveoutleft
    u "(快速离开"
    "这座山是我们这为数不多的景点"
    "但是风景非常优美"
    "常常会吸引许多人来此地旅游"
    show mio p22
    with moveinright
    u "抱歉，我还是没找到，能带我去吗？"
    m "...好吧。"
    hide mio
    with dissolve
    "(好恐惧...我是个社恐啊...)"
    show mio p22
    with dissolve
    m "好了，就是这里"
    u "谢谢~"
    hide mio
    with moveoutleft
    "她走进了厕所。"
    "我也快速离开了"

    # 此处跳转至第二章
    jump c1s2
label c1s2:
    with fade
    show min p7
    m "唔~起床了"
    "今天是去新学校报道的第一天，我可不能迟到。"
    show min p1
    m "(出门前的神秘准备工作"
    hide min
    with dissolve
    m "(离开"
    "少女走路中...(按下 Enter 键以前进。"
    show min p1
    "来到教室，这里熙熙攘攘的，坐满了新同学"
    "我用着视线瞟着新同学们"
    "突然，我的视线落在一个女孩身上。"
    u "......"
    show min p11
    with vpunch
    "这不是昨天的那个女生吗？"
    show min p3
    m "...hi?"
    "我向她打了个招呼"
    show mio p16
    u "....你好"
    "她略带羞涩地回应了我"
    m "我去，好巧啊，你也开始在这上学了？"
    show mio p22
    u "...是。"
    "那，你叫什么"
    # show mio p20
    mo "...我...我的名字是Yukari..."
    "她的脸染上了红晕，扭捏着"
    m "很高兴认识你！我的名字是minqwq，平常直接叫我min就行。"
    show min p11
    show mio p25
    "随后，上课铃响起了。"
    "我们俩随后立即摆正坐姿"
    hide all
    "少女上课中..."
    with fade
    "转眼见外面的太阳都快要落下去了。"
    m "再见"
    show mio p12
    mo "再见~！"
    hide mio
    "我们俩就这么告了别，随后我打算去咖啡厅喝杯咖啡"
    m "(出门"
    show min p5
    m "虽然走夜路很害怕，但是还是想要去喝一杯咖啡再回家啊..."
    "于是我还是打算去来一杯咖啡。"
    "少女黑夜行走中..."
    with fade
    show min p8
    m "终于到地方了..."
    m "(推门"
    show min p2
    m "老板...?"
    show saf p12
    s "min...?"
    m "你怎么穷的都来打工了("
    show saf p0
    s "不是啦，其实就是想整点小钱买台手机而已"
    m "所以"
    m "来一杯多糖咖啡"
    show saf p10
    s "好"
    "制咖啡中..."
    with fade
    s "好了"
    "(拿"
    show min p13 and saf p10
    snm "(微笑"
    hide saf
    show min p9
    "(闻"
    show min p11
    m "不赖啊"
    show min p11 and saf p4
    s "那肯定，上一任老板亲自教我的"
    hide all
    "(坐在店铺的某个角落里开始饮用"
    "少女饮咖中..."
    with fade
    show min p13
    m "那我先走了，明天虽然不上学但是有代码没写"
    show min p13 and saf p10
    s "好~"
    show saf p5
    "现在处于 Another View 状态"
    s "又无聊了..."
    hide saf
    "现在处于 Player View 状态"
    show min p8
    m "...累死了。"
    m "可算到家了"
    hide min
    m "(飞上床"
    m "(闭眼"
    return
