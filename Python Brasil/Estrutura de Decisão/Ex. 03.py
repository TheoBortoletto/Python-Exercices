print("\n\t Exercício 3 \n")

'''Faça um Programa que verifique se uma letra digitada é 
   "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.'''

string = str (input("Digite 'F' para feminino e 'M' para masculino: "))

if string == "f":
    print("Feminino. \n")

if string == "m":
    print("Masculino. \n")

else:
    print("Sexo Inválido. \n")