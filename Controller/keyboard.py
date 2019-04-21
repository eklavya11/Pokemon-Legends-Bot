import win32gui
import time
import win32con


def press_key(given_handle, key_name):
    win32gui.SendMessage(given_handle, win32con.WM_KEYDOWN, key_name)
    time.sleep(0.2)
    win32gui.SendMessage(given_handle, win32con.WM_KEYUP, key_name)


def go_left(handle):
    press_key(handle, win32con.VK_LEFT)


def go_right(handle):
    press_key(handle, win32con.VK_RIGHT)


def go_up(handle):
    press_key(handle, win32con.VK_UP)


def go_down(handle):
    press_key(handle, win32con.VK_DOWN)


def press_num(handle, num):
    press_key(handle, num + 48)


def hold_key(handle, key_name):
    win32gui.SendMessage(handle, win32con.WM_KEYDOWN, key_name)


def release_key(handle, key_name):
    win32gui.SendMessage(handle, win32con.WM_KEYUP, key_name)
