import pynput

xy = []

def click(x, y, button, pressed):
    if pressed:
        x = int(x)
        y = int(y)
        xy.append(x)
        xy.append(y)
        if len(xy) == 4:
            print(xy)
            return False

with pynput.mouse.Listener(on_click = click) as pynput.mouse.Listener:
    pynput.mouse.Listener.join()