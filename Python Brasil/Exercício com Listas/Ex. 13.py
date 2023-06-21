print("\n\t Exercício 13 \n")

'''Faça um programa que receba a temperatura média de cada 
mês do ano e armazene-as em uma lista. Após isto, calcule 
a média anual das temperaturas e mostre todas as temperaturas 
acima da média anual, e em que mês elas ocorreram 
(mostrar o mês por extenso: 1 - Janeiro, 2 - Fevereiro, . . . ).'''

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
temperaturas = []
cont = 0
i = 0

for mes in meses:
    temperatura = float (input(f"Informe a temperatura do mês de {mes}: "))
    temperaturas.append(temperatura)

media = sum(temperaturas) / len(temperaturas)

print("\n")

for i, temperatura in enumerate(temperaturas):
    if temperatura > media:
        print(f"{meses[i]} teve uma temperatura de {temperatura}°C, acima da média anual de {media}°C.")

print("\n")
