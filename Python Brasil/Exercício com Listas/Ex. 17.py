print("\n\t Exercício 17 \n")

'''Em uma competição de salto em distância 
cada atleta tem direito a cinco saltos. 
O resultado do atleta será determinado pela 
média dos cinco valores restantes. Você deve 
fazer um programa que receba o nome e as cinco 
distâncias alcançadas pelo atleta em seus saltos 
e depois informe o nome, os saltos e a média dos 
saltos. O programa deve ser encerrado quando não 
for informado o nome do atleta. A saída do programa 
deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo
 
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m'''

saltos = ["Primeiro Salto", "Segundo Salto", "Terceiro Salto", "Quarto Salto", "Quinto Salto"]
valores = []
i = 0

atleta = str (input("Informe o seu nome: "))
print("\n")

for salto in saltos:
    valor = float (input(f"{salto}: "))
    valores.append(valor)

media = sum(valores) / len(valores)
print("\n")

for valor in valores:
    print(f"{saltos[i]}: {valores[i]} m")
    i += 1

print("\nResultado final:")
print(f"Atleta: {atleta}")
print(f"Saltos: {valores[0]} - {valores[1]} - {valores[2]} - {valores[3]} - {valores[4]}")
print(f"Média dos saltos {media} m\n")