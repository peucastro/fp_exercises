def most_frequent(alist):
    dict = {}

    for e in alist:
        if e not in dict:
            dict[e] = 1

        else:
            dict[e] += 1

    return max(dict, key=dict.get)
