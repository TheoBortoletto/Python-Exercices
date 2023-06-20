print("\n\t Exercício 6 \n")

'''Faça um Programa que peça as quatro notas de 10 alunos, 
calcule e armazene num vetor a média de cada aluno, imprima 
o número de alunos com média maior ou igual a 7.0.
'''

i = 1
aluno1 = []

print("Aluno 1: \n")
while i <= 4:
    aluno1.append(float (input("Digite a sua nota: ")))
    i += 1

j = 1
aluno2 = []

print("\nAluno 2: \n")
while j <= 4:
    aluno2.append(float (input("Digite a sua nota: ")))
    j += 1

k = 1
aluno3 = []

print("\nAluno 3: \n")
while k <= 4:
    aluno3.append(float (input("Digite a sua nota: ")))
    k += 1

x = 1
aluno4 = []

print("\nAluno 4: \n")
while x <= 4:
    aluno4.append(float (input("Digite a sua nota: ")))
    x += 1

z = 1
aluno5 = []

print("\nAluno 5: \n")
while z <= 4:
    aluno5.append(float (input("Digite a sua nota: ")))
    z += 1

print("\n")

print("Notas do Aluno 1: ", aluno1)
print("Notas do Aluno 2: ", aluno2)
print("Notas do Aluno 3: ", aluno3)
print("Notas do Aluno 4: ", aluno4)
print("Notas do Aluno 5: ", aluno5)

print("\n")

media1 = []
media2 = []
media3 = []
media4 = []
media5 = []

media1.append (sum(aluno1) / 4)
media2.append (sum(aluno2) / 4)
media3.append (sum(aluno3) / 4)
media4.append (sum(aluno4) / 4)
media5.append (sum(aluno5) / 4)

if (sum(aluno1) / 4) >= 7.0:
    print("Média do Aluno 1: ", media1)
else: 
    print("O Aluno 1 não atingiu a média 7.0")

if (sum(aluno2) / 4) >= 7.0:
    print("Média do Aluno 2: ", media2)
else: 
    print("O Aluno 2 não atingiu a média 7.0")

if (sum(aluno3) / 4) >= 7.0:
    print("Média do Aluno 3: ", media3)
else: 
    print("O Aluno 3 não atingiu a média 7.0")

if (sum(aluno4) / 4) >= 7.0:
    print("Média do Aluno 4: ", media4)
else: 
    print("O Aluno 4 não atingiu a média 7.0")

if (sum(aluno5) / 4) >= 7.0:
    print("Média do Aluno 5: ", media5)
else:
    print("O Aluno 5 não conseguiu atingir a média 7.0")

print("\n")