print("\n\t Exercício 4 \n")

'''Faça um Programa que verifique se uma letra digitada é vogal ou consoante.'''

consoante = ["a", "e", "i", "o", "u"]

letra = str (input("Digite uma letra: "))

if letra in consoante:
    print("A letra:", letra + "," + " é vogal. \n") 

else:
    print("A letra:", letra + "," + " é consoante. \n")