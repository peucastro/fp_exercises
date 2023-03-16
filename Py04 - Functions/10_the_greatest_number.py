def greatest(num):
    alist = list(str(num))
    alist.sort()
    alist.reverse()
    res = ''.join(alist)
    return int(res)


print(greatest(128325))
