taks = open('todos.txt')

for chore in taks:
    # print(chore)
    # Por padrão o PRINT adiciona um caracter de quebra de linha, para evitar, usamos o parametro [end]
    # Neste exemplo as linhas de texto impressas já tem o caracter de comando de QUEBRA DE LINHA por isso suprimimos a QUEBRA DE LINHA do PRINT
    print(chore,end='')