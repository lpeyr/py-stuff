def rev(s):
    f = ''
    for i in range(len(s)-1, -1, -1):
        f+=s[i]
    return f

def palindrome(s):
    return s == rev(s)

print(palindrome("essayasse"))