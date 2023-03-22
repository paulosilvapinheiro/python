
valor = 5
valor2 = 1

#A identação é importante, neste exemplo se não identar temos uma exception de [ IndentationError ]
# if valor > 2:
# print("5 is greater than 2!!!")


#todo o bloco deve estar na mesma identação : exception de [ IndentationError ]
# if valor > 2:
#         print("5 is greater than 2!!!")
#     print("mensagem fora do if")

#o proximo comando não identado inicia a nova instrução
if valor > valor2:
    print(valor , " is greater than ", valor2, " !!!!")
print("mensagem fora do if")


"""
bloco de comentário são abertos com 3 aspas
dentro do bloco podemos escrever um comentário 
de várias linhas
"""