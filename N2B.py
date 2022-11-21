print("Gerador de Senhas\n")
print("Mateus Anunciato Sobral")
print("Matheus Silva e Sousa")
print("Tomás Carrera Massabki")
print("Vinicius Esposito Cava")

from random import randint

# PARTE 1 - Gerar arquivo de entrada, chamado MATR.TXT, contendo N números de matrícula
# no formato de 6 dígitos, gerados em sequência por laço for

# arquivo = open("MATR.txt", "w")

# for i in range(222000, 223000):
#    arquivo.write(f'{str(i)}\n')

#arquivo.close()

# PARTE 2 - Receber argumentos para função de geração da senha (tipo de senha e tamanho):
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

ltr_maiuscula = []
for i in range(65,91):
    ltr_maiuscula.append(chr(i))

ltr_minuscula = []
for i in range(97, 123):
    ltr_minuscula.append(chr(i))

especiais = [45, 95, 58, 64, 35, 36, 38, 63]
for i in range(len(especiais)):
    especiais[i] = chr(especiais[i])


# PARTE 3 - Definir função que gera senha
def GeraSenha(tipo, Tam):
    if tipo == 'a':
        escopo = algarismos
    elif tipo == 'b':
        escopo = ltr_maiuscula + ltr_minuscula
    elif tipo == 'c':
        escopo = algarismos + ltr_maiuscula
    elif tipo == 'd':
        escopo = algarismos + ltr_maiuscula + ltr_minuscula
    elif tipo == 'e':
        escopo = algarismos + ltr_maiuscula + ltr_minuscula + especiais
    senha = ""
    # primeiro ciclo de geração da senha
    for i in range(Tam):
       digit = escopo[randint(0,len(escopo)-1)]
       senha = senha + digit
    return senha

def VerificaSenha(tipo, senha):
    if tipo == 'a':
        return True
    elif tipo == 'b':
        temMaiuscula = False
        temMinuscula = False
        for i in range(len(senha)):
            if senha[i] in ltr_maiuscula:
                temMaiuscula = True
            else:
                temMinuscula = True
            if temMaiuscula and temMinuscula:
                return True
        if temMaiuscula and temMinuscula:
            return True
        else:
            return False
    elif tipo == 'c':
        temAlgarismo = False
        temMaiuscula = False
        for i in range(len(senha)):
            if senha[i] in algarismos:
                temAlgarismo = True
            else:
                temMaiuscula = True
            if temAlgarismo and temMaiuscula:
                return True
        if temAlgarismo and temMaiuscula:
            return True
        else:
            return False

    elif tipo == 'd':
        temAlgarismo = False
        temMaiuscula = False
        temMinuscula = False
        for i in range(len(senha)):
            if senha[i] in ltr_maiuscula:
                temMaiuscula = True
            elif senha[i] in ltr_minuscula:
                temMinuscula = True
            else:
                temAlgarismo = True
            if temMaiuscula and temMinuscula and temAlgarismo:
                return True
        if temMaiuscula and temMinuscula and temAlgarismo:
            return True
        else:
            return False
    elif tipo == 'e':
        temAlgarismo = False
        temMaiuscula = False
        temMinuscula = False
        temEspecial = False
        for i in range(len(senha)):
            if senha[i] in algarismos:
                temAlgarismo = True
            elif senha[i] in ltr_maiuscula:
                temMaiuscula = True
            elif senha[i] in ltr_minuscula:
                temMinuscula = True
            else:
                temEspecial = True
            if temAlgarismo and temMaiuscula and temMinuscula and temEspecial:
                return True
        if temAlgarismo and temMaiuscula and temMinuscula and temEspecial:
            return True
        else:
            return False


# PARTE 4 - Implementar função em código que apresente programa para usuário

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
    senhaValida = VerificaSenha(tipo, senha)
    while not senhaValida:
        senha = GeraSenha(tipo, tamanho)
        senhaValida = VerificaSenha(tipo, senha)
    linha = linha.split('\n')
    matricula = linha[0]
    saida.write("{};{};\n".format(matricula, senha))

entrada.close()
saida.close()
