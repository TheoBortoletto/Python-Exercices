print("\n\t Exercício 2 \n")

'''Faça um programa que leia um nome de usuário e a sua senha
e não aceite a senha igual ao nome do usuário, mostrando uma 
mensagem de erro e voltando a pedir as informações.'''

user = str (input("Digite o nome de usuário: "))
senha = str (input("Digite a sua senha: "))
print("\n")

while user == senha:
    print("Seu nome de usuário e senha não podem ser iguais, tente novamente. \n")
    user = str (input("Digite o nome de usuário: "))
    senha = str (input("Digite a sua senha: "))

if user != senha:
    print("\nProssiga.")