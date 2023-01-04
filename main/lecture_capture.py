import pynput
import pyautogui
import customtkinter
import tkinter
import tkinter.messagebox
import time

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Lecture_Caputure.py")
        self.geometry(f"{500}x{250}")

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

if __name__ == "__main__":
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")

    app = App()
    app.mainloop()