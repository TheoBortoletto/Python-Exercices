print("\n\t Exercício 2 \n")

'''Faça um Programa que leia um vetor de 10 números 
reais e mostre-os na ordem inversa.'''

num = []
i = 1

while i <= 10:
    num.append(int (input("Digite um número: ")))
    i += 1

num.sort(reverse = True)
print("\nOrdem inversa dos valores digitados: ", num, "\n")