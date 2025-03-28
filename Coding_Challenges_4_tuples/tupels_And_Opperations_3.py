# Create a tuple with repeated values
fruit_tuple = ("apple", "banana", "apple", "cherry", "banana", "Watermelon", "apple")

# Ask the user to enter a fruit name
fruit_name = input("Enter a fruit name: ")

# Count how many times the fruit appears in the tuple
fruit_count = fruit_tuple.count(fruit_name)

# Print the result
print(f"'{fruit_name}' appears {fruit_count} times in the tuple.")
