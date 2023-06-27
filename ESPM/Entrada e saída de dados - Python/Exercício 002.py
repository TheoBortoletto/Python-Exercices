print("\n\t - Exercício 2 \n")

#* 2) Ler o nome de um produto, o seu valor e a quantidade 
#* comprada e apresentar uma mensagem contendo o nome do produto, 
#* o seu valor unitário e o valor total da compra.

produto = str (input("Digite o nome do produto: "))
valorProduto = float (input("Informe o valor do produto: "))
qtdProduto = int (input("Quantidade de " + produto + " comprada: "))

print("\n")

valorTotal = valorProduto * qtdProduto

print("Nome do produto: " + produto + ";\nValor unitário: " + str(valorProduto) + ";\nValor total da compra: " + str(valorTotal) + ".")

print("\n")