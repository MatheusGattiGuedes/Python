from gpiozero import Button
from random import choice
from time import sleep

botao = Button(3)

while True:
    print(" ")
    print("Faça apenas perguntas de SIM ou NÃO!")
    pgt = input("Pergunte algo: ")
    print("")

    sleep(3)

    print("Raspberry diz: Estou consultando os astros...")
    print(" ")

    sleep(1)

    respostas = [
        "Os sinais apontam que sim",
        "Sem duvida nenhuma",
        "Não conte com isto",
        "Interferências estão no meu caminho, não posso predizer agora",
        "Não. de jeito nenhum"
    ]

    print("Raspberry diz: " + choice(respostas))
