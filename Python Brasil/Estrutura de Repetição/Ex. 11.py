print("\n\t Exercício 11 \n")

'''Altere o programa anterior para mostrar no final a soma dos números.'''

num = []

num1 = int (input("Digite um número: "))
num2 = int (input("Digite um número: "))
print("\n")

x = list(range(num1, num2, 1))

print(x)

num.append(num1)
num.append(num2)

soma = sum(num)

print("\nA soma dos números é:", soma, "\n")