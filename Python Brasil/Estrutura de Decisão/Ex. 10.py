print("\n\t Exercicío 10 \n")

'''Faça um Programa que pergunte em que turno você estuda. 
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", 
conforme o caso.'''


print("Digite 'm'-matutino 'v'-Vespertino ou 'n'- Noturno. \n")
msg = str (input("Digite: "))

if msg == "m":
    print("Bom dia! \n")

if msg == "v":
    print("Boa tarde! \n")

if msg == "n":
    print("Boa noite! \n")


elif msg != "m" and msg != "v" and msg != "n":
    print("Valor inválido")