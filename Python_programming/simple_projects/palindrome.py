def is_palindrome(palindrome):
    palindrome = palindrome.lower()
    palindrome = ''.join(e for e in palindrome if e.isalnum())
    return palindrome == palindrome[::-1]

string = input("Enter a string: ")
if is_palindrome(string):
    print("Yes, this string is a palindrome.")
else:
    print("No, this string is not a palindrome.")
