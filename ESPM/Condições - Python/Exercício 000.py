print("\n\t - Exercício 0: \n")

'''Ler 4 valores:
   Calcular a média
   Condição:
   Se A média for maior do 50
   então mostrar a média
   senão não mostrar a média'''

p1 = float (input("Digite a nota da prova 1: "))
p2 = float (input("Digite a nota da prova 2: "))
p3 = float (input("Digite a nota da prova 3: "))
p4 = float (input("Digite a nota da prova 4: "))
print("\n")

media = (p1 + p2 + p3 + p4) / 4

if media >= 6.0:
    print("Sua média é: ", media)
    print("Parabéns, você atingiu a média maior que 6. \n")
   
else:
    print("Sua média é: ", media)
    print("Você não conseguiu atingir a média. \n")

if media == 6.0:
    print("Sua média é: ", media)
    print("Parabéns, você conseguiu atingir a média. \n")


