print("\n\t - Exercício 001: \n")

'''1) O usuário deverá informar 3 valores que representarão os lados de um triângulo. Verifique se os
      valores formam um triângulo e classifique esse triângulo:

 - equilátero: três lados iguais;
 - isósceles: dois lados iguais;
 - scaleno: três lados diferentes.

Observação: Para formar um triângulo, nenhum dos lados pode ser igual a zero, um lado não pode ser
maior do que a soma dos outros dois.'''

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

