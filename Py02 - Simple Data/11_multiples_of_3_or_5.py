n = int(input('Number = '))
divisable = []

for c in range (1, n+1):
    if c % 3 == 0 or c % 5 == 0:
        divisable.append(c)
        
print(sum(divisable))
