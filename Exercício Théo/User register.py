print("\n\t\t [--------------- Novo Usúario ---------------]\n")

print("\t Registro: \n")
email = str (input("Digite o seu E-mail: "))
senha = str (input("Digite a sua Senha: "))

print("\n")

confirmEmail = str (input("Confirme o seu E-mail: "))
confirmSenha = str (input("Confirme a sua Senha: "))

print("\n")

cont = 0

while confirmEmail != email or confirmSenha != senha:
    print("\n\tO E-mail ou Senha não coincidem, tente novamente.\n")
    
    confirmEmail = str (input("Confirme o seu E-mail: "))
    confirmSenha = str (input("Confirme a sua Senha: "))
    cont += 1
    if cont >= 3:
        print("\nO número máximo de tentativas foi excedido. Por favor reinicie o programa.\n")
        break


if confirmEmail == email and confirmSenha == senha:
    print("\nBem-vindo!!!\n")    
    