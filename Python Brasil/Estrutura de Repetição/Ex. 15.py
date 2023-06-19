print("\n\t Exercício 15 \n")

'''A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
Faça um programa capaz de gerar a série até o n−ésimo termo.'''

n = int (input("Digite o termo: "))

penultimo = 1
ultimo = 1

if (n==1) or (n==2):
    print("1")

else:
    i = 3
    while i <= n:
        termo = ultimo + penultimo
        penultimo = ultimo 
        ultimo = termo
        i += 1
    print(termo)