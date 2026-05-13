"""
A school system converts numerical scores to letter grades. 
Build the grading logic with proper elif chains.

"""
score = float(input("Enter the student's score: "))
if score >= 70 and score <= 100:
    grade = 'A'
elif score >= 60 and score < 70:
    grade = 'B'
elif score >= 50 and score < 60:
    grade = 'C'
elif score >= 40 and score < 50:
    grade = 'D'
elif score >= 0 and score < 40:
    grade = 'F'
else:
    grade = 'Invalid score'

if score >= 40:
    print(f"Pass")
else:
    print(f"Fail")

print(f"The student's grade is: {grade}")