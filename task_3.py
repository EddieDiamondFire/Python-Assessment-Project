# This is buggy
import random as r

print("Do you want to roll a die?: ")

response = str(input())

while True:
    if response == "Yes" or "yes":
        print(str(r.randint(1, 6)))

        print("Do you want to roll a die?: ")

        response_1 = str(input())

        if response_1 == "Yes" or "yes":
            print(str(r.randint(1, 6)))
        elif response_1 == "No" or "no":
            print("Okay!")
            break
    elif response == "No" or "no":
        print("Okay!")
        break

exit()
