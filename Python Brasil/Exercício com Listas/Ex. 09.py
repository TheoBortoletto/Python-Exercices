print("\n\t Exercício 9 \n")

'''Faça um Programa que leia um vetor A com 10 números inteiros, 
calcule e mostre a soma dos quadrados dos elementos do vetor.
'''

vetor = []
cont = 1

while cont <= 5:
    vetor.append(int (input("Digite um número: ")))
    cont += 1

print("\n")

i = 0
while vetor[i] <= 5:
    print("O quadrado de ", vetor[i], "é:", vetor[i]**2)
    i += 1

print("\n")