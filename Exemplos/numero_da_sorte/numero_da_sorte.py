from random import randrange """ Inporta a função 'randrange da bibliotéca 'random'' """

NUMERO_DA_SORTE = randrange(10) """ gera um numero aleatória entre 0 e 9 """

while True:
    print(" ")
    numero = int(input("Digite um número da sorte: "))
    if not numero:
        continue
    elif numero > NUMERO_DA_SORTE:
        print("Tente um número menor.")
    elif numero < NUMERO_DA_SORTE:
        print("Tente um número MAIOR.")
    elif numero == NUMERO_DA_SORTE:
        break

print("PARABÉNS")
print("Você acertou o nuúmero da sorte!")
    
