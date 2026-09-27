# Crie um programa para registrar a quantidade de gols de uma seleção.

# O programa deve continuar perguntando:

# Quantos gols a seleção marcou?

# até que o usuário forneça um número inteiro válido e maior ou igual a zero.

# Considere situações como:

# Quantos gols a seleção marcou? três
# Entrada inválida.

# Quantos gols a seleção marcou? -2
# A quantidade de gols não pode ser negativa.

# Quantos gols a seleção marcou? 4
# Quantidade de gols registrada: 4

# Para resolver o exercício, utilize os conteúdos estudados até aqui, incluindo:

# input();
# conversão com int();
# try/except;
# ValueError;
# condição;
# while.

# O programa só deve parar de solicitar a informação quando receber um valor válido.

qtd_gols_valido = False
while qtd_gols_valido == False:
    try:
        qtd_gols = int(input("Quantos gols a seleção marcou? "))
        if qtd_gols < 0:
            print("A quantidade de gols não pode ser negativa.")
        else:
            print(f"Quantidade de gols registrada: {qtd_gols}\n")
            qtd_gols_valido = True
    except ValueError:
        print("Entrada inválida.")