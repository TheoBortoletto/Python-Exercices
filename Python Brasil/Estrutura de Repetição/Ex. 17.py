print("\n\t Exercício 17")

'''Faça um programa que calcule o fatorial de um número 
inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120'''

num = int (input("Digite o número que deseja ser fatorado: "))

result = 1
i = 1

while i <= num:
    result *= i
    i += 1

print(result)