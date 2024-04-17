# alguns caracteres de scape \r (retorno de carro \n (nova linha) -> CRLF windows versão antiga e as novas
# \n -> LF unix
# obs: print já faz quebra de linha automaticamente sem precisar dos scapes acima
print(12, 34, 105, sep ='-', end = '\r\n')
print(56, 78, sep ="========", end = '\n')
print(1, 2, 3, sep ="," , end = '#\n') 
print(1, 2, 3, sep =",") 