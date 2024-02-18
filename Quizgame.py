print("Welcome to computer Quiz")
play=input("Do you want to play?")
if play.lower().strip()!="yes":
    print("okay bye")
else:
    print(" ok Lets begin")
    score=0
    ques=input("what does CPU stands for?")
    if ques.lower().strip()=="central processing unit":
        print("correct!")
        score+=1
    else:
        print("Incorrect")
    ques=input("what does HCI stands for?")
    if ques.lower().strip()=="human computer interaction":
        print("correct")
        score+=1
    else:
        print("Incorrect")
    ques=input("what does GPS stands for?")
    if ques.lower().strip()=="global positioning system":
        print("correct")
        score+=1
    else:
        print("Incorrect")
    ques=input("What does RAM stands for?")
    if ques.lower().strip()=="random access memory":
        print("correct")
        score+=1
    else:
        print("Incorrect")
    ques=input("What does GUI stands for?")
    if ques.lower().strip()=="graphical user interface":
        print("Correct")
        score+=1
    else:
        print("Incorrect")
    print("you got "+ str(score) + " questions correct!")
    print("you got "+ str((score / 5) * 100) + "%")
          
    
    







    





            

