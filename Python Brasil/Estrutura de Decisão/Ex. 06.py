print("\n\t  Exercício 6 \n")

'''Faça um Programa que leia três números e mostre o maior deles.'''

val1 = int (input("Digite um número: "))
val2 = int (input("Digite um número: "))
val3 = int (input("Digite um número: "))

if val1 > val2 and val3:
    print(val1, "é maior que", val2, "e", val3)

if val2 > val1 and val3:
    print(val2, "é maior que", val1, "e", val3)

if val3 > val1 and val2:
    print(val3, "é maior que", val1, "e", val2)
