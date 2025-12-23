import game_manager as gm
import constants as cons
import win32gui
import pyautogui
import time
import os

def read_address():
    if not os.path.exists('address.txt'):
        print('找不到address.txt!')
        return None
    with open('address.txt') as file:
        address = file.readline()
        if address == '':
            print('Address.txt为空！')
            return None
        print('目标地址：', address)
        return address

def main():

    # 读取目标地址
    target_address = read_address()
    if target_address is None:
        os.system("PAUSE")
        return 1

    # 若游戏正在运行，则将其关闭
    if gm.check_process_exists(cons.GAME_PROCESS_NAME):
        gm.close_game(cons.GAME_PROCESS_NAME)

    # 打开游戏并连接到指定服务器
    gm.open_game(cons.APPID, target_address, cons.GAME_WINDOW_TITLE)

    # 跳过‘按任意键继续’的界面
    print(r'跳过‘按任意键继续’...')
    hwnd = gm.game_window_hwnd(cons.GAME_WINDOW_TITLE)
    for i in range(0, 120):             # 10分钟后跳出循环
        win32gui.SetForegroundWindow(hwnd)
        pyautogui.press('a')
        print('#', end='')
        time.sleep(5)

    os.system("PAUSE")
    return 0


if __name__ == '__main__':
    main()