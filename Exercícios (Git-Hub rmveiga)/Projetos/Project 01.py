'''Desenvolva um jogo de acerte o número, onde o 
computador escolhe um número inteiro aleatório de 
0 a 10, e o usuário tem 5 tentativas para adivinhar 
o número.

OBS.: O design da tela pode ser implementado livremente



(PLUS): Implemente um sistema de pontuação 
com o seguinte comportamento: se o usuário 
adivinhar o número na primeira tentativa, 
receberá a pontuação máxima (ex. 100 pontos); 
se o usuário adivinhar o número na última 
tentativa, receberá a pontuação mínima 
(ex. 10 pontos); se o usuário não acertar 
o número, não receberá nenhum ponto.

(PLUS): Implemente um controle de erros. 
Caso o jogador digite um número fora da 
faixa permitida ou caracteres não numéricos,
o sistema deve notificar o jogador e solicitar 
o input correto.

(PLUS): Implemente a opção de o usuário iniciar uma nova 
partida. Ao finalizar uma rodada, após o resultado final, 
o jogo deve perguntar se o jogador quer iniciar uma nova 
partida e, em caso negativo, encerrar a aplicação.'''


import random

def game():
    
    print("\n\t JOGO DE ACERTE O NÚMERO:")
    
    randNum = random.randrange(0, 10)
    tentativa = 1
    pontos = 0
    print(randNum, "\n")

    while tentativa <= 5:
        palpite = int (input(f"Tentativa {tentativa}: "))
        if palpite == randNum:
            print("Você acertou!!! \n")
            break
        tentativa += 1
    else:
        print("\nNúmero máximo de tentativas atingido.")

    if palpite == randNum and tentativa == 1:
        pontos = 100

    if palpite == randNum and tentativa == 2:
        pontos = 80

    if palpite == randNum and tentativa == 3:
        pontos = 60

    if palpite == randNum and tentativa == 4:
        pontos = 40

    if palpite == randNum and tentativa == 5:
        pontos = 20

    print(f"Total de pontos: {pontos}.\n")

    jogarNovamente = int (input("Deseja jogar novamente? (1)-SIM  (2)-NÃO: "))
    print("\n")

    if jogarNovamente == 1:
        game()
    if jogarNovamente == 2:
        print("ATÉ LOGO!!! \n")
        exit()

game()