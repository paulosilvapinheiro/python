
vowels = ['a','e','i','o','u']
word = "Paulo da Silva Pinheiro"
found = []

dicVowels = {}

for letter in word:
    if letter in vowels:
        if letter in dicVowels:
            dicVowels[letter] += 1
        else:
            dicVowels[letter] = 1

        if letter not in found:
            found.append(letter)
            print(letter)

for vowels in dicVowels:
    print(f"vogal:{vowels} : {dicVowels[vowels]}")

# O dicionario é uma estrutura não ordenada (UNSORTED)
# Para ter um retorno ordenado usar o funcão nativa SORTED()

print("\n Exemplo ordenado [SORTED()]")

for vowels in sorted(dicVowels):
    print(f"vogal:{vowels} : {dicVowels[vowels]}")


print("\n Uso do método Items() do dicionário")

print(f"tipo do retorno do método ITEMS(): {type(dicVowels.items())}")
print(f"O tipo [dict_items] retorna uma TUPLA quando iterado")

for key,value in sorted(dicVowels.items()):
    print(f"vogal:{key} : {value}")