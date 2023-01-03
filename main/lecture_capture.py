import pynput
import pyautogui

xy = []
screenshot = pyautogui.screenshot()
screenshot.save("C:/Users/kimgu/OneDrive/사진/Lecture_Capture/screenshot.jpg")

def click(x, y, button, pressed):
    if pressed:
        x = int(x)
        y = int(y)
        xy.append([x, y])
        if len(xy) == 2:
            print(xy)
            return False

with pynput.mouse.Listener(on_click = click) as pynput.mouse.Listener:
    pynput.mouse.Listener.join()