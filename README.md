# Lecture-Capture
Lecture-Capture은 동영상 강의를 시청하는 중에 강의내용을 캡쳐하여 PDF로 변환해주는 프로그램입니다.  
>개발자 본인이 동영상 강의로 진행되나 PDF와 같은 다른 수업자료가 없던 수업을 수강하면서 일일이 수업내용을 옮겨적거나 동영상 화면을 캡쳐하는 것에 불편함을 느끼고 제작하게 되었습니다.

## 시연영상
https://user-images.githubusercontent.com/44095919/223807817-edd8cdf0-0617-41cb-9827-cf53fedacedb.mp4

## 설치방법
1. [Releases](https://github.com/geonbly327/Lecture-Capture/releases)에서 최신 버전 클릭
2. 버전.zip 파일 다운로드 후 압축 해제
3. exe -> dist -> lecture_capture 응용 프로그램 실행

> **Note**
> Windows만 지원합니다.

## 기능
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)을 이용한 GUI
- OpenCV를 이용하여 원하는 영역의 캡쳐범위 설정
- 버튼 혹은 단축키를 사용하여 동영상 강의 캡쳐
- 캡쳐된 강의자료를 자동으로 PDF로 변환

## 사용방법
![스크린샷 2023-03-09 031710](https://user-images.githubusercontent.com/44095919/223804088-945914be-a094-44d1-ae5f-485f581084c5.png)
1. File Name 칸에 파일이름 입력하기
2. Folder 버튼을 클릭하여 파일을 저장할 폴더 지정하기
3. Start 버튼을 클릭하여 시작하기
4. Display 옵션 메뉴에서 디스플레이 선택하기  
   4-1. Display숫자(Main)은 메인 디스플레이  
   4-2. 디스플레이는 상시 수정 가능  
5. XY setting 버튼을 클릭하여 캡쳐범위 설정하기 (※선택사항※)  
   5-1. 캡쳐범위를 설정하지 않을 경우, 기본값은 전체화면 캡쳐  
   5-2. 캡쳐범위는 상시 수정 가능  
   5-3. 프로그램을 종료하기 이전까지는 캡쳐범위가 유지
6. Capture 버튼을 클릭하거나, alt + c 단축키를 이용하여 화면캡쳐하기
7. End 버튼을 클릭하여 지금까지 캡쳐한 이미지를 조합하여 PDF로 변환하기
