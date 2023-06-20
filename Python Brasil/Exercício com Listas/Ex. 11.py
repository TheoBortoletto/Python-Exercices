print("\n\t Exercício 11 \n")

'''Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.'''

vetorA = []
vetorB = []
vetorC = []
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

cont = 1

print("\nValores do vetor C:\n")

while cont <= 2:
    vetorC.append(int (input("Digite um número: ")))
    cont += 1

vetorD = vetorA + vetorB + vetorC

print("\nVetor D: ", vetorD, "\n")