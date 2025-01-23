
def search4Vowels(phrase:str, letters:str='aeiou')->set:
    """Retorna um SET com as letras encontradas na frase fornecida"""   
    return set(letters).intersection(set(phrase))