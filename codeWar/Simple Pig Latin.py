import string

def test(text):
    fisrtLetter = ''
    sliceWord = ''
    sufixo = 'ay'
    newWord = ''
    newText = []
    for word in text.split(" "):
        if word not in string.punctuation:
            fisrtLetter = word[0]
            sliceWord = word[1:]
            newWord = sliceWord + fisrtLetter + sufixo
            newText.append(newWord)
        else:
            newText.append(word)

    return " ".join(newText)

print(test('Paulo da silva pinheiro !'))

       
