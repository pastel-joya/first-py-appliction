student = {}

while True:
    print("\n---Student Management System---")
    print("1. add student")
    print("2. view student")
    print("3. show grade")
    print("4. exit")
    
    choice = input("enter your choice: ")
    
    if choice == '1':
        name = input("enter your name: ")
        number = int(input("enter your marks/number: ")) 
        student[name] = number
        print(f"student {name} added successfully")

    elif choice == '2':
        name = input("enter student name to view: ")
        if name in student:
            print(f"student name is {name}, the number is {student[name]}")
        else:
            print("student not found")

    elif choice == '3':
        name = input("enter student name to see grade: ")
        if name in student:
            score = student[name] 
            if score >= 90:
                print(f"{name} has an A grade")
            elif score >= 80:
                print(f"{name} has a B grade")
            elif score >= 70:
                print(f"{name} has a C grade")
            else:
                print(f"{name} has failed")
        else:
            print("student name is not found")

    elif choice == '4':
        print("exiting....code, goodbye.....")
        break
        
    