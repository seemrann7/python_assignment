# Write a program to find prime number with in a range using function.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def primes_in_range(start, end):
    primes = [num 
              for num in range(start, end+1) 
              if is_prime(num)]
    return primes

start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))
prime_numbers = primes_in_range(start_range, end_range)
print("Prime numbers in the given range:", prime_numbers)

