print("\n\t Exercício 2 \n")

'''Desenvolva um programa que apresente a 
soma dos valores pares e dos valores ímpares 
da sequência ([21, 5, 34, 8, 16, 7, 3])'''

num = [21, 5, 34, 8, 16, 7, 3]

somaPar = sum(map(lambda n: n if n % 2 == 0 else 0, num))
somaImpar = sum(map(lambda n: n if n % 2 != 0 else 0, num))

print(f"Lista dos números: {num}. \n")
print(f"Soma dos valores Pares {somaPar}.")
print(f"Soma dos valores Ímpares {somaImpar}. \n")
