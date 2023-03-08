#-*-coding: utf-8-*-

import customtkinter
import tkinter
import tkinter.messagebox
import tkinter.filedialog
import time
import os
import keyboard
import winsound
import setting_area
import screeninfo
import mss
from PIL import Image
from tqdm import tqdm
from pynput import mouse

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.xy = []
        self.folder = ""
        self.adress = ""
        self.number = 1
        self.screen_id = 0

        self.monitors = screeninfo.get_monitors()
        self.monitor_options = []
        for m in range(len(self.monitors)):
            if self.monitors[m].is_primary == True:
                self.monitor_options.append(f"Display{m + 1}(Main)")
            else:
                self.monitor_options.append(f"Display{m + 1}")

        keyboard.add_hotkey("alt+c", self.capture)

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
        self.logo.grid(row=0, column=0, padx=20, pady=20)

        # explain textbox
        self.text_box = customtkinter.CTkTextbox(self.sidebar_frame, height=165)
        self.text_box.grid(row=1, column=0, padx=20, pady=0)

        self.explain = 'How to use \n\n 1. File Name 입력하기 \n\n 2. folder 버튼 누르고 저장할 폴더 선택하기 \n\n 3. Start 버튼 누르기\n\n 4. XY setting 버튼 누른후 캡쳐할 영역 드래그하기 \n (세팅을 안할시 기본값인 전체화면 캡쳐) \n (드래그하는 동안 아무것도 안보이는게 정상) \n\n 5. Capture버튼을 클릭하거나 단축키 "alt + c"로 캡쳐하기(단축키를 사용할 때에는 다른 단축키가 작동될 수 있기 때문에 작업 표시줄 클릭 후 사용하길 권장) \n\n 6. 캡쳐가 다 끝난 후 End 버튼을 눌러 완성하기'
        self.text_box.insert("0.0", self.explain)
        self.text_box.configure(state="disabled")

        # monitor option
        self.monitor_option = customtkinter.CTkOptionMenu(self.sidebar_frame, width=200, values=self.monitor_options, command=self.monitor_select)
        self.monitor_option.grid(row=2, column=0, padx=20, pady=20)

        # name textbox
        self.name_textbox = customtkinter.CTkEntry(self, placeholder_text="File Name")
        self.name_textbox.grid(row=0, column=1, columnspan=2, padx=20, pady=10, sticky="nsew")

        # start button
        self.start_button = customtkinter.CTkButton(self, text="Start", command=self.start, fg_color="green", corner_radius=100, state="disabled")
        self.start_button.grid(row=1, column=1, padx=20, pady=10)

        # end button
        self.end_button = customtkinter.CTkButton(self, text="End", command=self.end, fg_color="green", corner_radius=100, state="disabled")
        self.end_button.grid(row=2, column=1, padx=20, pady=10)

        # capture button
        self.capture_button = customtkinter.CTkButton(self, text="Capture", command=self.capture, fg_color="#990F02", state="disabled")
        self.capture_button.grid(row=3, column=1, columnspan=2, padx=20, pady=10, sticky="nsew")

        # select folder button
        self.folder_button = customtkinter.CTkButton(self, text="Folder", command=self.select_folder, corner_radius=100, fg_color="#5AA1C2")
        self.folder_button.grid(row=1, column=2, padx=20, pady=10)

        # xy button
        self.xy_button = customtkinter.CTkButton(self, text="XY setting", command=self.xy_setting, corner_radius=100, fg_color="#5AA1C2", state="disabled")
        self.xy_button.grid(row=2, column=2, padx=20, pady=10)

    def monitor_select(self, option):
        self.screen_id = self.monitor_options.index(option)

    # Info Messagebox
    def info_msgbox(self, text):
        tkinter.messagebox.showinfo('Info', text)

    # Warning Messagebox
    def warning_msgbox(self, text):
        tkinter.messagebox.showwarning('Warning', text)

    # Confirm MessageBox
    def confirm_msgbox(self):
        YoN = tkinter.messagebox.askokcancel('Confirm', '캡쳐를 완료하고 PDF로 변환하시겠습니까?')
        return YoN
    
    def start(self):
        try:
            self.adress = self.folder + self.name_textbox.get()
            os.mkdir(self.adress)
            os.mkdir(self.adress + "/img")
            os.mkdir(self.adress + "/tmp")
            self.number = 1

            # change button state
            self.start_button.configure(state="disabled")
            self.folder_button.configure(state="disabled")
            self.end_button.configure(state="normal")
            self.capture_button.configure(state="normal")
            self.xy_button.configure(state="normal")
            
            self.info_msgbox("Start")
        except FileExistsError:
            self.warning_msgbox("이미 존재하는 파일 이름입니다.\n경로를 수정하거나 이름을 수정해주세요.")
    
    def end(self):
        YoN = self.confirm_msgbox()
        print(YoN)
        if YoN == False:
            self.info_msgbox("Canceled.")
            return

        self.file_list = os.listdir(self.adress + "/img")
        self.img_list = []

        if self.file_list == []:
            self.warning_msgbox("캡쳐된 이미지가 없습니다.")
            return

        #for i in tqdm(self.file_list):
        for i in self.file_list:
            self.img = Image.open(self.adress + "/img" + "\\" + str(i))
            self.img = self.img.convert("RGB")
            self.img_list.append(self.img)

        self.img = Image.open(self.adress + "/img" + "\\" + str(self.file_list[0])).convert("RGB")
        del self.img_list[0]
        self.img.save(self.adress + "\\" + self.name_textbox.get() + ".pdf", save_all=True, append_images=self.img_list)

        self.folder_button.configure(state="normal")
        self.end_button.configure(state="disabled")
        self.capture_button.configure(state="disabled")
        self.xy_button.configure(state="disabled")
        self.info_msgbox("Success")
        os.startfile(self.adress)

    def select_folder(self):
        self.folder = tkinter.filedialog.askdirectory(initialdir="/") + "/"
        if self.folder != "/":
            self.start_button.configure(state="normal")

    def capture(self):
        with mss.mss() as sct:
                mon = sct.monitors[self.screen_id + 1]

                if self.xy ==[]:
                    monitor = {"top": mon["top"], "left": mon["left"], "width": mon["width"], "height": mon["height"]}
                else:
                    monitor = {"top": self.monitors[self.screen_id].y + self.xy[0][1], "left": self.monitors[self.screen_id].x + self.xy[0][0], "width": self.xy[1][0] - self.xy[0][0], "height": self.xy[1][1] - self.xy[0][1]}

                img = sct.grab(monitor)
        
        try:
            output = f"{self.adress}/img/{str(self.number)}.jpg".format(**monitor)
            mss.tools.to_png(img.rgb, img.size, output=output)
            self.number += 1
            winsound.Beep(frequency=900, duration=150)
            winsound.Beep(frequency=1200, duration=100)
        except:
            print("Error : start 안하고 단축키 사용")
    
    def xy_setting(self):
        self.xy = []

        with mss.mss() as sct:
                mon = sct.monitors[self.screen_id + 1]

                if self.xy ==[]:
                    monitor = {"top": mon["top"], "left": mon["left"], "width": mon["width"], "height": mon["height"]}
                else:
                    monitor = {"top": self.xy[0][1], "left": self.xy[0][0], "width": self.xy[1][0] - self.xy[0][0], "height": self.xy[1][1] - self.xy[0][1]}

                img = sct.grab(monitor)
                output = f"{self.adress}/tmp/setting.jpg".format(**monitor)
                mss.tools.to_png(img.rgb, img.size, output=output)

        self.xy = setting_area.setting_area(self.adress + "/tmp/setting.jpg", self.screen_id)
        if self.xy[0][0] > self.xy[1][0]:
            self.xy[0][0], self.xy[1][0] = self.xy[1][0], self.xy[0][0]
        if self.xy[0][1] > self.xy[1][1]:
            self.xy[0][1], self.xy[1][1] = self.xy[1][1], self.xy[0][1]

        self.info_msgbox("범위 설정이 완료되었습니다.")

        print(self.xy)

if __name__ == "__main__":
    customtkinter.set_appearance_mode("Dark")
    customtkinter.set_default_color_theme("blue")

    app = App()
    app.title("Lecture_Capture")

    app.mainloop()