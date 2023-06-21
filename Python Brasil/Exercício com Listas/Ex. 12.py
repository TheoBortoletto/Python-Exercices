print("\n\t Exercício 12 \n")

'''Foram anotadas as idades e alturas de 30 alunos. 
Faça um Programa que determine quantos alunos com mais 
de 13 anos possuem altura inferior à média de altura desses alunos.
'''

idade = []
altura = []
cont = 1

while cont <= 5:
    print("Aluno", cont,":")
    idade.append(int (input("Informe a sua idade: ")))
    altura.append(float (input("Informe a sua altura: ")))
    cont += 1


for x in idade:
    if x < 13:
        idade.append(x)

print(idade)

# alunos = []

# mediaAltura = sum(altura) / 5

# print(mediaAltura)
