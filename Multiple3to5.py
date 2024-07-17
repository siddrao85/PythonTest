def sum_of_multiples(limit):
    total = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

# Calculate the sum of multiples of 3 or 5 below 1000
result = sum_of_multiples(1000)

print(f"The sum of all multiples of 3 or 5 below 1000 is: {result}")