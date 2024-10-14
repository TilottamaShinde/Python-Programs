import string

def is_palindrome(s: str) -> bool:
    #Convert the string into lowercase
    s = s.lower()
    s = ''.join(char for char in s if char.isalnum())

    # Compare the cleaned string with its reverse
    return s == s[::-1]

# Example
test_string = "A man, a plan, a canal, Panama!"
print(is_palindrome(test_string))