from machine import Pin, PWM
from time import sleep

#Defining LEDs and Button

pwm_1 = PWM(Pin(15))
pwm_2= PWM(Pin(13))
pwm_3 = PWM(Pin(12))
pwm_4 = PWM(Pin(11))
pwm_5 = PWM(Pin(10))
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

#Setting LED frequency

pwm_1.freq(1000)
pwm_2.freq(1000)
pwm_3.freq(1000)
pwm_4.freq(1000)
pwm_5.freq(1000)


while True:
    #If button is pressed, display LEDs in this sequence
    if button.value():
        for duty in range(65025):
            pwm_1.duty_u16(duty)
            sleep(0.000000001)
        for duty in range(65025, 0, -1000):
             pwm_1.duty_u16(duty)
             sleep(0.000000001)
        for duty in range(65025):
            pwm_2.duty_u16(duty)
            sleep(0.0000000001)
        for duty in range(65025, 0, -1000):
             pwm_2.duty_u16(duty)
             sleep(0.000000001)
        for duty in range(65025):
            pwm_3.duty_u16(duty)
            sleep(0.00000001)
        for duty in range(65025, 0, -1000):
             pwm_3.duty_u16(duty)
             sleep(0.00000001)
        for duty in range(65025):
            pwm_4.duty_u16(duty)
            sleep(0.00000001)
        for duty in range(65025, 0, -1000):
             pwm_4.duty_u16(duty)
             sleep(0.00000001)
        for duty in range(65025):
            pwm_5.duty_u16(duty)
            sleep(0.00000001)
        for duty in range(65025, 0, -1000):
             pwm_5.duty_u16(duty)
             sleep(0.00000001)
        for duty in range(65025):
            pwm_4.duty_u16(duty)
            sleep(0.00000001)
        for duty in range(65025, 0, -1000):
            pwm_4.duty_u16(duty)
            sleep(0.00000001)
        for duty in range(65025):
            pwm_3.duty_u16(duty)
            sleep(0.00000001)
        for duty in range(65025, 0, -1000):
            pwm_3.duty_u16(duty)
            sleep(0.000000001)
        for duty in range(65025):
            pwm_2.duty_u16(duty)
            sleep(0.0000000001)
        for duty in range(65025, 0, -1000):
            pwm_2.duty_u16(duty)
            sleep(0.000000001)
