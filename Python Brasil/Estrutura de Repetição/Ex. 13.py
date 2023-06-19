print("\n\t Exercício 13 \n")

'''Faça um programa que peça dois números, base e expoente, 
calcule e mostre o primeiro número elevado ao segundo número. 
Não utilize a função de potência da linguagem.'''

base = int (input("Digite a base da operação: "))
expoente = int (input("Digite o expoente da operação: "))

i = 1
potencia = 1

while i <= expoente:
    potencia *= base
    i += 1

print(potencia)
