num = int(input('Number = '))
divisors_sum = 0
for i in range(1, num+1):
    if num % i == 0:
        divisors_sum += i 
print(divisors_sum)
