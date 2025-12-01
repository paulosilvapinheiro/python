
def imprimirElementos(colecao):
    print(type(colecao))
    if isinstance(colecao,dict):
        for elemento in colecao.keys():
            print(elemento)
    else:
        for elemento in colecao:
            print(elemento)


elementos = ['paulo','lucas', 'pedro','amanda','aline','kelly','bianca','eduardo']
imprimirElementos(elementos)

elementos = ('paulo','lucas', 'pedro','amanda','aline','kelly','bianca','eduardo')
imprimirElementos(elementos)

elementos = {'paulo','lucas', 'pedro','amanda','aline','kelly','bianca','eduardo'}
imprimirElementos(elementos)

elementos = {'paulo':41,'lucas':40, 'pedro':15,'amanda':12,'aline':61,'kelly':51,'bianca':45,'eduardo':32,'aurelio':32,'rita':32,
             'camila':32,'beatriz':32,'luiz':32,'adriana':32}
imprimirElementos(elementos)


