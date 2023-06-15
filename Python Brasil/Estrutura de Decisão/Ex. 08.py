print("\n\t  Exercício 8 \n")

'''Faça um programa que pergunte o preço de três produtos e informe 
   qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato. '''

a = float (input("Digite o valor do produto 1: "))
b = float (input("Digite o valor do produto 2: "))
c = float (input("Digite o valor do produto 3: "))
print("\n")

menor = a

if b < c and b < a:
    menor = b
if c < b and c < a:
    menor = c

if menor == a:
    print("O produto com menor valor é o produto 1.\n")

if menor == b:
    print("O produto com menor valor é o produto 2.\n")

if menor == c:
    print("O produto com menor valor é o produto 3.\n")