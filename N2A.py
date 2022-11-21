print("Totalização Simples de Vendas de Produtos\n")
print("Mateus Anunciato Sobral")
print("Matheus Silva e Sousa")
print("Tomás Carrera Massabki")
print("Vinicius Esposito Cava")

# PARTE 1 - abrir arquivo e organizar em listas
arquivo = open("vendas.txt")

# declarar lista de produtos, contendo três listas internas, na ordem:
# indice 0 -> codigos de produto
# indice 1 -> quantidade de produto
# indice 2 -> preço unitário de cada produto
produtos = []

for linha in arquivo:
    registro = linha.split(sep=";")
    codigo = int(registro[0])
    quantidade = int(registro[1])
    preco_unitario = float(registro[2])
    produtos.append([codigo, quantidade, preco_unitario])

arquivo.close()

# PARTE 2 - fazer as contas do total geral
total = 0
for produto in produtos:
    total += produto[1] * produto[2]

print(f"O total geral vendido é R$ {total:.2f}\n\n")

# PARTE 3
codigo = 1
while codigo != 0:
    codigo = int(input("Digite o código: "))
    if 10000 <= codigo <= 21000:
        total_produto = 0
        for produto in produtos:
            if produto[0] == codigo:
                total_produto += produto[1] * produto[2]
        print(f"Total vendido do produto {codigo} = R$ {total_produto:.2f}\n")
    elif codigo != 0:
        print(f"{codigo} Código inválido (deve ser entre 10000 de e 21000)\n")

print("Fim do programa")
        