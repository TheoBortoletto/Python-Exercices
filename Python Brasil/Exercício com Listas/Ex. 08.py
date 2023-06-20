print("\n\t Exercício 8 \n")

'''Faça um Programa que peça a idade e a altura de 5 pessoas, 
armazene cada informação no seu respectivo vetor. Imprima a 
idade e a altura na ordem inversa a ordem lida.'''

idade = []
altura = []

cont = 1

while cont <= 5:
    idade.append(int (input("Informe a sua idade: ")))
    altura.append(float (input("Informe a sua altura: ")))
    print("\n")
    cont += 1

print("Idade inversa da ordem digitada: ", idade[::-1])
print("\n")
print("Altura inversa da ordem digitada: ", altura[::-1])
print("\n")