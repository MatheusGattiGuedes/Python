from gpiozero import Button, Buzzer
from signal import pause

bz = Buzzer(14)
botao = Button(15)

botao.when_pressed = bz.toggle

pause()
