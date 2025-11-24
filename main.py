last = control.millis()
state = False

def on_forever():
    global last, state
    now = control.millis()
    if now - last >= 200:
        state = not state
        # led brightness 255 = on, 0 = off
        led.plot(0, 0) if state else led.unplot(0, 0)
        last = now

basic.forever(on_forever)
