# Write a program to check palindrome.
def is_palindrome(string):
    return string == string[::-1]

word = input("Enter a word to check if it's a palindrome: ")
if is_palindrome(word):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")