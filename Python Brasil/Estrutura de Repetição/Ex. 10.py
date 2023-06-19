print("\n\t Exercício 10 \n")

'''Faça um programa que receba dois números 
inteiros e gere os números inteiros que estão 
no intervalo compreendido por eles.'''

num1 = int (input("Digite um número: "))
num2 = int (input("Digite um número: "))

x = list(range(num1, num2, 1))

print(x)