# Crie um programa que pergunte a idade do usuário:

# Converta a resposta para int.

# Use try/except para impedir que o programa seja encerrado caso alguém digite algo 
# como: vinte

# Se a conversão funcionar, mostre:
# Idade registrada com sucesso.
# Se ocorrer um ValueError, mostre:
# Digite a idade utilizando apenas números.

idade_valida = False

while idade_valida == False:
    try:
        idade = input("Qual a sua idade? ")
        idade = int(idade)
        idade_valida = True
    except ValueError:
        print("Digite a idade utilizando apenas números.")

print("Idade registrada com sucesso.")