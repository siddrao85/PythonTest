def sum_even_fibonacci(limit):
    a, b = 1, 2  # First two terms of the Fibonacci sequence
    even_sum = 0

    while a <= limit:
        if a % 2 == 0:
            even_sum += a
        a, b = b, a + b  # Generate the next Fibonacci number

    return even_sum

# Set the limit to 4 million
limit = 4_000_000

result = sum_even_fibonacci(limit)

print(f"The sum of even-valued Fibonacci terms not exceeding {limit:,} is: {result:,}")