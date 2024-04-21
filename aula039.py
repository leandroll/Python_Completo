"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
# qtd_linhas = 5
# qtd_colunas = 5

# linha = 1
# while linha <= qtd_linhas:
#     coluna = 1
#     while coluna <= qtd_colunas:
#         print(f'{linha=} {coluna=}')
#         coluna += 1
#     linha += 1


# print('Acabou')


print("Tabuada multiplicação")
qtd_linhas = 10
qtd_colunas = 10

multiplicando = 0
while multiplicando <= qtd_linhas:
    multiplicador = 1
    while multiplicador <= qtd_colunas:
        produto = multiplicando * multiplicador
        print(f'{str(multiplicando).zfill(3)} " x " {str(multiplicador).zfill(3)} = {str(produto).zfill(3)}')
        multiplicador += 1
    multiplicando += 1




