print("\n\t Exercício 1 \n")

'''Desenvolva um programa que leia o seu nome 
completo e que apresente somente o seu primeiro 
e último nomes
'''

fulln = str (input("Informe o seu nome completo: "))
print("\n")
fname = lambda nome: nome.split()[0] #! Pegará a primeira posição -> (primeiro nome).
lname = lambda nome: nome.split()[-1] #! Pegará a primeira posição de trás pra frente.

print(f"Seu primeiro nome é {fname(fulln)}.")
print(f"Seu último nome é {lname(fulln)}. \n")

