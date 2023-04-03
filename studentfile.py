while True:
    lastname = input("Please type last name (or type 'ZZZ' to quit): ")
    if lastname == "ZZZ":
        break
    firstname = input("Please type student first name: ")
    gpa = float(input("Please enter student's GPA: "))
    if gpa >= 3.5:
        print(f"{firstname} {lastname} has made both the Dean's List and Honor Roll.")
    elif gpa >= 3.25:
        print(f"{firstname} {lastname} has made the Honor Roll.")
    else:
        print(f"{firstname} {lastname} does not qualify for either the Dean's List or the Honor Roll.")