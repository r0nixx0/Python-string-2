# You can remove 'pass' if you written code in the function

# Exercise 1
def is_valid_email(text):
    r=0
    for char in text:
        if char=='@':
            r+=1
        if char=='.':
            r+=1
    if r==2:
        return "Valid"
    if r==0:
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

    pass

# Exercise 4
def extract_year(text):
    # Write your code here
    pass

# Exercise 5
def is_palindrome(text):
    # Write your code here
    pass
