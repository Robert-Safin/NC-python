# A phrase is a palindrome if, after converting all uppercase letters
# into lowercase letters and removing all non-alphanumeric characters,
# it reads the same forward and backward. Alphanumeric characters include
# letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.



def isPalindrome(s: str) -> bool:

    clean_str = ''
    for c in s:
        if c.isalpha() or c.isdigit():
            clean_str += c.capitalize()

    LEFT = 0
    RIGHT = len(clean_str) - 1

    while LEFT < RIGHT:
        if clean_str[LEFT] != clean_str[RIGHT]:
            return False
        LEFT += 1
        RIGHT -= 1

    return True



s = "A man, a plan, a canal: Panama"
print(isPalindrome(s)) # True


s = "race a car"
print(isPalindrome(s)) # False
