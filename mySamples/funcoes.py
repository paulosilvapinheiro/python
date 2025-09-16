

def carregarLista() -> list:
    """Preenche uma lista heterogêna e a retorna para facilitar os exercicios que manipulam listas"""
    myList = [
    'paulo'
    ,41
    ,['banana','maça','pera','uva']
    ,('tv',1000,'rosa') #tupla
    ,{11,13,15,17,19} # conjunto
    ,{1:'amanda',2:'antonio',3:'bianca',4:'bruno'}#dicionario
    ,'pietro'
    ,10.5
    ] #suporta vários tipos (é heterogênea)
    return myList

def imprimirLista(colecao:iter):
    """Imprime os itens de uma coleção"""
    if isinstance(colecao, dict):
        for k,v in colecao.items():
            print(f"chave:{k} \t| valor: {v}")
    else:
        for item in colecao:
            try:
                iter(item)
                if not isinstance(item,str):
                    for i in item:
                        print(i)
                else:
                    print(item)
            except:
                print(item)