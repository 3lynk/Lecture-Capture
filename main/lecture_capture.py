import pynput
import pyautogui
import customtkinter
import tkinter
import tkinter.messagebox
import time

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # init setting
        self.title("Lecture_Caputure.py")
        self.geometry(f"{600}x{300}")

        # grid setting
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)
        
        # sidebar frame
        self.sidebar_frame = customtkinter.CTkFrame(self, width=100, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")

        # logo
        self.logo = customtkinter.CTkLabel(self.sidebar_frame, text="Lecture_Capture", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo.grid(row=0, column=0, padx=20, pady=(20, 10))

        # explain textbox
        self.text_box = customtkinter.CTkTextbox(self.sidebar_frame)
        self.text_box.grid(row=1, column=0, padx=20, pady=20)

        self.text_box.insert("0.0", "How to use\n")
        self.text_box.configure(state="disabled")

        # link text
        self.save_adress = customtkinter.CTkEntry(self, placeholder_text="Save Adress")
        self.save_adress.grid(row=0, column=1, padx=20, pady=10)

        # name textbox
        self.name_textbox = customtkinter.CTkEntry(self, placeholder_text="File Name")
        self.name_textbox.grid(row=1, column=1, padx=20, pady=10)

        # xy button
        self.xy_button = customtkinter.CTkButton(self, text="XY setting")
        self.xy_button.grid(row=2, column=1, padx=20, pady=10)

        # start button
        self.start_button = customtkinter.CTkButton(self, text="Start")
        self.start_button.grid(row=0, column=2, padx=20, pady=10)

        # capture button
        self.capture_button = customtkinter.CTkButton(self, text="Capture")
        self.capture_button.grid(row=1, column=2, padx=20, pady=10)

        # end button
        self.end_button = customtkinter.CTkButton(self, text="End")
        self.end_button.grid(row=2, column=2, padx=20, pady=10)

xy = []
def capture():
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

'''with pynput.mouse.Listener(on_click = click) as pynput.mouse.Listener:
    pynput.mouse.Listener.join()'''

if __name__ == "__main__":
    customtkinter.set_appearance_mode("Dark")
    customtkinter.set_default_color_theme("blue")

    app = App()
    app.mainloop()