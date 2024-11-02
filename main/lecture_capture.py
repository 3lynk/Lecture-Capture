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
import base64
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

        self.explain = 'How to use \n\n 1. File Name 입력하기 \n\n 2. folder 버튼 누르고 저장할 폴더 선택하기 \n\n 3. Start 버튼 누르기\n\n 4. Display 선택하기(주 모니터는 Main) \n\n 5. XY setting 버튼 누른후 캡쳐할 영역 드래그하기 \n (세팅을 안할시 기본값인 전체화면 캡쳐) \n (드래그하는 동안 아무것도 안보이는게 정상) \n\n 6. Capture버튼을 클릭하거나 단축키 "alt + c"로 캡쳐하기(단축키를 사용할 때에는 다른 단축키가 작동될 수 있기 때문에 작업 표시줄 클릭 후 사용하길 권장) \n\n 7. 캡쳐가 다 끝난 후 End 버튼을 눌러 완성하기'
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
        for i in range(1, len(self.file_list) + 1):
            self.img = Image.open(self.adress + "/img" + "\\" + str(i) + ".jpg")
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

    icon = \
    """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"""

    icondata = base64.b64decode(icon)
    tempFile= "../build/icon.ico"
    iconfile= open(tempFile,"wb")
    iconfile.write(icondata)
    iconfile.close()
    app.wm_iconbitmap(tempFile)

    app.mainloop()