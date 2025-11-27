# Take input from the students that can attend the exam or not
Medical_Cause = input ("Did you have a medical cause or not. Yes or No: ")
#Take input of the attendence
attendence = int(input("Enter the attendence of the student"))

#Checking the user input predicting output accordingly

if Medical_Cause == 'Yes': #checking the condition
    print("You are allowed to particpate in the IBT exam")
else:
    if attendence>=75:
        print("You are allowed to particpate in the IBT exam")
    else: 
     print("You are not permitted to participate in the IBT exam")
