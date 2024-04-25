"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# for letra in texto
#texto = 'Leandro'  # iterável

# iteratador = iter(texto)  # iterator

# while True:
#     try:
#         letra = next(iteratador)
#         print(letra)
#     except StopIteration:
#         break

# for letra in texto:
#     print(letra)

#-------------

texto = 'Leandro'  # iterável

iteratador = iter(texto)  # iterator
qtd_letra = 1

while qtd_letra <= len(texto):
        letra = next(iteratador)
        print(letra)
        qtd_letra += 1
       


