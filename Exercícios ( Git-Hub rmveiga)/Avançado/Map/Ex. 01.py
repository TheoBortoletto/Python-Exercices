print("\n\t Exercício 1 \n")

'''Desenvolva um programa que converta todas as temperaturas 
desta lista em Celsius: ([22.5, 40, 13, 29, 34]) para Fahrenheit
'''

tempC = [22.5, 40, 13, 29, 34]

tempF = list(map(lambda temp: round((9/5) * temp + 32, 1), tempC))
print(tempF, "\n")