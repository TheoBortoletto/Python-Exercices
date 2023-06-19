print("\n\t Exercício 8 \n")

'''Faça um programa que leia 5 números e informe a soma e a média dos números.'''

x = 0
num = []

while x < 5:
    num.append (int(input("Digite um número: ")))
    x += 1

media = sum(num) / 5

print("A media dos valores é: ", media, "\n")