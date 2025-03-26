# Initial list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Even numbers list using list comprehension
even_numbers = [num for num in numbers if num % 2 == 0]

# Squared numbers list using list comprehension
squared_numbers = [num ** 2 for num in even_numbers]

# Print the lists
print(even_numbers)
print(squared_numbers)
