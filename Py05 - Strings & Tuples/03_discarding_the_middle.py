def discard_middle(s):
    
    if len(s) <= 4:
        return ''
    
    else:
        return str(s[0] + s[1] + s[-2] + s[-1])
