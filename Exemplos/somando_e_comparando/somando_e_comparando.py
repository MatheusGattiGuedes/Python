print("Verifique se você foi aprovado!")
print(" ")
nota_um = int(input("Digite o resultado da primeira prova: "))
nota_dois = int(input("Agora o resultado da segunda: "))
resultado = nota_um + nota_dois

if resultado >= 60 and resultado < 70:
    print(" ")
    print("Nada mal, mas precisa melhorar!")
    print("Sua nota foi: " + str(resultado))
    print("Parabéns você foi APROVADO!")
elif resultado >= 70 and resultado < 89:
    print(" ")
    print("Você foi bem!")
    print("Sua nota foi: " + str(resultado))
    print("Prabéns você foi APROVADO!")
elif resultado >= 90 and resultado <101:
    print(" ")
    print("Excelente, você foi muito bem!")
    print("Sua nota foi: " + str(resultado))
    print("Parabéns você foi APROVADO!")
elif resultado > 100 or resultado < 0:
    print(" ")
    print("Algo está errado!")
    print("O valor maáximo é 100")
    print("E também não pode ser menor que 0")
    print("Tente NOVAMENTE!")
elif resultado > 0 or resultado < 60:
    print(" ")
    print("Você deve estudar mais!")
    print("Sua nota foi: " + str(resultado))
    print("Você foi REPROVADO!")
else:
    print("Valor INVALIDO!")


    

    
