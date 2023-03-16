def lost_element(s1, s2):
    if len(s1) > len(s2):
        res = list(s1 - s2)
    else:
        res = list(s2 - s1)
    return res[0]
