'''
Set
Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is unordered, unchangeable*, and unindexed.
'''

import writeTerminal as wt

_wt = wt.writeTerminal()

mySet = { "Pietro", "Paulo", "Patrizia" }
#Tipo SET
_wt.printFormat("Tipo Set",type(mySet),True)

#Tamanho do Set
_wt.printFormat("Tamanho do set", len(mySet),True)

#Acessando itens

try:
    item = mySet[1]
    _wt.printFormat("Item 2 do SET",item, False)
except:
    print("Não é possivel acessar um SET pelo indice")

_wt.pularLinha()

#Adicionando Itens
_wt.write("Adicionando Itens")
thisset = {"apple", "banana", "cherry"}
_wt.printFormat("Itens do SET",thisset,False)
thisset.add("orange")
_wt.printFormat("Adicionado [orange] \nItens do SET",thisset,False)

anotherthisset = {"cat", "monkey", "dog"}
_wt.printFormat("Itens do SET 2",thisset,False)
thisset.update(anotherthisset)
_wt.printFormat("Adicionado itens do SET 2 \nItens do SET",thisset,True)

#Removendo Itens
_wt.write("Removendo Itens")
thisset.remove("orange")
_wt.printFormat("Removido [orange] \nItens do SET",thisset,False)

#Remove gera exceção
try:
    thisset.remove("Morango")
except:
    print("O item Morango não existe")

thisset.discard("dog")
_wt.printFormat("Descartado [dog] \nItens do SET",thisset,False)

#Discard não gera exceção
try:
    thisset.discard("Lion")
except:
    print("O item Lion não existe")

#Remove item aleatoriamente
thisset.pop()
_wt.printFormat("Item removido aleatóriamente do SET",thisset,False)

#Remove todos os itens
thisset.clear()
_wt.printFormat("Limpa SET",thisset,False)

#Apaga o Set
del(thisset)

try:
    _wt.printFormat("Limpa SET",thisset,False)
except:
    print("O SET não existe [Foi deletado]")

_wt.pularLinha()

#SET loop apenas com for
_wt.write("LOOP SET")
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  _wt.printFormat("Item do Set:",x,False)

_wt.pularLinha()


#JOIN Set
'''
Cria um terceiro SET com a junção dos dois
'''
_wt.write("Joint SET [UNION]")
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
_wt.printFormat("Union dos set",set3,True)

#intersection_update - Mantem apenas os itens em comun (inner join)
#intersection - Igual ao [intersection_update] mas cria um novo SET
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)
_wt.printFormat("Intersection_update set",x,True)

#symmetric_difference_update - Mantem apenas os itens em comun (outter join)
#symmetric_difference - Igual ao [symmetric_difference_update] mas cria um novo SET
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)
_wt.printFormat("Intersection_update set",x,True)   
