print("\n\t - Exercício 2(2): \n")

'''2) Considere a situação em que um sistema que controla a temperatura ambiente de uma determinada
sala precisa receber a temperatura e decidir qual mensagem apresentar:

Temperatura acima de 28 graus, deve mostrar “acionar o ar condicionado”
Temperatura abaixo de 10 graus, deve mostrar “acionar o aquecedor”
Altere o programa anterior e adicione essa condição'''

temp = float (input("Temperatura de agora: "))
print("\n")

if temp > 28:
    print("Acionar o ar condicionado.\n")

if temp < 10:
    print("Acionar o aqueceedor.\n")