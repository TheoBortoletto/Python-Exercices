print("\n\t Exercício 12 \n")

'''Foram anotadas as idades e alturas de 30 alunos. 
Faça um Programa que determine quantos alunos com mais 
de 13 anos possuem altura inferior à média de altura desses alunos.
'''

import random
idades = []
alturas = []
aluno_13 = []
media_13 = []

for i in range(30):
    numero_aleatorio = idades.append(random.randrange(1, 20)) #! Números aleatórios 
                                                              #! de 1 a 20 (idades).

    numero_aleatorio2 = alturas.append(random.randrange(150, 200)) #! Números aleatórios 
                                                                  #! de 50 a 200 (altura 
                                                                  #! em cm).

for i in range(30):
    if idades[i] > 13: #! Percorre o vetor das 
                       #! idades e verifica se as idades são maiores que 13.

        aluno_13.append(alturas[i]) #! Se a condição for verdadeira, 
                                    #! pega as alturas dos que são maiores de 13.

media = sum(aluno_13) / len(aluno_13) #! Faz a soma das alturas e
                                      #! divide ela pela quantidade 
                                      #! de itens que tem dentro dessa lista


for i in range(len(aluno_13)): #! Percorre o tanto de itens que contém nessa lista
                               #! Nesta lista só há as alturas dos que tem mais de 13
                               
    if aluno_13[i] < media: #! Verifica se a altura dos alunos maiores de 13 anos é
                            #! menor que a média.

        media_13.append(aluno_13[i]) #! Se a condição for verdadeira, pega todos
                                     #! com a média inferior a média das altura dos
                                     #! alunos e coloca na lista 'media_13'

print("\nIdade dos 30 alunos: ", idades, "\n")
print("Altura dos 30 alunos: ", alturas, "\n")

print("Quantidade de aluos que são maiores de 13 anos: ", len(aluno_13), "\n")
print("Altura dos alunos que são maiores de 13 anos: ", aluno_13, "\n") 

print("Quantidade de alunos que possuem a altura inferior à media e altura: ", len(media_13), "\n")


