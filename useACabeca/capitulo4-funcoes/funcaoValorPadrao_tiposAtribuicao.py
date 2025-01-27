

# Valor de parametro Opcional
# Padrão de Atribuição a POSICIONAL
def search4Vowels(phrase:str, letters:str='aeiou')->set:
    """Retorna um SET com as letras encontradas na frase fornecida"""   
    return set(letters).intersection(set(phrase))

letters = search4Vowels('Paulo Pinheiro', 'xyza')

print(f"Com parametro XYZA: {letters}")
print(type(letters))


letters = search4Vowels('Paulo Pinheiro')

print(f"Sem parametro (Uso do valor opcional): {letters}")

# Atribuição a PALAVRA-CHAVE
letters = search4Vowels(letters='blzau',phrase='Olha só isso, interessante')

print(f"Atribuição a PALAVRA-CHAVE: {letters}")
