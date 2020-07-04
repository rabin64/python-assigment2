#12. Create a function, is_palindrome, to determine if a supplied word is
#the same if the letters are reversed.

def is_palindrome(val):
    if val == val[::-1]:
        return True
    else:
        return False

s=input("enter a string to check:")
print(is_palindrome(s))