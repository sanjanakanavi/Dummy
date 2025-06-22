"""if database is in diff module then instead of writing 'import modulename'
we can also write 'from modulename import dataname' by this u dont have to preattach modulename
in code whenever u use dataname,it will be easier"""


print("*********************")
print('welcome to quiz game')
'question and crt option in a list of dictionaries'
question_bank = [{"text": "the ability of one class to acquire methods and attributes of another class is called____",
                  "answer": "A"},
                 {"text": "which of the following is the type of inheritance?",
                 "answer": "D"},
                 {"text": "what type of inheritance has a multiple subclasses to a single superclass?",
                 "answer": "C"},
                 {"text": "what is the depth of multilevel in heritance in python",
                 "answer": "C"},
                 {"text": "what does mro stand for",
                 "answer": "B"}]

'for options creating  list of lists ,every list has options for every question'
options = [["A. inheritance", "B. abstraction", "C. polymorphism", "D. objects"],
           ["A. single", "B. double", "C. multiple", "D. both A and C"],
           ["A. multiple inheritance", "B. multilevel inheritance",
               "C. hierarchical inheritance", "D. none"],
           ["A. two level", "B. three level", "C. any level", "D. none"],
           ["A. method recursive object", "B. method resolution order", "C. main resolution order", "D. method resolution object"]]
score = 0

'function to check id ans is crt or no'


def check_answer(user_guess, correct_answer):
    if user_guess == correct_answer:  # if crt return true
        return True
    else:
        return False  # else false


# iterationg question bank,passing 1 by 1 dictionary
for question_num in range(len(question_bank)):
    print("********************************")
    print(question_bank[question_num]["text"])
    for i in options[question_num]:  # iterating every list of options list
        print(i)  # it will print contents of list of options list

    guess = input("enter your answer(A/B/C/D)").upper()
    # checking ans by passing guessed ans and crt ans present in item of dictionary of list question bank
    is_correct = check_answer(guess, question_bank[question_num]["answer"])
    if is_correct:  # if crt then score will be added by 1
        print("correct answer")
        score += 1
    else:
        print("incorrect answer")
        # else display the crt answer
        print(f"the correct answer is {question_bank[question_num]['answer']}")
    # printing no of crt answers out of no of attempted questions
    print(f"you score is {score}/{question_num+1}")

print(f"your have given {score} correct answer")  # no of crt answers
# printing percentage of score
print(f"your score is {(score/len(question_bank))*100} %")
