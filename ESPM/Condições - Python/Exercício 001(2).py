print("\n\t - Exercício 1(2): \n")

''' 1) Para ser aprovado em uma disciplina o aluno precisa obter média final maior ou igual a 7,00.
Considere que em uma determinada disciplina ele realiza 3 atividades com os seguintes pesos:

Prova - peso 45%, 
Projeto - peso 25%,
Atividades - peso 30%.

Caso o aluno não alcance a média 7,0 ele poderá realizar uma prova chamada EXAME. O novo resultado 
deverá ser calculado com a média simples entre a média anterior e a nota do exame. Altere o 
programa anterior adicionando uma condição para verificar 
situação do aluno: Aprovado, Aprovado com exame ou Reprovado.'''


disc = str (input("Nome da disciplina: "))
print("\n")

prova = float (input("Sua nota na prova: "))
projeto = float (input("Sua nota no projeto: "))
ativ = float (input("Sua nota nas atividades: "))

print("\n")

prova = prova * 0.45
projeto = projeto * 0.25
ativ = ativ * 0.3

media = (prova + projeto + ativ)

if media >= 7:
    print("Sua média é", media, "você está aprovado.")

else:
    print("Sua média é:", media, "você foi reprovado, mas tem direito ao EXAME.\n")

exameNota = float (input("Nota no Exame: "))

mediaNova = ((prova + projeto + ativ)/3) + ((media + exameNota)/3)

print("\nParabéns, você foi aprovado com exame.")

    