text = str(input('Phrase: '))
num = int(input('Times: '))
phrase = ('{}-'.format(text)) * num
print(phrase[:-1])
