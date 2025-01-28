
# Estrutura padrão de uma função
def a_descriptive_name(param_func):
    """
        A documentation string: 
        Serve para explicar a funcionalidade 
        e comportamento da função
    """
    #code goes here
    return value_return


# Função documentada no padrão PEP 257
def search4Vowels(word:str)->set:
    """Procura por vogais no Palavra passada""" #docstring
    vowels = set('aeiou')
    # Intersection
    vowels_in_word = vowels.intersection(set(word))
    for vowel in vowels_in_word:
        print(vowel)
    return vowels_in_word


search4Vowels('Paulo Pinheiro')

word = search4Vowels("teste")

print(word)
print(type(word))