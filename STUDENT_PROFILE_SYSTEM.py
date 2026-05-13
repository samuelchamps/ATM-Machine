# Student Profile System

# Welcome message
print("Student Profile System")

# Collect student information
while True:

    student_name = input("Enter the student's name: ")
    student_age = int(input("Enter the student's age: "))
    student_course = input("Enter the student's course: ")
    student_state = input("Enter the student's state: ")

    is_graduated = input(
        "Has the student graduated? (yes/no): "
    ).strip().lower() == 'yes'

    # Subjects list
    subjects = []

    num_subjects = int(input("Enter the number of subjects: "))

    for i in range(num_subjects):
        subject = input(f"Enter the name of subject {i + 1}: ")
        subjects.append(subject)

    # Dictionary
    student_profile = {
        "Name": student_name,
        "Age": student_age,
        "Course": student_course,
        "State": student_state,
        "Subjects": subjects,
        "Graduated": is_graduated
    }

    # Display profile
    print("\n===== STUDENT PROFILE =====")

    for key, value in student_profile.items():
        print(f"{key}: {value}")

    # Ask if user wants to continue
    continue_program = input(
        "\nDo you want to add another student? (yes/no): "
    ).strip().lower()

    # Stop program
    if continue_program == "no":
        print("Program ended.")
        break