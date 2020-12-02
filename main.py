def on_forever():
    basic.show_leds("""
        . . . . .
        . # # # .
        . . . . .
        . # # # .
        . . . . .
        """)
    basic.show_leds("""
        # # # # .
        # . . . .
        # . # # .
        # . . # .
        # # # # .
        """)
    basic.show_leds("""
        # # # # .
        # . . # .
        # . . # .
        # . . # .
        # # # # .
        """)
    basic.show_leds("""
        # # . . .
        # . # . .
        # . # . .
        # . # . .
        # # . . .
        """)
basic.forever(on_forever)

def on_forever2():
    if pins.digital_read_pin(DigitalPin.P13) == 0 and pins.digital_read_pin(DigitalPin.P14) == 0:
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 255)
    elif pins.digital_read_pin(DigitalPin.P13) == 1 and pins.digital_read_pin(DigitalPin.P14) == 0:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 240)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, 10)
    elif pins.digital_read_pin(DigitalPin.P13) == 0 and pins.digital_read_pin(DigitalPin.P14) == 1:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, 10)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 240)
    else:
        if maqueen.ultrasonic(PingUnit.CENTIMETERS) < 15:
            while maqueen.ultrasonic(PingUnit.CENTIMETERS) < 20:
                maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, 255)
basic.forever(on_forever2)
