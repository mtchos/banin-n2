print("Gerador de Senhas\n")
print("Mateus Anunciato Sobral")
print("Matheus Silva e Sousa")
print("Tomás Carrera Massabki")
print("Vinicius Esposito Cava")

import random

# PARTE 1 - Receber argumentos para função de geração da senha (tipo de senha e tamanho):
# Numérica -> 'a' = apenas algarismos
# Alfabética -> 'b' = apenas letras maiúsculas e minúsculas
# Alfanumérica 1 -> 'c' = apenas letras maiúsculas e algarismos
# Alfanumérica 2 -> 'd' = apenas letras minúsculas, maiúsculas e algarismos
# Geral -> 'e' = apenas letras minúsculas, maiúsculas, algarismos e caracteres especiais abaixo:
#                       [-, _, :, @, #, $, &, ?]

# usar tabela ASCII para isso? ver funções built-in ord() e chr()

# listas geradas por tipo de caracter, usando função chr() e tabela ASCII,
# para futura verificação da senha, no que diz respeito a conter pelo menos 1 caracter de cada tipo

# ex.: senhas de tipo 'c' necessitam ter pelo menos 1 caracter algarismo, 1 caracter
# maiúscula e 1 caracter minúscula

algarismos = []
for i in range(48,58):
    algarismos.append(chr(i))

letraMaiuscula = []
for i in range(65,91):
    letraMaiuscula.append(chr(i))

letraMinuscula = []
for i in range(97, 123):
    letraMinuscula.append(chr(i))

especiais = [45, 95, 58, 64, 35, 36, 38, 63]
for i in range(len(especiais)):
    especiais[i] = chr(especiais[i])


# PARTE 2 - Definir função que gera senha
def GeraSenha(tipo, tamanho):
    # a depender do tipo de senha, coloca os respectivos grupos
    # de caracter dentro uma lista maior (escopo)
    escopo = []
    if tipo == 'a':
        escopo = [algarismos]
    elif tipo == 'b':
        escopo = [letraMaiuscula, letraMinuscula]
    elif tipo == 'c':
        escopo = [algarismos, letraMaiuscula]
    elif tipo == 'd':
        escopo = [algarismos, letraMaiuscula, letraMinuscula]
    elif tipo == 'e':
        escopo = [algarismos, letraMaiuscula, letraMinuscula, especiais]
    # para garantir a variedade da posição dos tipos, embaralha a
    # lista de escopo com o shuffle
    random.shuffle(escopo)
    # define o valor de caracteres que ainda faltam a ser incrementados
    # na senha
    tamanhoRestante = tamanho
    senha = ""
    # loop for que garante a presença de ao menos um caracter de cada 
    # tipo do escopo usando choice como fator de aleatoriedade e decrementa
    # o tamanho restante a ser usado no próximo loop for
    for tipo in escopo:
        senha += random.choice(tipo)
        tamanhoRestante -= 1
    # após garantir que existe um caracter de cada tipo na senha, completa
    # ela com caracteres de um tipo aleatório
    for i in range(tamanhoRestante):
       tipo = random.choice(escopo)
       senha += random.choice(tipo)
    return senha

# PARTE 3 - Implementar função em código que apresente programa para usuário

# pedir o tamanho e repetir enquanto não for válido
tamanho = int(input("Informe o tamanho: "))

# pedir o tipo e repetir enquanto não for válido
tipoValido = False
tipo = input("Informe o tipo: ")
while not tipoValido:
    if tipo == 'a' or tipo == 'b' or tipo == 'c' or tipo == 'd' or tipo == 'e':
        tipoValido = True
    else:
        print("Valor inválido para tipo de senha!")
        print("Precisa ser a, b, c, d ou e")
        tipo = input("Digite novamente: ")


entrada = open("MATR.txt", "r")
saida = open("SENHA.txt", "w")

for linha in entrada:
    senha = GeraSenha(tipo, tamanho)
    linha = linha.split('\n')
    matricula = linha[0]
    saida.write("{};{};\n".format(matricula, senha))

entrada.close()
saida.close()
