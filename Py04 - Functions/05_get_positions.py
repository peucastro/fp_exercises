def get_positions(sentence, word_list):
    sentence_list = sentence.split()
    if sentence_list[0] not in word_list or sentence_list[1] not in word_list:
        return('')
    if sentence_list[0] == word_list[0]:
        x = str(0)
    elif sentence_list[0] == word_list[1]:
        x = str(1)
    elif sentence_list[0] == word_list[2]:
        x = str(2)
    if sentence_list[1] == word_list[0]:
        y = str(0)
    elif sentence_list[1] == word_list[1]:
        y = str(1)
    elif sentence_list[1] == word_list[2]:
        y = str(2)
    else:
        x = ''
        y = ''
    return(f'{x} {y}')
