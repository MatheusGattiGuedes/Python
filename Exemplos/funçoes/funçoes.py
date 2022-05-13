""" -----------------------------------------------------
| 'def' cria um função permitindo estrutura-la e        |
| posteriormente fazer a chamada dessa função no código |
----------------------------------------------------- """

def hello(): # Criando a função 'hello'
    print("Hello World!") # Quando chamada mostrará 'Hello World' na tela

def imprime_nome(nome): # Cria a função 'imprime_nome'
    if not nome: # Se não existir nenhum valor em 'nome'
        print("Por favor digite um nome!") # retorna isso na tela
    else: # Se o parâmetro nome existir
        print("Olá " + nome) # Então é mostrado 'Olá 'nome' na tela

def media(numero_1, numero_2): # Cria a função 'media' com dois parâmetros
    media = numero_1 + numero_2 # Atribui á 'media' a soma dos parâmetros
    media /= 2 # Divide o valor contido em 'media' por 2 e o atribui esse valor
    print("Média: " + str(media)) # transforma média em string e mostra na tela

""" Chamando as funções """
hello()
imprime_nome("")
imprime_nome("Matheus")
media(15, 20)
