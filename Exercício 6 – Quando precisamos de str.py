# Considere:

numero = 10
jogador = "Rodrygo"

# Crie uma mensagem que resulte em:

# O jogador Rodrygo veste a camisa 1.

# Para este exercício, faça a construção da mensagem utilizando +.

# Observe o erro que acontece ao tentar concatenar diretamente numero com os textos
#  e depois utilize str() para corrigir o problema.

# Explique por que a conversão foi necessária.
numero = str(numero)

mensagem = "O jogador " + jogador + "veste a camisa " + numero
print(mensagem)