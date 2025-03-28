# Ask the user to input two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Swap the values using tuple unpacking
a, b = b, a

# Print the swapped values
print("Swapped values:", (a, b))
  