# Step 1: Create a frozenset
frozen_numbers = frozenset({1, 2, 3, 4, 5})

# Step 2: Try to add an element to the frozenset (this will raise an error)
try:
    frozen_numbers.add(6)
except AttributeError as e:
    print(f"Error: {e}")

# Step 3: Print the frozenset
print(frozen_numbers)
