from gpiozero import Button, Buzzer, LED
from signal import pause

bz = Buzzer(14)
botao = Button(15)
vermelho = LED(17)

while True:
    if botao.when_pressed:
        bz.toogle
        vermelho.toggle

# botao.when_pressed = bz.toggle

pause()
