# List Comprehension
squares = [x**2 for x in range(10)]
print(f"List Comprehension: {squares}")

# Dictionary Comprehension
square_dict = {x: x**2 for x in range(5)}
print(f"Dictionary Comprehension: {square_dict}")

# Set Comprehension
square_set = {x**2 for x in range(5)}
print(f"Set Comprehension: {square_set}")
