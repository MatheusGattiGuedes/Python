from gpiozero import LED, Button
from signal import pause

botao = Button(14, bounce_time=0.05) # 50 milisegundo para estabilisr o boto
vermelho = LED(15)

"""
botao.when_pressed = vermelho.on # Qunado o botão fo precionado
botao.when_released = vermelho.off # Qunado o botão for liberado
"""

# botao.when_pressed = vermelho.toggle # Quando preciona o botão muda o estao do LED


while True:
    if botao.is_pressed:
        vermelho.toggle()


pause()
