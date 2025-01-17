
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