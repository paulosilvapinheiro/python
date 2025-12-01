numbers = [10,1,2,8,7,5,3,9,4,6]

##count = 0
##for i in range(1,len(numbers)):
##
##    print(numbers)
##
##    numeroAtual = numbers[i]
##    iNumComparacao = i - 1
##
##    while numeroAtual < numbers[iNumComparacao] and iNumComparacao >=0:
##        count += 1
##        numbers[iNumComparacao + 1] = numbers[iNumComparacao]
##        iNumComparacao -= 1
##
##    numbers[iNumComparacao + 1] = numeroAtual
##
##print(numbers)
##print(count)

# Exemplo utilizando uma função e uma LAMBDA para atender o parametro de condição

def insertionsort(lista:list, asc:bool)->list:

    for i in range(1,len(lista)):

        numeroAtual = lista[i]
        iNumComparacao = i-1

        if asc:
            condicao = lambda x,y: x < y
        else:
            condicao = lambda x,y: x > y
        #numeroAtual > lista[iNumComparacao]
        while condicao(numeroAtual, lista[iNumComparacao]) and iNumComparacao >=0:
            lista[iNumComparacao + 1] = lista[iNumComparacao]
            iNumComparacao -=1

        lista[iNumComparacao + 1] = numeroAtual
        
    return lista

print(insertionsort(numbers,False))
