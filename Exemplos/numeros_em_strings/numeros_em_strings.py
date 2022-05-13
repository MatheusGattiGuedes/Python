""" --------------------------------------- 
- Esse programa recebe duas strings
- transfroma em numeros e armazena eles
- em duas variaveis respectivamentes.
- Depois transforma os numeros novamente
- em strings e concatena-os junto a outras
- strings, mostrando uma menssagem na tela.
--------------------------------------- """

numero_um = int(input("Digite um número: ")) # Recebe uma string e transforma em numero.
numero_dois = float(input ("Digite outro número: ")) # Recebe outra string e transforma em ponto flutuante.

print("Você digitou " + str(numero_um) + " e " + str(numero_dois) + " respectivamente.") # Mostra na tela o resultado da concatenação dos numeros transformado em strings novamente.
