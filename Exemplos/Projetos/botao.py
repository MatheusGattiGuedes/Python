from gpiozero import Button

botao = Button(14)

botao.wait_for_press()
print("Botão precionado")
