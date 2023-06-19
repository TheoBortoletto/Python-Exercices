print("\n\t Exercício 14 \n")

'''Faça um programa que peça 10 números inteiros, 
calcule e mostre a quantidade de números pares e a 
quantidade de números impares.'''

num = []
i = 1


while i <= 10:
    num.append (int(input("Digite um número: ")))
    i += 1

print("\nLista dos números: ", num, "\n")

pares = []
impares = []

for x in num:
    if x % 2 == 0:
        pares.append(x)
    else:
        impares.append(x)

print("Números pares: ", pares)
print("Números ímpares: ", impares)

print("\n")