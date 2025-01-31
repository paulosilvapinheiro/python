#the_stealth_warrior
#The-Stealth-Warrior



def to_camel_case(text):
    
    separador = '-'
    textAux = ''
    print(text)
    for letra in text:
        print(letra.isalpha())
        if letra.isalpha():
            textAux += letra
        else:
            textAux += separador
    
    listPalavras = textAux.split(separador)
    
    for i in range(1,len(listPalavras)):
        listPalavras[i] = listPalavras[i].capitalize()
    
    return ''.join(listPalavras)