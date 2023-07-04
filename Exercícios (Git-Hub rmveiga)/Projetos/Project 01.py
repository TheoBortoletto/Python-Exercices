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
            print("\nVocê acertou!!!")
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

#* Solução alterinativa por -> rmveiga

#* from random import randint
#* 
#* DEBUG = False
#* TENTATIVAS = 6
#* TOTAL_RODADAS = TENTATIVAS - 1
#* PONTUACAO_MAXIMA = 100
#* MENSAGENS = {
#*     'DEFAULT': {
#*         'SAUDACAO': 'Escolhi um número entre 0 e 10. Tente adivinhar',
#*         'VITORIA': 'Parabéns!! Você acertou',
#*         'DERROTA': 'Que pena!! Você não acertou',
#*         'INPUT_JOGADOR': 'Digite um número entre 0 e 10: ',
#*         'NOVA_PARTIDA': 'Gostaria de jogar novamente? (1-Sim; 2-Não) ',
#*         'ENCERRAMENTO': 'Até a próxima!!!',
#*         'PONTUACAO': lambda pontuacao: f'A sua pontuação final é {pontuacao} pontos'
#*     },
#*     'ERRO': {
#*         'TENTATIVA_INVALIDA': 'ERRO: São permitidos apenas números inteiros entre 0 e 10',
#*         'NOVA_PARTIDA_INVALIDA': 'ERRO: São permitidas apenas as opções: 1-Sim ou 2-Não',
#*     }
#* }
#* 
#* 
#* def mensagem_tela(mensagem, pontuacao=None, mensagem_resultado=None):
#*     TAMANHO_LINHA = 70
#*     ALINHAMENTO = f'^{TAMANHO_LINHA}'
#*     print(f'{"-" * TAMANHO_LINHA}')
#*     print(f'{mensagem.upper():{ALINHAMENTO}}')
#*     if pontuacao is not None:
#*         print(f'{mensagem_resultado.upper():{ALINHAMENTO}}')
#*     print(f'{"-" * TAMANHO_LINHA}')
#* 
#* 
#* def get_input_jogador(mensagem):
#*     return str(input(mensagem))
#* 
#* 
#* def valida_tentativa_jogador(numero):
#*     try:
#*         int(numero)
#*     except ValueError:
#*         return False
#*     return int(numero) in range(11)
#* 
#* 
#* def valida_opcao_jogador(input):
#*     try:
#*         int(input)
#*     except ValueError:
#*         return False
#*     return int(input) in range(3)
#* 
#* 
#* def nova_partida(input):
#*     # 1 - Sim; 2 - Não
#*     return input == '1'
#* 
#* 
#* def verifica_acerto(numero_jogador, numero_computador):
#*     return int(numero_jogador) == numero_computador
#* 
#* 
#* def calcula_pontuacao(rodada, tentativas, pontuacao_maxima=100):
#*     if rodada == 1:
#*         return pontuacao_maxima
#*     else:
#*         return pontuacao_maxima - (pontuacao_maxima / (tentativas - 1)) * (rodada - 1)
#* 
#* 
#* while True:
#*     numero_computador = randint(0, 10)
#*     numero_jogador = None
#*     rodada = 1
#*     mensagem_tela(MENSAGENS.get('DEFAULT').get('SAUDACAO'))
#* 
#*     if DEBUG:
#*         print(numero_computador)
#* 
#*     while rodada < TENTATIVAS:
#*         print(f'Rodada {rodada}/{TOTAL_RODADAS}')
#*         numero_jogador = get_input_jogador(MENSAGENS.get('DEFAULT').get('INPUT_JOGADOR'))
#* 
#*         while not valida_tentativa_jogador(numero_jogador):
#*             mensagem_tela(MENSAGENS.get('ERRO').get('TENTATIVA_INVALIDA'))
#*             print(f'Rodada {rodada}/{TOTAL_RODADAS}')
#*             numero_jogador = get_input_jogador(MENSAGENS.get('DEFAULT').get('INPUT_JOGADOR'))
#* 
#*         if verifica_acerto(numero_jogador, numero_computador):
#*             break
#* 
#*         rodada += 1
#* 
#*     pontos = calcula_pontuacao(rodada, TENTATIVAS, PONTUACAO_MAXIMA)
#*     resultado = MENSAGENS.get('DEFAULT').get('PONTUACAO')
#* 
#*     if rodada < TENTATIVAS:
#*         mensagem_tela(
#*             MENSAGENS.get('DEFAULT').get('VITORIA'),
#*             pontuacao=pontos,
#*             mensagem_resultado=resultado(pontos)
#*         )
#*     else:
#*         mensagem_tela(
#*             MENSAGENS.get('DEFAULT').get('DERROTA'),
#*             pontuacao=pontos,
#*             mensagem_resultado=resultado(pontos)
#*         )
#* 
#*     opcao = get_input_jogador(MENSAGENS.get('DEFAULT').get('NOVA_PARTIDA'))
#*     while not valida_opcao_jogador(opcao):
#*         mensagem_tela(MENSAGENS.get('ERRO').get('NOVA_PARTIDA_INVALIDA'))
#*         opcao = get_input_jogador(MENSAGENS.get('DEFAULT').get('NOVA_PARTIDA'))
#* 
#*     if not nova_partida(opcao):
#*         mensagem_tela(MENSAGENS.get('DEFAULT').get('ENCERRAMENTO'))
#*         break