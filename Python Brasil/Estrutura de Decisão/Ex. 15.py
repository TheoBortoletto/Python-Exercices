print("\n\t Exercicío 15 \n")

'''aça um Programa que peça os 3 lados de um triângulo. 
O programa deverá informar se os valores podem ser um triângulo. 
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, 
isósceles ou escaleno.

Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;'''

lado1 = float (input("Informe o valor do lado 1: "))
lado2 = float (input("Informe o valor do lado 2: "))
lado3 = float (input("Informe o valor do lado 3: "))
print("\n")

if lado1 == lado2 == lado3:
    print("Este triângulo é equilátero. \n")

if lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Este triângulo é isósceles. \n")

else:
    print("Este triângulo é escaleno. \n")