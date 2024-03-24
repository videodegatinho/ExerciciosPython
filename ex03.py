precoAtual = float(input("Qual o preço atual do produto? "))
qtdVendas = int(input("Qual a quantidade de vendas do produto? "))

if qtdVendas <= 500 and precoAtual <= 30:
    novoPreco = precoAtual * 1.1
elif 501 >= qtdVendas <= 1200 and 30.01 >= precoAtual <= 80.00:
    novoPreco = precoAtual * 1.15
elif qtdVendas >= 1200 and precoAtual >= 80:
    novoPreco = precoAtual * 0.80
else:
    novoPreco = precoAtual

print("Novo preço do produto:", novoPreco)
