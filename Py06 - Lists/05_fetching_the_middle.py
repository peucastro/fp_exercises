def fetch_middle(llists):
    result = []
    for lista in llists:
        if len(lista) % 2 != 0:
            middle = lista[len(lista) // 2]
            result.append(middle)
        else:
            middle = (lista[len(lista) // 2 -1] + lista[len(lista) // 2]) / 2
            result.append(middle)
    return result
