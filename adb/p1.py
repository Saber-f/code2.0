import os

adbShell = "adb shell  {cmdStr}"


def execute(cmd):
    str = adbShell.format(cmdStr=cmd)
    print(str)
    os.system(str)


if __name__ == '__main__':
    # 点击返回按键
    os.system(" adb shell input keyevent 4 ")
    # 点击
    #execute("input tap 928 331")
    # 滑动 从  928 541  滑动到  928 331   用100毫秒
    #execute("input swipe 928 541 928 331 100")

    # 点击。 使其获得焦点
    #execute("input tap 928 331")
    # 往输入框中输入文字 。前提是输入框获得了焦点
    #execute(" input text '1111'")