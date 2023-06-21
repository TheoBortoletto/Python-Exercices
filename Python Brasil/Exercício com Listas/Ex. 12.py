print("\n\t Exercício 12 \n")

'''Foram anotadas as idades e alturas de 30 alunos. 
Faça um Programa que determine quantos alunos com mais 
de 13 anos possuem altura inferior à média de altura desses alunos.
'''

idade = []
altura = []
idadeMaiorTreze = []

perguntaI = []
perguntaA = []

cont = 1




while cont <= 5:
    print("Aluno", cont,":")
    perguntaI.append(int (input("Informe a sua idade: ")))
    perguntaA.append(float (input("Informe a sua altura: ")))
    cont += 1

mediaAltura = sum(perguntaA) / 5
   
if perguntaA < mediaAltura:
    idadeMaiorTreze.append(perguntaA)


print(idadeMaiorTreze)




