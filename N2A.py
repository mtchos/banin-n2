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
produtos = [[], [], []]

for linha in arquivo:
    registro = linha.split(sep=";")
    codigo = int(registro[0])
    produtos[0].append(codigo)
    quantidade = int(registro[1])
    produtos[1].append(quantidade)
    preco_unitario = float(registro[2])
    produtos[2].append(preco_unitario)

arquivo.close()

# para evitar alterações, transformar listas internas em tuplas
produtos[0] = tuple(produtos[0])
produtos[1] = tuple(produtos[1])
produtos[2] = tuple(produtos[2])

# PARTE 2 - fazer as contas do total geral
total = 0
for i in range(len(produtos[0])):
    total += produtos[1][i] * produtos[2][i]

print(f"O total geral vendido é R$ {total:.2f}\n\n")

# PARTE 3
codigo = 1
while codigo != 0:
    codigo = int(input("Digite o código: "))
    if 10000 <= codigo <= 21000:
        total_produto = 0
        for i in range(len(produtos[0])):
            if produtos[0][i] == codigo:
                total_produto += produtos[1][i] * produtos[2][i]
        print(f"Total vendido do produto {codigo} = R$ {total_produto:.2f}\n")
    elif codigo != 0:
        print(f"{codigo} Código inválido (deve ser entre 10000 de e 21000)\n")

print("Fim do programa")
        