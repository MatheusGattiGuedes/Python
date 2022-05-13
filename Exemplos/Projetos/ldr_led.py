from gpiozero import LightSensor, PWMLED
from signal import pause

sensor = LightSensor(18)
led = PWMLED(21)

led.source = sensor.values # adiciona os valores PWM recebido pelo sensor aos valores PWM do led

pause()


""" Se tiver luz o LED apaga se não ele acende
sensor.when_light = led.of
sensor.when_dark = led.on

pause()
"""

""" # Detecta luz ou sombra e mostra na tela.
while True:
    sensor.wait_for_light()
    print("Isso é Luz! :)")
    sensor.wait_for_dark()
    print("Isso é sombra. :(")
"""
