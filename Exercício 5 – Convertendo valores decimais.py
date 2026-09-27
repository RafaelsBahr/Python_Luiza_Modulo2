# Crie um programa que peça ao usuário:

# o nome de um jogador;
# sua nota na partida.

# A nota pode possuir casas decimais, como 8.5.

# Converta a nota para o tipo adequado e exiba uma mensagem semelhante a:

# Vinicius recebeu a nota 8.5.

# Antes de finalizar, utilize type() para verificar se a nota foi realmente convertida para o tipo esperado.

nome_jogador = input("Nome do jogador? ")
nota_partida = input("Sua nota na partida? ")

nota_partida = float(nota_partida)
print(type(nota_partida), "\n")

print(f"{nome_jogador} recebeu a nota {nota_partida}.")