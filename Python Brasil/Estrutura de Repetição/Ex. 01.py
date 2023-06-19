print("\n\t Exercício 1 \n")

'''Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido e continue
pedindo até que o usuário informe um valor válido.'''

num = int (input("Digite um número entre 0 e 10: "))
print("\n")

if num <= 10:
    print("Valor okay")

while num > 10:
    num = int (input("Digite novamente: "))


