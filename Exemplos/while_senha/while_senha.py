SENHA_PADRAO = "Matheus"
ERROU = 0

while True:
    senha = input("Digite sua senha: ")
    if not senha:
        continue
    elif ERROU == 2:
        break
    elif senha == SENHA_PADRAO:
        break
    print("Senha INCORRETA")
    ERROU += 1

if ERROU == 2:
    print("Você errou 3 tentativas!")
    print("Acesso Bloqueado.")
else:
    print("Bem vindo!")
    print("Iniciando programa...")
