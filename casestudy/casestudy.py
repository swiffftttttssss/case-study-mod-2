#Aseel Ibrahinm
#casestudy.py
#This app will accept students names and gpas and test if the student qualifies for either the deans list or honor roll is the gpa is 3.5 or higher he/she qualifies for the deans list, if the student has a 3.25 or higher they have made the Honor roll

lastname = input("Please Type Last Name: ")
while lastname != "ZZZ":
    firstname = input("Please Type Student First Name: ")
    gpa = float(input("Please Enter Students GPA: "))
    if gpa >= 3.5:
        print("{} {} has made the Dean's List.".format(firstname, lastname))
    else:
        if gpa >= 3.25:
            print("{} {} has made the Honor Roll.".format(firstname, lastname)) 
    lastname = input("\nEnter Student Last Name: ")
