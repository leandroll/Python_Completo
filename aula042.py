""" while/else """
string = input("Digite algo, se houver espaço o que vier após o espaço será desconsiderado: ")

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('Não encontrei um espaço na string.')

print('Fim do programa') # sempre serr executado idependente do resultado do while/else