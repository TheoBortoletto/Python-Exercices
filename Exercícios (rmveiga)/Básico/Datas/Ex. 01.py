print("\n\t Exercício 1 \n")

'''Carregue a data atual do computador e, 
com base na data atual, apresente a data de dois dias no futuro'''

from datetime import datetime, timedelta

date = datetime.now()

futuredate = datetime.now() + timedelta(2)

print("Data de hoje: ", date)

print("Data futura: ", futuredate)

print("\n")

