# Ask the user to enter their score
#Made By Bilal Shamsi
#Making a grading system for kids to see there marks
score = int(input("Enter your score: "))

# Use conditional statements to determine the grade
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
