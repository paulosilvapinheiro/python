from mediana import mediana

def test_is_impar(lista:list)->bool:
    return len(lista)%2==1

def calc_quartis_exc(lista:list)->list:
    is_impar = test_is_impar(lista)
    result = []

    if len(lista) > 3:
        if is_impar:
            #calcula Q2
            result.append(mediana(lista))

            #calcula Q1
            result.append(int(mediana(lista[0:int(len(lista)/2)])))

            #calcula Q3
            result.append(int(mediana(lista[int(len(lista)/2)+1:len(lista)])))
        else:
            #calcula Q2
            result.append(int(mediana(lista)))

            #Variaveis para calcular Q1 e Q3
            base = len(lista)+1
            n = len(lista)

            kq1 = 1
            iq1 = kq1 * ( base/4 )
            jq1 = int(iq1)
            fq1 = iq1-int(iq1)
            v1q1 = lista[jq1-1]
            v2q1 = lista[jq1]
            
            kq3 = 3
            iq3 = kq3 * ( base/4 )
            jq3 = int(iq3)
            fq3 = iq3-int(iq3)
            v1q3 = lista[jq3-1]
            v2q3 = lista[jq3]

            q1 = v1q1 + (fq1 * ( v2q1 - v1q1 ))
            q3 = v1q3 + (fq3 * ( v2q3 - v1q3 ))

            result.append(q1)
            result.append(q3)
    else:
        result.extend(lista)
        
    return result


print(sorted(calc_quartis_exc([10,20,30,40,50,60,70,80])))
        



