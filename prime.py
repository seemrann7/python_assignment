# Write a program to find prime number with in a range using function.
# Write a program to generate the Fibonacci sequence of a given number.
# Create a number guessing game. Where you have to generate a random number in between 1 to 100 and user have to prompt a number for guess.
# if its high or low number let the user know and guide them through the process to guess correct number.
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# def primes_in_range(start, end):
#     primes = [num 
#               for num in range(start, end+1) 
#               if is_prime(num)]
#     return primes

# start_range = int(input("Enter the start of the range: "))
# end_range = int(input("Enter the end of the range: "))
# prime_numbers = primes_in_range(start_range, end_range)
# print("Prime numbers in the given range:", prime_numbers)

# Write a program to check palindrome.
def is_palindrome(string):
    return string == string[::-1]

word = input("Enter a word to check if it's a palindrome: ")
if is_palindrome(word):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
