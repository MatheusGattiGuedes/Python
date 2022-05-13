from gpiozero import MotionSensor, LED, Buzzer, Button
from signal import pause

pir = MotionSensor(4)
led = LED(16)
bz = Buzzer(21)
bt = Button(15)

while True:
    if pir.when_motion:
        bz.on
        print("Alarme tocando!")
    if bt.when_pressed:
        bz.off
        print("Alarme desligado")
    
pause()
