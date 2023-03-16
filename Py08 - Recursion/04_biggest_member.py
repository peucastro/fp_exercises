def biggest_member(atuple):
    maxlen = len(atuple)
    out = atuple
    for e in atuple:
        if type(e) == tuple:
            biggest = biggest_member(e)
            if len(biggest) > maxlen:
                maxlen = len(biggest)
                out = biggest

    return out
