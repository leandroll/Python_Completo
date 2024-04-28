import traceback


try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0
except:
    # Obtém a mensagem de exceção completa
    mensagem = traceback.format_exc()
    print("Ocorreu um erro:", mensagem)