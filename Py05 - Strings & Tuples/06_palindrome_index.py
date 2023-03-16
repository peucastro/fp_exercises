def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False


def palindrome_index(s):
    if palindrome(s):
        return -1

    for i in range(len(s)):
        string = s[0:i] + s[i+1:]
        if palindrome(string):
            return i

    return -1
