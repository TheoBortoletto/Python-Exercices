print("\n\t Exercício 14 \n")

'''Utilizando listas faça um programa que faça 5 perguntas 
para uma pessoa sobre um crime. As perguntas são:

"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 

O programa deve no final emitir uma classificação sobre a participação da pessoa 
no crime. Se a pessoa responder positivamente a 2 questões 
ela deve ser classificada como "Suspeita", entre 3 e 4 como 
"Cúmplice" e 5 como "Assassino". Caso contrário, ele será 
classificado como "Inocente".'''

perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]

pontos = 0

print("Digite 's' para Sim e 'n' para Não: \n")

for pergunta in perguntas:
    ponto = str (input (f" {pergunta}: "))

    if ponto == "s":
        pontos += 1

print("\n")

if pontos == 0 or pontos == 1:
    print("Voocê é inocente.\n")

if pontos == 2:
    print("Você é suspeito.\n")

if pontos == 3 or pontos == 4:
    print("Você é cúmplice.\n")

if pontos == 5:
    print("Você é o assasino.\n")
