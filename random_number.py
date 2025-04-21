
import random

# Generate a random integer between 1 and 100
random_number = random.randint(1, 100)
print(f"Random number: {random_number}")

# If you want to generate a random float between 0 and 1
random_float = random.random()
print(f"Random float: {random_float}")

# Generate a random float within a specific range (e.g., between 1 and 10)
random_range = random.uniform(1, 10)
print(f"Random number between 1 and 10: {random_range}")

# If you want to generate multiple random numbers, you can use a list comprehension
random_list = [random.randint(1, 100) for _ in range(5)]
print(f"List of 5 random numbers: {random_list}")