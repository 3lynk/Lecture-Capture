import pynput

xy = []

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