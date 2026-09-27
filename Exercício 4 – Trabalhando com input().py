# Crie um programa que pergunte ao usuário quantos gols uma seleção marcou em 
# uma partida.

# Depois:

# descubra o tipo do valor recebido diretamente pelo input();
# converta esse valor para int;
# mostre novamente o tipo depois da conversão;
# calcule quantos gols a seleção teria caso marcasse mais um.

# Exemplo de entrada:

# Quantos gols a seleção marcou? 2
# Resultado esperado ao final:
# Com mais um gol, a seleção teria 3 gols.

gols_texto = input("Quantos gols a seleção marcou na partida? ")
print(type(gols_texto))

gols = int(gols_texto)
print(type(gols))

gols_1 = gols + 1

print(f"Com mais um gol, a seleção teria {gols_1} gols.")