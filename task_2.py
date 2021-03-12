
print("There are 3 questions in the Test")

# Possible answers
question_1_answers = ["orange", "mandarin"]
score = int(0)

print("What is a fruit called when the Colour is Orange?")
answer = str(input())

if answer in question_1_answers:
    print("Correct!")
    print("You scored 1 point")
    score = score + 1
else:
    print("That is incorrect!")

# Possible Answers
possible_question_2 = ["soccer", "football"]
print("What sport is called that involves kicking and passing to each other")

answer_2 = str(input())

if answer_2 in possible_question_2:
    print("Correct!")
    print("You scored 1 point")
    score = score + 1
else:
    print("That is incorrect!")

print("You got " + str(score))






