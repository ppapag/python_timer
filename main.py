from microbit import *

last = running_time()

while True:
    now = running_time()
    if now - last >= 200:
        current = display.get_pixel(0, 0)
        new = 0 if current > 0 else 9
        display.set_pixel(0, 0, new)
        last = now
