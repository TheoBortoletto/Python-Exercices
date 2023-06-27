print("\n\t - Exercício 2: \n")

'''2) Considere a situação em que um sistema que controla a temperatura ambiente de uma determinada
   sala precisa receber a temperatura e, caso acima de 28 graus, precisa mostrar uma mensagem
   indicando que é necessário acionar o ar condicionado. Escreva um programa que receba a
   temperatura e verifique isso.'''

tempAr = float (input("Qaul a temperatura no momento?: "))

if tempAr > 28:
    print("\nATENÇÃO! É necessário o uso de ar condiconado.\n")

else:
    print("\nA temperatura está boa. Não é necessário o uso de ar condicionado.\n")
