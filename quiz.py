print ("WELCOME TO THE QUIZ!!")

list1 = ["Are you reading this?","What is the capital of india?", "What is the full form of WWW?"," Which state of India is known as pink city?"  ]
list2 = ["yes","new delhi" , "world wide web", "jaipur", ]
score = 0
for i in range (4):
    ques = list1[i] + "\n"
    ans = list2[i]
    
    input_ans = input(ques)
    
    if (input_ans == list2[i]):
        print("correct answer")
        score += 1

    else:
        print("incorrect answer")
        print ("the correct answer is:")
        print (list2[i])

print("Your score :", score)