def get_grade_message(grade, subject):
    if grade >= 101:
        return f"You got an A+ in {subject}. Good job you're in a HON's class."
    elif grade >= 94 or grade == 100:
        return f"You got an A in {subject}. Good job, keep it up."
    elif grade >= 90:
        return f"You got an A- in {subject}. Good job, keep it up."
    elif grade >= 87:
        return f"You got a B+ in {subject}. Try a little harder on the next assignment."
    elif grade >= 83:
        return f"You got a B in {subject}. Try a little harder on the next assignment."
    elif grade >= 80:
        return f"You got a B- in {subject}. Try a little harder on the next assignment."
    elif grade >= 77:
        return f"You got a C+ in {subject}. Try a little harder on the next assignment."
    elif grade >= 73:
        return f"You got a C in {subject}. Try a little harder on the next assignment."
    elif grade >= 70:
        return f"You got a C- in {subject}. Try a little harder on the next assignment."
    elif grade >= 67:
        return f"You got a D+ in {subject}. You are going to FAIL if you get a lower grade."
    elif grade >= 60:
        return f"You got a D in {subject}. You are going to FAIL if you get a lower grade."
    else:
        return f"You got an F in {subject}. You are going to FAIL this term. So try and get your grades up, and try to stay after if you can."

def college_grade_convert():
    try:
        first_number = float(input("Please enter the top number in your college grade list: "))
        second_number = float(input("Please enter the bottom number in your college grade list: "))
        
        if first_number == "" or second_number == "":
            print("Please enter a number in your college grade list")
        else:
            output = first_number / second_number
            print(f"Your grade is: {output}")
    except ValueError:
        print("ERROR: Please enter valid numbers")

# Example usage:
grade = int(input("Enter the grade: "))
subject = input("Enter the subject: ")
print(get_grade_message(grade, subject))

college_grade_convert()
