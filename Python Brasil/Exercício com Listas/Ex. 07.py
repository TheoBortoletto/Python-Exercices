print("\n\t Exercício 7 \n")

'''Faça um Programa que leia um vetor de 5 números inteiros, 
mostre a soma, a multiplicação e os números.'''

from math import prod

numeros = []
cont = 1

while cont <= 5:
    numeros.append(int (input("Digite um número: ")))
    cont += 1

print("\n")
soma = sum(numeros)
mult = prod(numeros)

print("Lista dos valores digitados: ", numeros)
print("Soma dos valores digitados: ", soma)
print("Multiplicação dos valores digitados: ", mult)

print("\n")