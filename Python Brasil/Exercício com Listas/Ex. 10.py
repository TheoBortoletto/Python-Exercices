print("\n\t Exercício 10 \n")

'''Faça um Programa que leia dois vetores com 10 elementos cada. 
Gere um terceiro vetor de 20 elementos, cujos valores deverão ser 
compostos pelos elementos intercalados dos dois outros vetores.'''

vetorA = []
vetorB = []
cont = 1

print("Valores do vetor A:\n")

while cont <= 2:
    vetorA.append(int (input("Digite um número: ")))
    cont += 1

cont = 1

print("\nValores do vetor B:\n")

while cont <= 2:
    vetorB.append(int (input("Digite um número: ")))
    cont += 1

vetorC = vetorA + vetorB

print("\nVetor C: ", vetorC, "\n")
