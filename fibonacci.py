# Write a program to generate the Fibonacci sequence of a given number.
def generate_fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

num_terms = int(input("Enter the number of Fibonacci terms to generate: "))
fibonacci_sequence = generate_fibonacci(num_terms)
print("Fibonacci sequence:", fibonacci_sequence)
