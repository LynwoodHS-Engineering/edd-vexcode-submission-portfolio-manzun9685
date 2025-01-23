while True:
    if limit_switch_a.pressing() and limit_switch_b.pressing():
        led_c.on()
        led_d.off()
    else:
        led_d.on()
        led_c.off()
