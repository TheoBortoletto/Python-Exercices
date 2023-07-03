print("\n\t Exercício 1 \n")

'''Desenvolva um programa que apresente o 
maior e o menor valores da sequência ([54, 10, 29, 87, 7, 64])
'''

#! ERRADO:

#* from functools import reduce

#* list = [54, 10, 29, 87, 7, 64]

#* def acharMin(x, y):
#*     if x < y:
#*         return x
#*     else:
#*         return y
    
#* def acharMax(x, y):
#*     if x > y:
#*         return y
#*     else:
#*         return x
    
#* minimo = reduce(acharMin, list)
#* maximo = reduce(acharMax, list)

#* print(f"O menor valor da lista é: {minimo}.")
#* print(f"O maior valor da lista é: {maximo}. \n")

#! CERTO:

from functools import reduce

list = [54, 10, 29, 87, 7, 64] 

maiorValor = 