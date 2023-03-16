num = int(input('Number = '))
while num > 0:
    for c in range(num, 0, -1):
        print(c, end=' ')
    print()
    num -= 1
