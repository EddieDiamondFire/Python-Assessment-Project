import random as r


def dice():
    print("Do you want to roll a dice?: ")

    response = str(input())

    answer_no = ["No", "no"]
    answer_yes = ["Yes", "yes"]
    while True:
        if response in answer_yes:
            print(r.randint(1, 6))

            print("Do you want to roll a dice?:")
            response_1 = str(input())

            if response_1 in answer_yes:
                print(r.randint(1, 6))
            elif response_1 in answer_no:
                print("Okay")
                break
            continue
        elif response in answer_no:
            print("Okay")
            exit()


dice()
