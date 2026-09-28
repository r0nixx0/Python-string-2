# You can remove 'pass' if you written code in the function

# Exercise 1
def is_valid_email(text):
    r=0
    for char in text:
        if char=='@':
            r+=1
        if char=='.':
            r+=1
    if r==2 or r>2:
        return "Valid"
    if r==0 or r==1:
        return "Invalid"
    pass

# Exercise 2
def remove_vowels(text):
    r="aeouiAEOUI"
    f=""
    for char in text:
        if char not in r:
            f=f+char
    return f

    pass

# Exercise 3
def get_initials(text):
    words = text.split()
    r=""
    for word in words:
        r+=word[0].upper()+"."
    return r
    pass

# Exercise 4
def extract_year(text):
    r=""
    l='0123456789'
    for char in text:
        if char in l:
            r=r+char
    return r
    pass

# Exercise 5
def is_palindrome(text):
    text=text.replace(' ','')
    text=text.lower()
    r=text[::-1]
    if text==r:
        return "True"
    else:
        return "False"
    pass
print(is_palindrome("Hello World"))
