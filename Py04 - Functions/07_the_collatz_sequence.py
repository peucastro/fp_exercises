def collatz(n):
    previous = n
    list_c = [str(n)]
    next = 0

    while next != 1:
        if previous == 1:
            list_c = [str(1)]
            next = 1
        elif previous % 2 == 0:
            next = int(previous / 2)
            list_c.append(str(next))
            previous = next
        elif previous % 2 != 0:
            next = int(previous * 3 + 1)
            list_c.append(str(next))
            previous = next

    return(','.join(list_c))
