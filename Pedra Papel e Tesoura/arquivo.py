import random
import time
print("Bem vindo ao jogo")
def checar():
    opcoes = [1,2,3]
    computador = random.choice(opcoes)
    voce = int(input(""))
    time.sleep(1)
    print("...")
    time.sleep(1)
    print(f"O computador usou {computador} ")


    if voce == computador:
        print("Deu empate")
    elif (voce == 1 and computador == 3) or (voce == 2 and computador == 1) or (voce == 3 and computador == 2):
        print("Parabens voce venceu!!")
    else:
        print("Que pena voce perdeu")

    jogarNovamente()


def jogar():
    time.sleep(1)
    print("Escolha uma das opcoes:")
    time.sleep(1)
    print("1 - Pedra " "\n" "2 - Papel  " "\n" "3 - Tesoura")
    time.sleep(1)
    checar()


def jogarNovamente():
    print("Deseja jogar novamente? \n1 - Sim  \n2 - Não")
    jogaDeNovo = input("")

    if jogaDeNovo == '1':
            jogar()
    elif jogaDeNovo == '2' or jogaDeNovo == "Não":
         print("Adeus amigo")
    else:
         print("Vou entender isso como um Não")
          
jogar()