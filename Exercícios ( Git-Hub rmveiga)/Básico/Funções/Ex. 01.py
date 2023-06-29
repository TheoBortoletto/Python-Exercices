print("\n\t Exercício 1 \n")

'''Desenvolva um programa que tenha uma função
que verifique se um número inteiro qualquer 
é par ou impar'''

def parImpar():
    if num %2 == 0:
        print("\nO número", num, "é par. \n")
    else:
        print("\nO número", num, "é ímpar. \n")
    

num = int (input("Informe um número para ver se ele é Par ou Ímpar: "))

parImpar()