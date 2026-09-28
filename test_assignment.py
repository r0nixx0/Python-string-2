import pytest
from assignment import (
    is_valid_email,
    remove_vowels,
    get_initials,
    extract_year,
    is_palindrome
)

# Exercise 1: Valid email check
@pytest.mark.parametrize("email, expected", [
    ("hello@gmail.com", "Valid"),
    ("user.name@domain.co", "Valid"),
    ("hellogmail.com", "Invalid"),
    ("name@", "Invalid"),
])
def test1(email, expected):
    assert is_valid_email(email) == expected


# Exercise 2: Remove vowels
@pytest.mark.parametrize("text, expected", [
    ("Please call me tomorrow", "Pls cll m tmrrw"),
    ("Python is amazing", "Pythn s mzng"),
    ("AEIOUaeiou", ""),
])
def test2(text, expected):
    assert remove_vowels(text) == expected


# Exercise 3: Get initials
@pytest.mark.parametrize("name, expected", [
    ("elon musk", "E.M."),
    ("Ada Lovelace", "A.L."),
    ("grace hopper", "G.H."),
    ("alan mathison turing", "A.M.T."),
])
def test3(name, expected):
    assert get_initials(name) == expected


# Exercise 4: Extract year
@pytest.mark.parametrize("sentence, expected", [
    ("I was born in 2008", "2008"),
    ("World Cup 2010 was amazing!", "2010"),
    ("No year here!", False),
    ("My ID number is 12345", False),
])
def test4(sentence, expected):
    assert extract_year(sentence) == expected


# Exercise 5: Palindrome check
@pytest.mark.parametrize("text, expected", [
    ("Never odd or even", True),
    ("Hello World", False),
    ("A man a plan a canal Panama", True),
    ("Was it a car or a cat I saw", True),
    ("Random text", False),
])
def test5(text, expected):
    assert is_palindrome(text) == expected
