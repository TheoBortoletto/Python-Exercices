print("\n\t Exercício 2 \n")

'''Desenvolva um programa que leia um número qualquer e informe se ele é par ou ímpar'''

num = int (input("Informe um número: "))
print("\n")

par = lambda a: num % 2 == 0

if par(num):
    print(f"O número {num} é par. \n")
else:
    print(f"O número {num} é ímpar. \n")

#* print(par(num), "\n"))