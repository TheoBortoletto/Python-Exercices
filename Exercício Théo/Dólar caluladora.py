print("\n")

dolarBR = float (input("Informe o valor do dólar em R$: "))
convert = float (input("Informe o valor que deseja converter: "))

conta = dolarBR * convert

parcela = (conta / 4) * 3

dozeVzs = parcela / 12

print("\nValor total:%.2f" % conta)

print("1/3 do valor total:%.2f" % parcela)

print("As parcelas ficam 12x de:%.2f" % dozeVzs, "\n")

