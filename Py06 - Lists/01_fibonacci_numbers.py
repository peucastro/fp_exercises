def fib(n):
    
    list_n = [0,1]

    if n == 1:
        return [0]
    for i in range(n+1):
            prev_1 = list_n[i]
            prev_2 = list_n[i+1]
            num = int(prev_1 + prev_2)
            list_n.append(num)
            if len(list_n) == n:
                return list_n
            
    return list_n
