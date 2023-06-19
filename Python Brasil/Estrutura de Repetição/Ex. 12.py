print("\n\t Exercício 12 \n")

'''Desenvolva um gerador de tabuada, capaz de gerar a 
tabuada de qualquer número inteiro entre 1 a 10. 
O usuário deve informar de qual numero ele deseja 
ver a tabuada. A saída deve ser conforme o exemplo abaixo:

Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50 '''

num = int (input("Digite qual tabuada você quer: "))
print("\n")

mult = 1

while mult < 11:

    result = num * mult
    print(num, "X", mult, "=", result)
    mult += 1