import writeTerminal as wt

_wt = wt.writeTerminal()

#A tuple is a collection which is ordered and unchangeable.
''' Ou seja as tuplas são estruturas mais simples nas quais NÃO POSSO:
    -Mudar
    -Adicionar
    -Remover
    -Reordenar os itens
    itens
    '''
mytuple = ("apple", "banana", "cherry")

_wt.printFormat("Uma tupla", mytuple, True)

try:
    mytuple[1] = "paulo"
except:
    print("Tupla não pode ser alterada")

#Tamanho da Tupla
_wt.write("Tamanho da Tupla")
thistuple = ("apple", "banana", "cherry")
_wt.printFormat("O tamnho da tupla",(len(thistuple)),True)

#Tipo Tupla
_wt.printFormat("O tipo da tupla",type(thistuple),True)

#Acessar um item da Tupla
thistuple = ("apple", "banana", "cherry")
_wt.printFormat("Para acessar um item na tupla é da mesma forma que em uma lista { thistuple[1] } ",thistuple[1],False)

#Check if Item Exists
if "bananas" in thistuple: print("banana existe na tupla ") 
else: print("bananas não existe na tupla ")

_wt.pularLinha()

#Change Tuple Values
'''
Tupla não podem se mudadas, então caso seja necessário podemos aplicar algumas manobras para conseguir isso.
'''

#Alterar um valor
x = ("apple", "banana", "cherry")
_wt.printFormat("Tupla origem",x,False)
y = list(x)
y[1] = "kiwi"
x = tuple(y)
_wt.printFormat("Tupla Modificada",x,True)


#Adicionando um item
thistuple = ("apple", "banana", "cherry")
_wt.printFormat("Tupla origem",thistuple,False)
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
_wt.printFormat("Tupla item Adicionado",thistuple,True)

#Removendo um item
thistuple = ("apple", "banana", "cherry")
_wt.printFormat("Tupla origem",thistuple,False)
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
_wt.printFormat("Tupla iten Removido",thistuple,True)

#Unpack Tuples
'''
O ato de inserir valores em uma tupla chamamos de Packing, quando extraímos os valores para variaveis
chamamos este processo de Unpacking
'''
# Packing
fruits = ("apple", "banana", "cherry")

# Unpacking
(green, yellow, red) = fruits
_wt.write("Unpaking tupla")
print(green)
print(yellow)
print(red)

_wt.pularLinha()

#Loop tuples
'''
A forma de dar loops em uma tupla é da mesma forma que em listas
'''
_wt.write("Loop tupla")
thistuple = ("apple", "banana", "cherry")

i = 0
for x in thistuple:
    _wt.printFormat("Item[{0}] da tupla".format(i),x,False)
    i = i +1

_wt.write("Loop tupla comprimida")

[_wt.printFormat("Item[{0}] da tupla".format(i),thistuple[i],False) for i in range(len(thistuple))]

# While loop
i = 0
while i < len(thistuple):
  _wt.printFormat("Item[{0}] da tupla".format(i),thistuple[i],False)
  i = i + 1

#Join Tuplas
_wt.write("Join tuplas")
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
_wt.printFormat("Resultado de tuple3 = tuple1 + tuple2 ",tuple3,True)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
_wt.printFormat("Multiplicação de tuplas (mytuple = fruits * 2) ",mytuple,True)
