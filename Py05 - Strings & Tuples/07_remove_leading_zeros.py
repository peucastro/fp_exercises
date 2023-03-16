def remove_leading(ip):
    ip_list = ip.split('.')
    res = []
    for num in ip_list:
        if num[0] != '0':
            res.append(num)
        elif int(num) == 0:
            res.append('0')
        elif num[0] == '0':
            res.append(num[1:])
    return '.'.join(res)
