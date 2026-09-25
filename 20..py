
marks = float(input("Enter your marks (0 - 100): "))


if marks >= 90 and marks <= 100:
    grade = 'A+'
elif marks >= 80:
    grade = 'A'
elif marks >= 70:
    grade = 'B'
elif marks >= 60:
    grade = 'C'
elif marks >= 50:
    grade = 'D'
elif marks >= 0:
    grade = 'F (Fail)'
else:
    grade = "Invalid marks! Please enter a value between 0 and 100."

print("Grade:", grade)
