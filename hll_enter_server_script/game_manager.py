import time
import win32gui
import os
import pyautogui
import win32com.client
import sys

import constants as cons


def game_window_hwnd(game_title):
    """检查游戏窗口是否存在"""

    hwnd = win32gui.FindWindow(None, game_title)
    if hwnd == 0:
        return None
    else:
        return hwnd


def find_steam_shortcut():
    """返回Steam快捷方式的绝对路径"""

    found_path = [
        os.path.join(os.environ['USERPROFILE'], 'Desktop', 'Steam.lnk'),
        r'C:\Users\Public\Desktop\Steam.lnk',
        r'C:\Steam.lnk'
    ]

    if os.path.exists(found_path[0]):
        return found_path[0]
    elif os.path.exists(found_path[1]):
        return found_path[1]
    elif os.path.exists(found_path[2]):
        return found_path[2]
    else:
        print('未找到\'Steam.lnk\'!')
        os.system('PAUSE')
        sys.exit(1)


def open_game(appid, address, game_title):
    """打开游戏并连接到指定服务器"""

    steam_shortcut_path = find_steam_shortcut()

    print('Open game...')
    os.system(f"\"{steam_shortcut_path}\" -applaunch {appid} +connect {address}")
    print(f"Steam shortcut path: {steam_shortcut_path}, address: {address}")

    for _ in range(0, 120):  # 10分钟
        print('#', end='')
        time.sleep(5)
        if game_window_hwnd(game_title) is not None:
            print('Game is Opened.')
            return True

    return False  # 命令发出10分钟后未检测到游戏窗口


def check_process_exists(process_name):
    """检查指定进程是否存在"""
    try:
        wmi = win32com.client.GetObject("winmgmts:")
        processes = wmi.InstancesOf("Win32_Process")

        for process in processes:
            if process.Name == process_name:
                return True

        return False

    except Exception as e:
        print(f"检查进程时出错: {e}")
        os.system('PAUSE')
        sys.exit(1)


def close_game(process_name):
    """关闭游戏"""

    os.system(f"taskkill /IM {process_name}")

    print('Wait 40s for taskkill...')
    time.sleep(40)

def pass_any_key_screen(time_limit=600):
    """
    跳过按任意键继续界面
        :time_limit: 最大时间限制(seconds)
    """

    hwnd = game_window_hwnd(cons.GAME_WINDOW_TITLE)
    for i in range(0, int(time_limit/5)):             # 超过时间限制则跳出循环
        win32gui.SetForegroundWindow(hwnd)
        pyautogui.press('a')
        print('#', end='')
        time.sleep(5)
        # 此处添加：识别到进服成功则... && 识别到异常情况处理...

    def pass_any_key_screen_v2(time_limit=600):
        """
        跳过按任意键继续界面，使用模板匹配识别游戏状态
        :param time_limit: 最大时间限制(seconds)
        :return:
        """

        hwnd = game_window_hwnd(cons.GAME_WINDOW_TITLE)
        for i in range(0, int(time_limit / 5)):  # 超过时间限制则跳出循环
            win32gui.SetForegroundWindow(hwnd)
            pyautogui.press('a')
            print('#', end='')
            time.sleep(5)
            # 此处添加：识别到进服成功则... && 识别到异常情况处理...

