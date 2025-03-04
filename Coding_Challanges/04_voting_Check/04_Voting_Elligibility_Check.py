# Ask the user to enter their age for voting
#Made By Bilal Shamsi
#Purpose to see if user is eligble to vote
age = int(input("Enter your age: "))

# Check if the person is eligible to vote for the election
if age >= 18:
    print("You are eligible to vote!")
else:
    print("Sorry, you are not eligible to vote yet.")
