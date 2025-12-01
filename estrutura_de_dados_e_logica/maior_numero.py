def imprimirMaior(a:int,b:int,c:int)->None:
    resultado = None
    if a > b or a > c:
        resultado = a
    elif b > a and b > c:
        resultado = b
    else:
        resultado = c
    print(resultado)

    
imprimirMaior(55,50,100)
