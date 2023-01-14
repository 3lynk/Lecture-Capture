import pyautogui
import customtkinter
import tkinter
import tkinter.messagebox
import time
import os
import keyboard
from PIL import Image
from tqdm import tqdm
from pynput import mouse

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.xy = []
        self.adress = ""
        self.number = 1
        keyboard.add_hotkey("ctrl+c+a", self.capture)

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

        # adress textbox
        self.save_adress = customtkinter.CTkEntry(self, placeholder_text="Save Adress")
        self.save_adress.grid(row=0, column=1, columnspan=2, padx=20, pady=10, sticky="nsew")

        # name textbox
        self.name_textbox = customtkinter.CTkEntry(self, placeholder_text="File Name")
        self.name_textbox.grid(row=1, column=1, columnspan=2, padx=20, pady=10, sticky="nsew")

        # xy button
        self.xy_button = customtkinter.CTkButton(self, text="XY setting", command=self.xy_setting)
        self.xy_button.grid(row=2, column=1, padx=20, pady=10)

        # start button
        self.start_button = customtkinter.CTkButton(self, text="Start", command=self.start)
        self.start_button.grid(row=2, column=2, padx=20, pady=10)

        # capture button
        self.capture_button = customtkinter.CTkButton(self, text="Capture", command=self.capture)
        self.capture_button.grid(row=3, column=1, padx=20, pady=10)

        # end button
        self.end_button = customtkinter.CTkButton(self, text="End", command=self.end)
        self.end_button.grid(row=3, column=2, padx=20, pady=10)

    # Info Messagebox
    def info_msgbox(self, text):
        tkinter.messagebox.showinfo('Info', text)

    # Warning Messagebox
    def warning_msgbox(self, text):
        tkinter.messagebox.showwarning('Warning', text)
    
    def start(self):
        try:
            self.adress = self.save_adress.get() + self.name_textbox.get()
            os.mkdir(self.adress)
            self.number = 1
            
            self.info_msgbox("Start")
        except FileExistsError:
            self.warning_msgbox("이미 존재하는 폴더 이름입니다.\n경로를 수정하거나 이름을 수정해주세요.")
    
    def end(self):
        self.file_list = os.listdir(self.adress)
        self.img_list = []

        for i in tqdm(self.file_list):
            self.img = Image.open(self.adress + "\\" + str(i))
            self.img = self.img.convert("RGB")
            self.img_list.append(self.img)

        self.img = Image.open(self.adress + "\\" + str(self.file_list[0])).convert("RGB")
        del self.img_list[0]
        self.img.save(self.adress + "\\" + self.name_textbox.get() + ".pdf", save_all=True, append_images=self.img_list)

        self.info_msgbox("Success")
        os.startfile(self.adress)

    def capture(self):
        screenshot = pyautogui.screenshot(region=(self.xy[0][0], self.xy[0][1], self.xy[1][0] - self.xy[0][0], self.xy[1][1] - self.xy[0][1]))
        screenshot.save(self.adress + "/" + str(self.number) + ".jpg")
        self.number += 1

    def click(self, x, y, button, pressed):
        if pressed:
            x = int(x)
            y = int(y)
            self.xy.append([x, y])
            if len(self.xy) == 2:
                print(self.xy)
                return False
    
    def xy_setting(self):
        self.xy = []
        with mouse.Listener(on_click = self.click) as listener:
            listener.join()
        self.info_msgbox("Coordinate Setting Completed")

if __name__ == "__main__":
    customtkinter.set_appearance_mode("Dark")
    customtkinter.set_default_color_theme("blue")

    app = App()
    app.mainloop()