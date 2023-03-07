import cv2
import numpy as np 
import screeninfo
import time

click = False

def draw_rectangle(event, x, y, flags, param):
    global x1,y1, x2, y2, click, roop, tmp, img

    if event == cv2.EVENT_LBUTTONDOWN:
        click = True 
        x1, y1 = x,y
		
    elif event == cv2.EVENT_MOUSEMOVE:
        if click == True:
            pass

    elif event == cv2.EVENT_LBUTTONUP:
        click = False; 

        overlay = img.copy()
        cv2.rectangle(overlay, (x1, y1), (x, y), (255, 255, 255), -1, cv2.LINE_AA)
        opacity = 0.4
        cv2.addWeighted(overlay, opacity, img, 1 - opacity, 0, img)
        cv2.rectangle(img, (x1, y1), (x, y), (0, 0, 0), 1, cv2.LINE_AA)

        x2, y2 = x, y

        roop = False

def setting_area(path, screen_id):
    global tmp, roop, img, x1, y1, x2, y2

    roop = True
    tmp = True
    is_color = False

    screen = screeninfo.get_monitors()[screen_id]
    width, height = screen.width, screen.height

    x1,y1 = -1,-1
    x2, y2 = -1, -1

    img_array = np.fromfile(path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    cv2.namedWindow('image', cv2.WND_PROP_FULLSCREEN)
    cv2.setMouseCallback('image',draw_rectangle)

    while True:
        cv2.moveWindow('image', screen.x - 1, screen.y - 1)
        cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow('image', img)

        k = cv2.waitKey(1) & 0xFF
            
        if k == 27:
            break

        if tmp == False:
            time.sleep(1)
            break

        if roop == False:
            tmp = False

    cv2.destroyAllWindows()
    return [[x1, y1], [x2, y2]]


if __name__ == "__main__":
    print(setting_area())