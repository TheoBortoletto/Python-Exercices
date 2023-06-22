print("\n\t Exercício 15 \n")

'''Faça um programa que leia um número indeterminado de valores, 
correspondentes a notas, encerrando a entrada de dados quando for 
informado um valor igual a -1 (que não deve ser armazenado). 
Após esta entrada de dados, faça:

Mostre a quantidade de valores que foram lidos; OK
Exiba todos os valores na ordem em que foram informados, um ao lado do outro; OK
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro; OK
Calcule e mostre a soma dos valores; OK
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;'''

numeros = []

cont = 0

while cont > -1:
    numUser = float (input("Digite a sua nota: "))
    numeros.append(numUser)
    if numUser == -1:
        numeros.pop()
        break
    else:
        cont += 1

print("\nQuantidade de valores que foram lidos: ", len(numeros))
print("Valores na ordem que foram digitados, um do lado do outro: ", numeros, "\n")
numeros.reverse()
print("Valores na ordem inversa à que foram informados, um abaixo do outro: ", *numeros, sep = "\n")
numeros.reverse()




    