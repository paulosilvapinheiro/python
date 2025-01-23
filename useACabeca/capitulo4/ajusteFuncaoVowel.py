

def search4Vowels(phrase:str, letters:str)->set:
    """Retorna um SET com as letras encontradas na frase fornecida"""   
    return set(letters).intersection(set(phrase))


search4Vowels('Paulo Pinheiro', 'xyza')

letters = search4Vowels('Paulo Pinheiro', 'xyza')

print(letters)
print(type(letters))