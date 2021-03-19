import random as r

answer_no = ["No", "no"]
answer_yes = ["Yes", "yes"]
while True:
    print("Do you want to roll a dice?: ")

    response = input()

    if str(response) in answer_yes:
        print(str(r.randint(1, 6)))
        continue
    elif str(response) in answer_no:
        print("Okay")
        break
    else:
        print("Sorry answer properly please!")
        continue
