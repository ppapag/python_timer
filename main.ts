let last = control.millis()
let state = false
basic.forever(function on_forever() {
    
    let now = control.millis()
    if (now - last >= 200) {
        state = !state
        //  led brightness 255 = on, 0 = off
        state ? led.plot(0, 0) : led.unplot(0, 0)
        last = now
    }
    
})
