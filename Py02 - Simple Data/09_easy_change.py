price = int(input('Price = '))
recived = int(input('Recived = '))

change = recived - price

fifty = 0
twenty = 0
ten = 0
five = 0

if change >= 50:
    while change >= 50:
        fifty += 1
        change -= 50
        
if change >= 20:
    while change >= 20:
        twenty += 1
        change -= 20

if change >= 10:
    while change >= 10:
        ten += 1
        change -= 10
        
if change >= 5:
    while change >= 5:
        five += 1
        change -= 5

print(str(fifty), str(twenty), str(ten), str(five))
