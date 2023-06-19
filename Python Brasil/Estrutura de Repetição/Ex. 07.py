print("\n\t Exercício 7 \n")

'''Faça um programa que leia 5 números e informe o maior número.'''

i = 0
num = []

while i < 5:
    num.append (int (input("Informe um número de 1 a 5: ")))
    i += 1

maior = max(num)
print("O maior número é: ", maior)

