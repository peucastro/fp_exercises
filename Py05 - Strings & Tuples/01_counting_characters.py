def count_chars(a_string):
    
    alphabetic = 0
    digits = 0
    symbols = 0
    
    for char in a_string:
        if char.isalpha() == True:
            alphabetic += 1
        elif char.isnumeric() == True:
            digits += 1
        else:
            symbols += 1
    return(alphabetic, digits, symbols)

