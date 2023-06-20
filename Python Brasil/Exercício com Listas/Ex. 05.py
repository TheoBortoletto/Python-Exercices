print("\n\t Exercício 5 \n")

'''Faça um Programa que leia 20 números inteiros 
e armazene-os num vetor. Armazene os números pares 
no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
'''

pares = []
impares = []

numeros = []
i = 1

while i <= 20:
    numeros.append(int (input("Digite um número: ")))
    i += 1

print("\nVetor com todos os númeors: ", numeros)

for x in numeros:

    if x %2 == 0:
        pares.append(x)
    else:
        impares.append(x)

print("Vetor com os números pares: ", pares)
print("Vetor com os números ímpares: ", impares, "\n")