# Lecture-Capture
Lecture-Capture은 동영상 강의를 시청하는 중에 강의내용을 캡쳐하여 PDF로 변환해주는 프로그램입니다.  
>개발자 본인이 동영상 강의로 진행되나 PDF와 같은 다른 수업자료가 없던 수업을 수강하면서 일일이 수업내용을 옮겨적거나 동영상 화면을 캡쳐하는 것에 불편함을 느끼고 제작하게 되었습니다.

## 시연영상
https://user-images.githubusercontent.com/44095919/222128634-d29e2290-80d4-4557-adf1-f19573f22a01.mp4

## 설치방법
1. [Releases](https://github.com/geonbly327/Lecture-Capture/releases)에서 최신 버전 클릭
2. 버전.zip 파일 다운로드 후 압축 해제
3. exe -> dist -> lecture_capture 응용 프로그램 실행

## 기능
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)을 이용한 GUI
- Tkinter을 이용하여 파일경로를 파일 다이얼로그로 설정
- OpenCV를 이용하여 캡쳐범위 설정시 불필요한 클릭 방지 및 캡쳐범위 시각화

## 사용방법
![screenshot1](https://user-images.githubusercontent.com/44095919/222131315-2edfa802-730b-4e1d-9c6e-dbb6d55e4c86.png)
1. File Name 칸에 파일이름 입력하기
2. Folder 버튼을 클릭하여 파일을 저장할 폴더 지정하기
3. Start 버튼을 클릭하여 시작하기
4. XY setting 버튼을 클릭하여 캡쳐범위 설정하기 (※선택사항※)  
   4-1. 캡쳐범위를 설정하지 않을 경우, 기본값은 전체화면 캡쳐  
   4-2. 캡쳐범위는 상시 수정 가능  
   4-3. 프로그램을 종료하기 이전까지는 캡쳐범위가 유지
5. Capture 버튼을 클릭하거나, alt + c 단축키를 이용하여 화면캡쳐하기
6. End 버튼을 클릭하여 지금까지 캡쳐한 이미지를 조합하여 PDF로 변환하기
