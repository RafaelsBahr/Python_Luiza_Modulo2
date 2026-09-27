# Crie as seguintes variáveis utilizando Type Hint:

# nome da seleção → texto;
# quantidade de vitórias → número inteiro;
# aproveitamento → número decimal;
# seleção classificada → valor booleano.

# Atribua um valor para cada variável.

# Depois, altere propositalmente uma delas para um valor de outro tipo e observe 
# o comportamento do Python.

# Com base no que aconteceu, responda:

# O Type Hint impede que uma variável receba outro tipo de valor durante a execução?

nome_selecao: str = "Brasil"
qtd_vitorias: int = 3
aproveitamento: float = 4.42
selecao_classificada: bool = True

qtd_vitorias = "Três"

# Type Hint não impede que variável receba outro tipo, apenas da uma dica