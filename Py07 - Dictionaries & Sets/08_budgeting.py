def budgeting(budget, products, wishlist):
    spent = 0
    res = {}
    for i in wishlist:
        spent += wishlist[i] * products[i]
        res[i] = wishlist[i]

    if spent > budget:
        dict_tup = list(products.items())
        dict_tup.sort(key=lambda x: x[1])

        for item in dict_tup:
            if item[0] in res:
                while spent > budget and res[item[0]] > 0:
                    spent -= item[1]
                    res[item[0]] -= 1
            if spent <= budget:
                break

    alist = list(res.items())
    for i in alist:
        if i[1] == 0:
            alist.remove(i)

    return dict(alist)


print(budgeting(750, {'nintendo': 100, 'mouse': 20, 'hoodie': 45, 'backpack': 30, 'tv': 300}, {
      'nintendo': 1, 'mouse': 1, 'hoodie': 4, 'tv': 2}))
