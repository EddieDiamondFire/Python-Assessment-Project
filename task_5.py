while True:
    print("Enter the username: ")
    username = input()

    if username == "end":
        break
    print("Enter the User's Exam Mark")
    exam_mark = float(input())

    if exam_mark == "end":
        break

    def check_grade(mark):
        if mark > 55:
            return "A"
        elif mark == 55:
            return "A"
        elif mark > 50:
            return "B"
        elif mark == 50:
            return "B"
        elif mark > 40:
            return "C"
        elif mark == 40:
            return "C"
        elif mark > 30:
            return "D"
        elif mark == 30:
            return "D"
        elif mark < 30:
            return "E"


    print(str(username) + "'s mark is " + str(check_grade(exam_mark)))
