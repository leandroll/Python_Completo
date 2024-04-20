a = 'nome 1'
b = 'nome 2'
c = 1.1

string_formatada = 'a={nome1} b={nome2} c={nome3:.2f}'

formato = string_formatada.format(nome1=a, nome2=b, nome3=c)

print(formato)

print(f'\n{a}, {b}, {c:.3f}')