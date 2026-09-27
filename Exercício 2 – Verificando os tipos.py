# Considere as variáveis:

numero_camisa = 10
jogador = "Raphinha"

# Utilize isinstance() para verificar:

# se numero_camisa é um int;
# se numero_camisa é uma str;
# se jogador é uma str.

if isinstance(numero_camisa, int):
    print(f"numero_camisa é um inteiro")
else:
    print(f"numero_camisa não é um inteiro")


if isinstance(numero_camisa, str):
    print(f"numero_camisa é uma string")
else:
    print(f"numero_camisa não é uma string")

if isinstance(jogador, str):
    print(f"jogador é uma string")
else:
    print(f"jogador não é uma string")
