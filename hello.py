#Program Menu Creation
Students = [{
    "Student ID" : 23247194,
    "Student Name" : "Olaoluwa",
    "Student Score": 98
    }]

student_record = {}
Students = [student_record]
while True:
    print("\nStudent Management System\n")
    print()
    print("1. Add Student")
    print("2. View All Student Records")
    print("3. Search by Student ID")
    print("4. Exit")
    print()

    print("Select Operation")
    print()

    #Initializing Student records
   

    #Menu Selection
    user_option = int(input("Enter a Number: "))

    #Students Addition
    if user_option == 1:
        no_s = int(input("Number Of Students to add: "))

    #Looping for repeated entries
        for students in range(no_s):
            student_id = int(input("Enter Student ID: ")),
            student_name = input("Enter Student Name: "),
            student_score = int(input("Enter Student Score: "))

            student_record = {
                "Student ID" : student_id,
                "Student Name" : student_name,
                "Student Score" : student_score
                }

    #Updating Student Records
            Students.append(student_record)
            print(Students)
        
    #All Records Display
    elif user_option == 2:

    #Determining Number of Student Entries
        total_std_no = len(Students)

        if total_std_no == 0:
            print("No Student Record found")

    #Printing Student Records
        else:
            for students in range(total_std_no):
                std_id = Students[student_record["Student ID"]]
                std_name = Students[student_record["Student Name"]]
                std_score = Students[student_record["Student Score"]]

    #Grading System Creation
                if std_score >= 90:
                    grade = "A"

                elif std_score >= 80:
                    grade = "B"

                elif std_score >= 70:
                    grade = "C"

                elif std_score >= 60:
                    grade = "D"

                else:
                    grade = "F"

                print(f"Student ID: {std_id}")
                print(f"Student Name: {std_name}")
                print(f"Student Score: {std_score}")
                print(f"Student Grade: {grade}")
                print()

    elif user_option == 3:
        pass

    elif user_option == 4:
        print("Exiting Program....")
        break

    else:
        print("Operation Not Found, Enter a Valid Number.")