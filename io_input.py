def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

something = input("Enter Text: ")

if(is_palindrome(something)):
    print("Palindrome.")
else:
    print("Not a Palindrome.")