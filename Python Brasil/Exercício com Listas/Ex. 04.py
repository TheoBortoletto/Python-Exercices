print("\n\t Exercício 4 \n")

'''Faça um Programa que leia um vetor de 5 caracteres, 
e diga quantas consoantes foram lidas. Imprima as consoantes.
'''

caract = []
contvogal = 0
vogais = ["a", "e", "i", "o", "u"]
i = 1

while i <= 5:
    entrada = str (input("Digite a palavra: "))
    i += 1

    caract.append(entrada)
    
    if entrada in vogais:
        contvogal += 1


print("\nQuantidade de consoantes: ", len(caract) - contvogal)