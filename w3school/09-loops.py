import writeTerminal as wt

_wt = wt.writeTerminal()

thislist = ["apple", "banana", "cherry"]
_wt.write("Loop FOR Método 1")
for x in thislist:
  print(x)

_wt.write("Loop FOR Método 2")
for i in range(len(thislist)):
  print(thislist[i])

_wt.write("Loop WHILE")
i = 0

while i <  len(thislist):
  print(thislist[i])
  i=i+1

_wt.write("Looping Using List Comprehension")
_wt.write("Loop FOR Comprehension Método 1")
[print(x) for x in thislist]
_wt.write("Loop FOR Comprehension Método 2")
[print(thislist[i]) for i in range(len(thislist))]

_wt.write("Criando uma nova lista com frutas que contenham 'a'")
_wt.write("Loop for SEM Comprehension")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

_wt.write("Loop for COM Comprehension")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist =[x for x in fruits if "a" in x]
print(newlist)

_wt.write("Criando uma nova lista com frutas que contenham 'a' e replace 'n' por 'b'")
_wt.write("Loop for SEM Comprehension")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    if 'n' in x:
        x = x.replace('n','b')
    newlist.append( x )

print(newlist)

_wt.write("Loop for COM Comprehension")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist =[x.replace('n','b') if 'n' in x else x for x in fruits if "a" in x]
print(newlist)

