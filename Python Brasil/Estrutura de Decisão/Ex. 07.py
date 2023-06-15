print("\n\t  Exercício 7 \n")

'''Faça um Programa que leia três números e mostre o maior e o menor deles.'''

val1 = int (input("Digite um número: "))
val2 = int (input("Digite um número: "))
val3 = int (input("Digite um número: "))
print("\n")

if val1 > val2 and val3:
    maior = val1

if val2 > val1 and val3:
    maior = val2
    
if val3 > val1 and val2 and val2 < val3 and val1 < val3:
    maior = val3 

if val3 and val2 > val1:
    menor = val1

if val3 and val1 > val2:
    menor = val2

if val1 and val2 > val3:
    menor = val3

print("O maior número é:", maior)
print("O menor número é:", menor, "\n")
