import random

while True:
    print("Do you want to roll a dice?: ")

    answer = str(input())

    if answer == "yes" or "Yes":
        print(random.randint(1, 6))

        print("Do you want to roll a dice?: ")

        answer_1 = str(input())

        if answer_1 == "yes" or "Yes":
            print(random.randint(1, 6))
        else:
            print("okay")
            break
    elif answer == "no" or "No":
        print("okay")
        break


exit()
