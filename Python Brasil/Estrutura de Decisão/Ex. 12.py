print("\n\t Exercicío 12 \n")

'''Faça um programa para o cálculo de uma folha de pagamento, 
sabendo que os descontos são do Imposto de Renda, que depende do 
salário bruto (conforme tabela abaixo) e 3% para o Sindicato e 
que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado 
(é a empresa que deposita). O Salário Líquido corresponde ao 
Salário Bruto menos os descontos. O programa deverá pedir ao 
usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, 
dispostas conforme o exemplo abaixo. 
No exemplo o valor da hora é 5 e a quantidade de hora é 220.

        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00'''


hora = int (input("Informe a quantidade de horas trabalhadas: "))
valorHora = int (input("Informe o valor da sua hora: "))

salarioB = hora * valorHora

ir = 0
ircinco = salarioB * 0.05
irdez = salarioB * 0.10
irvinte = salarioB * 0.20

inss = salarioB * 0.10
fgts = salarioB * 0.11

descontos = ir + inss
descontosc = ircinco + inss
descontosd = irdez + inss 
descontosv = irvinte + inss

salarioL = salarioB - descontos
salarioLC = salarioB - descontosc
salarioLD = salarioB - descontosd
salarioLV = salarioB - descontosv



print("\n")

if salarioB <= 900:
    print("Salário Bruto:", '(',hora, "*", valorHora,'):', "R$", salarioB)
    print("(-) IR -> ISENTO")
    print("(-) INSS (10%) R$", inss) 
    print("FGTS (11%) R$", fgts)
    print("Total de descontos: R$", descontos)
    print("Salário Líquido: R$", salarioL, "\n")

if salarioB > 900 and salarioB <= 1500:
    print("Salário Bruto:", '(',hora, "*", valorHora,'):', "R$", salarioB)
    print("(-) IR (5%) R$", ircinco)
    print("(-) INSS (10%) R$", inss) 
    print("FGTS (11%) R$", fgts)
    print("Total de descontos: R$", descontosc)
    print("Salário Líquido: R$", salarioLC, "\n")

if salarioB > 1500 and salarioB <= 2500:
    print("Salário Bruto:", '(',hora, "*", valorHora,'):', "R$", salarioB)
    print("(-) IR (10%) R$", irdez)
    print("(-) INSS (10%) R$", inss) 
    print("FGTS (11%) R$", fgts)
    print("Total de descontos: R$", descontosd)
    print("Salário Líquido: R$", salarioLD, "\n")  

if salarioB > 2500:
    print("Salário Bruto:", '(',hora, "*", valorHora,'):', "R$", salarioB)
    print("(-) IR (20%) R$", irvinte)
    print("(-) INSS (10%) R$", inss) 
    print("FGTS (11%) R$", fgts)
    print("Total de descontos: R$", descontosv)
    print("Salário Líquido: R$", salarioLV, "\n")  