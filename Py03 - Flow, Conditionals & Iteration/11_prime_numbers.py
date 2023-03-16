lower = int(input('lower = '))
upper = int(input('upper = '))
listp = []

for num in range(lower, upper+1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           listp.append(num)

lists = map(str, listp)

print('Prime numbers between {} and {} are: {}'.format(lower, upper, ' '.join(lists)))
