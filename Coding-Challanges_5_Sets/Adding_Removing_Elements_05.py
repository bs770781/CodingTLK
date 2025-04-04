# Creating the set
letters = {'a', 'b', 'c'}

# Adding multiple elements using .update()
letters.update({'d', 'e', 'f'})

# Removing 'b' using .discard() (won't raise an error if 'b' is not found)
letters.discard('b')

# Printing the updated set
print(letters)
