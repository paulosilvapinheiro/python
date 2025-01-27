
vowels = ['a','e','i','o','u']
word = "Paulo da Silva Pinheiro"
found = []

for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
            print(letter)


# Método Remove
# Remove primeiro item com o VALOR correspondente

nums = [1,2,3,4]

nums.remove(3)

print(nums)

# Método Pop
# Remove pelo indice ou o ultimo caso não seja passado parametro

nums.pop(2)

print(nums)

# Método Extend 
# Combina duas lista

nums2 = [5,6,7,8,9,10]

nums.extend(nums2)
print(nums)

# Método Insert 
# Inseri um item em uma posição especifica, a esquerda do INDICE especificado

nums.insert(3, "Paulo")
print(nums)

# Método Copy
# Como listas são objetos, se copiar utilizando o operador de atribuição [=] na verdade esta 
# apenas duplicando as variaveis apontando para a mesma lista.
# para criar uma lista independente use COPY

lista1 = [10,20,30,40]
lista2 = lista1.copy()
lista2.extend([50,60,74])

print(lista1)
print(lista2)

# Acessando um item com indice negativo

print(lista1[-2])

# Fatiando uma lista (slice)
# lista[START:STOP:STEP]

print(lista2[2::2])
print(lista2[::3])
print(lista2[3:5:])

# Método Join
# Tranforma em string

lista3 = ['p','a','u','l','o']
nome = ''.join(lista3)

print(lista3)
print(nome)

print(type(lista3))
print(type(nome))