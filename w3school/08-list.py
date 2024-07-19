import writeTerminal as wt

_wt = wt.writeTerminal()
# Em Python listas são construidas com [], não é necessário declaração, ou criação de objeto
# Após contrustida já é uma lista

mylist = ["apple", "banana", "cherry"]

# Objeto [LISTA]
_wt.pularLinha()
_wt.printFormat("Tipo lista",type(mylist),True)


# Uma lista pode ter vários tipos diferentes na mesma lista
class myClass:
    name = "myClass"

myObj = myClass()
myObj2 = myClass()

mylist = ["apple", "banana", "cherry", 1, True, 10.34, myObj, myObj2]

_wt.write("Relação de itens da lista")
for n in mylist:
    _wt.printFormat(type(n),n,False)

_wt.pularLinha()

_wt.printFormat("Itens da lista", mylist,True)

_wt.printFormat("Tamanho da lista", len(mylist),True)


#Acessando itens da lista
_wt.write("Acessando itens da lista")

_wt.printFormat("Item 2",mylist[1],True)

_wt.printFormat("Item 6",mylist[6],True)

_wt.printFormat("Objeto do Item 6",mylist[6].name,True)

#Acessando itens da lista [ Range Index ]
_wt.write("Acessando itens da lista por Rande Index")

_wt.printFormat("Itens 2 e 3",mylist[1:3],False)
_wt.printFormat("Itens 5,6 e 7",mylist[4:7],False)
_wt.printFormat("Item 8",mylist[7:8],False)
_wt.printFormat("Itens 3 ao 8",mylist[2:],False)
_wt.printFormat("Itenm 1 ao 4",mylist[:4],False)
_wt.pularLinha()

#Checando se item na lista 
_wt.write("Verificando se item existe")
if 'cherry' in mylist:
    _wt.printFormat("cherry existe na lista?", ( 'cherry' in mylist ),True)

#Replace itens na lista 
_wt.write("Replace itens na lista")

mylist[1] = 'japão'
_wt.printFormat("Replace item 2 da lista por 'japão'",mylist[1],True)

for i in range(len(mylist)):
    if mylist[i] == 10.34:
        mylist[i]=25
        itemSearch = i

_wt.printFormat("Replace 10.34 por 25 na lista",mylist[itemSearch],True)

#Insert itens no meio da lista 
_wt.write("Insert itens no meio da lista")
print(mylist)
print("Inserindo [ melão ] após japão")
mylist.insert(2, "melão")
print(mylist)

_wt.pularLinha()

#Insert itens no meio da lista 
_wt.write("Insert itens no fim da lista")
print(mylist)
print("Inserindo [ melancia ] no final")
mylist.append("melancia")
print(mylist)

_wt.pularLinha()

#Mesclando lista 
_wt.write("Mesclando listas")
listName = ['Pipoca','Lanterninha','Paçoca']
_wt.printFormat("Lista de nomes",listName,False)
listPet = ['Gato','Tigre','Urso']
_wt.printFormat("Lista de nomes",listPet,True)

listName.extend(listPet)
_wt.printFormat("Listas mescladas",listName,True)

#Remove itens da lista 
_wt.write("Remove itens da lista")
listName.remove("Paçoca")
_wt.printFormat("Remove Paçoca",listName,False)

_wt.write("Remove itens da lista por indice")
listName.pop(2)
_wt.printFormat("Remove posição 3 [Gato]",listName,False)

_wt.write("Remove o ultimo item da lista")
listName.pop()
_wt.printFormat("Remove ultima posicao [Urso]",listName,False)

#Limpa a lista 
_wt.write("Limpa lista")
listName.clear()
_wt.printFormat("Limpa lista",listName,False)

#Apaga a lista 
_wt.write("Apaga lista")
del listName
try:
    _wt.printFormat("Lista apagada",listName,True)
except NameError:
    print("listName não existe")
    _wt.pularLinha()

#Ordena a lista 
_wt.write("Sort List")
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
_wt.printFormat("Lista de Itens",thislist,False)
thislist.sort()
_wt.printFormat("Itens ordenados crescentemente",thislist,False)
thislist.sort(reverse=True)
_wt.printFormat("Itens ordenados decrescentemente",thislist,False)

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
_wt.printFormat("Lista de Itens",thislist,False)
thislist.sort(key = myfunc)
_wt.printFormat("Itens ordenados por uma função",thislist,True)

#Copy a lista 
_wt.write("Copy a lista")
thislist = ["apple", "banana", "cherry"]
#Esta acao apenas repassa a mesma lista para a outra variavel tendo assim duas variaveis para a mesma lista
mylist = thislist
mylist[0] = "uva"
_wt.printFormat("Mesmo imprimindo 'thislist' o primeio item é uva",thislist,False)
_wt.printFormat("Lista 'mylist'",mylist,False)
#Pata copiar é necessário
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
mylist[0] = "uva"
_wt.printFormat("Lista 'thislist' o primeio item é apple",thislist,False)
_wt.printFormat("Lista 'mylist' o primeio item é uva",mylist,True)
_wt.write("Another way to make a copy is to use the built-in method list().")
mylist = list(thislist)
mylist[2] = "Paulo"
_wt.printFormat("Lista 'thislist' ",thislist,False)
_wt.printFormat("Lista 'mylist'",mylist,True)


#joins list
_wt.write("JOIN List")

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

_wt.printFormat("Join com append",list1,False)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

# [list1.append(x) for x in list2] 
for x in list2:
    list1.append(x)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
_wt.printFormat("Join com extend",list1,True)