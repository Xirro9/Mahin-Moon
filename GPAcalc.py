#This program will allow users to calcualte their gpas by inputting all their letter grades.
#forever loop until user inputs the stop command. 
grade = 0 
total = 0
num = 0 
interatons = 0 
while grade != "":
    #promt the user to input all their letter grades
    grade = input("enter your letter grade, press enter when finished: ").upper()
    #assign letters to number values, get nnumbers, gets the amount of grades, and totals the gpa
    if grade == 'A':
        num = 4
        total = total + num
        interatons = interatons + 1
    elif grade == 'B':
        num = 3
        total = total + num
        interatons = interatons + 1
    elif grade == 'C':
        num = 2
        total = total + num
        interatons = interatons + 1
    elif grade == 'D':
        num = 1
        total = total + num
        interatons = interatons + 1
    elif grade == 'F':
        num = 0
        total = total + num
        interatons = interatons + 1
    else:
        if grade == "":
            print("")
        else:
            print("That was not a valid input") 
    #stop loop note: i figured out a better way to do this
    #stop = input("\npress enter to continue, type P if you are finished.").upper()
#print the gpa
gpa = total / interatons
print("\nYour final gpa is: "f"{gpa: .3f}")
input('Press ENTER to exit')