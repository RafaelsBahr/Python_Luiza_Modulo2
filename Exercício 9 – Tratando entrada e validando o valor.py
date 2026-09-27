# Uma avaliação de jogador deve receber uma nota entre 0 e 10.

# Crie um programa que peça essa nota ao usuário.

# O programa deve:


# tentar converter a entrada para float;
# tratar um possível ValueError;
# verificar se a nota está entre 0 e 10;
# informar quando a nota estiver fora desse intervalo.

# Exemplos:

# Digite a nota: oito
# Valor inválido. Digite um número.

# Digite a nota: 15
# A nota deve estar entre 0 e 10.

# Digite a nota: 8.5
# Nota registrada: 8.5



nota_valida = False
while nota_valida == False:
    try:
        nota_jogador = float(input("Qual a nota: "))
        if nota_jogador < 0 or nota_jogador > 10:
            print("A nota deve estar entre 0 e 10. \n")
        else:
            print(f"Nota registrada: {nota_jogador}")
            nota_valida = True
    except ValueError:
        print("Valor inválido. Digite um número.\n")