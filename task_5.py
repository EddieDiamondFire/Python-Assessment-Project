username = input()

exam_mark = float(input())


def check_grade(mark):
    if mark > 55:
        return "A"
    elif mark > 50:
        return "B"
    elif mark > 40:
        return "C"
    elif mark > 30:
        return "D"
    elif mark < 30:
        return "E"


print(check_grade(exam_mark))
