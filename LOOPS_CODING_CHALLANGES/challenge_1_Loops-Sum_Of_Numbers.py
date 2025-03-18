# Ask the user for a number
n = int(input("Enter a number: "))

# Initialize the sum variable
total_sum = 0

# Loop through numbers from 1 to n (inclusive)
for i in range(1, n + 1):
    total_sum += i

# Output the sum
print(f"Sum = {total_sum}")

