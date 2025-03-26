# Initial list of students
students = [['Alice', 25, 'Physics'], ['Bob', 22, 'Chemistry'], ['Charlie', 24, 'Biology']]

# Change Bob's age to 23 and his major to 'Mathematics'
students[1][1] = 23  # Update Bob's age
students[1][2] = 'Mathematics'  # Update Bob's major

# Print the updated students list
print(students)

# Access and print the name of the student who is studying 'Biology'
for student in students:
    if student[2] == 'Biology':
        print(student[0])  # Print the name of the student studying Biology
