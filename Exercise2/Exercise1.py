while True:
    score_input = input("Enter the student's score: ")
    
    # Check if input is a number
    if not score_input.isdigit():
        print("Please enter a valid number.")
        continue
    
    score = int(score_input)

    if score >= 80:
        print("Grade: A")
    elif score >= 70:
        print("Grade: B")
    elif score >= 60:
        print("Grade: C")
    elif score >= 50:
        print("Grade: D")
    elif score >= 40:
        print("Grade: E")
    elif score >= 30:
        print("Grade: F")
    else:
        print("Grade: Below F")

    break