n = int(input())
if n >= 0 and n <= 9:
    print("Looping number")
else:
    while n >= 10:
        temp1 = n % 10
        n = n // 10
        temp2 = n % 10
        if temp2 == (temp1+1) or temp2 == (temp1-1):
            resultado = True  
        else:
            resultado = False
            break
    if resultado == True:
        print("Looping number")
    if resultado == False:
        print("Not a looping number")
