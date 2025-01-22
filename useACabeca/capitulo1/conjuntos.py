vowels = {'a','e','i','o','u'}
word = "Paulo"

# Intersection
vowels_in_word = vowels.intersection(set(word))

print(vowels_in_word)

# Union
vowels_in_word = vowels.union(set(word))

print(vowels_in_word)

# Difference
vowels_in_word = vowels.difference(set(word))

print(vowels_in_word)
