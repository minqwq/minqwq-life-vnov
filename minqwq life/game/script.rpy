# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define u = Character("???")
define m = Character("minqwq")


# 游戏在此开始。

label start:

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为 bg room.png 或 bg room.jpg）来显示。

    scene bg room

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。

    # show mio_p22.png

    # 此处显示各行对话。
    #
    # 播放神秘小音乐
    play music endless_hcremix

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
    with fade
    "第一次被一个女生这样跟着，我的心嘭嘭直跳。"
    show mio p22
    with fade
    m "好了，就是这里"
    u "谢谢~"
    hide mio
    with moveoutleft
    "她走进了厕所。"
    "回家的路上，我仍然忘不了这如此甜美的声音"

    # 此处为游戏结尾。

    return
