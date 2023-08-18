import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = round(random.randrange(1, 101))
total_de_tentativas = 0

print("Qual nivel de dificuldade você quer?")
dificuldade_str = input("(1) Fácil, (2) Médio, (3) Difícil \n")
dificuldade = int(dificuldade_str)

if dificuldade == 1:
    total_de_tentativas = 20

elif dificuldade == 2:
    total_de_tentativas = 10

else:
    total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):

    print("Rodada #{} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um número entre 1 e 100: ")
    chute = int(chute_str)

    if chute < 1 or chute > 100:
        print("Voce deve digitar um número entre 1 e 100!!!")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("Parabens!")
        break
    else:
        print("Oh não!", end=" ")

        if maior:
            print("Seu chute foi maior que o número secreto!")

        elif menor:
            print("Seu chute foi menor que o número secreto!")

print("Fim de jogo!")