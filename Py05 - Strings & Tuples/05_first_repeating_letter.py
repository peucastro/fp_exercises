def repeated_letter(s):
    list_l = []
    
    for l in list(s):
        if l not in list_l:
            list_l += l
        elif l in list_l:
            return l
    return None
        
