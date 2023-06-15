print("\n\t  Exercício 9 \n")

'''Faça um Programa que leia três números e mostre-os em ordem decrescente.'''


a = float(input('Escreva um número: '))
b = float(input('Escreva um número: '))
c = float(input('Escreva um número: '))

numList = []

num1 = int (input("Digite um número: "))
num2 = int (input("Digite um número: "))
num3 = int (input("Digite um número: "))
print("\n")

numList.append(num1)
numList.append(num2)
numList.append(num3)

numList.sort()
print(numList)

# if a >= b and a >= c and b >= c:
#     print(f'A ordem decrescente é {a} , {b} e {c}')
# elif a >= b and a >=c and c >= b:
#     print(f'A ordem decrescente é {a} , {c} e {b}')
# elif b >= a and b >= c and a >= c:
#     print(f'A ordem decrescente é {b} , {a} e {c}')
# elif b >= a and b >= c and c >= a:
#     print(f'A ordem decrescente é {b} , {c} e {a}')
# elif c >= a and c >= b and a >=b:
#     print(f'A ordem decrescente é {c} , {a} e {b}')
# elif c >= a and c >= b and b >= a:
#     print(f'A ordem decrescente é {c} , {b} e {a}')

