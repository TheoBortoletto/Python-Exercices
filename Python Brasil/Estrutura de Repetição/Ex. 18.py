print("\n\t Exercício 18 \n")

'''Faça um programa que, dado um conjunto de N números, 
determine o menor valor, o maior valor e a soma dos valores.'''

num = []
i = 1

while i <= 5:
    num.append(int (input("Digite um número: ")))
    i += 1

print("\n")

print("O menor valor da lista é: ", min(num), "\n")

print("O maior valor da lista é: ", max(num), "\n")

print("A soma dos valores da lista é: ", sum(num), "\n")




