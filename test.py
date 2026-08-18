#Counter
from ast import While


count_even = 0
count_odd = 0

for Number in range(5):
    Number = int(input("Enter a Number: "))

    if Number % 2 == 0:
        print(f"{Number} is even")
        count_even += 1

    elif Number == ValueError:
        print(f"Input is invalid. Enter a number")

    else:
        print(f"{Number} is odd")
        count_odd += 1

print(f"There are {count_odd} odd numbers.")
print(f"There are {count_even} even numbers.")

#Student Management System

Students =[{
        "Student ID" : 23247194,
        "Student Name" : "Olaoluwa",
        "Student Score" : 79
        }]
student_record = {}

while True:
    print("\nStudent Management System")
    print()
    print("1. Add Student")
    print()
    print("2. View All StudentS")
    print()
    print("3. Search By Student ID")
    print()
    print("4. Exit")
    print()

    print("Choose Operation on the menu")

    user_option = int(input("Select your Operation: "))

    if user_option == 1:
        no_s = int(input("Number of Students to Add: "))


        for i in range(no_s):
            student_ID = int(input("Enter Student ID: "))
            student_Name = input("Enter Student Name: ")
            student_Score = int(input("Enter Student Scores: "))

            student_record = {
            "Student ID" : int(student_ID),
            "Student Name" : student_Name,
            "Student Score" : student_Score
            }

            Students.append(student_record)

        print(Students)

    elif user_option == 2:
        print("\nAll Student Records\n")

        student_no = len(Students)

        
        if student_no == 0:
                print("No Students found!")
        else:
            for students in range(student_no):
                std_id = Students[students]["Student ID"]
                print(f"Student ID: {std_id}")
                std_name = Students[students]["Student Name"]
                print(f"Student Name: {std_name}")
                std_score = Students[students]["Student Score"]
                print(f"Student Score: {std_score}")

                print(f"Student Grade: {grade}")

                if student_Score >= 90:
                    grade = "A"

                elif 80 <= student_Score <= 89:
                    grade = "B"

                elif 70 <= student_Score <= 79:
                    grade = "C"
    
                elif 60 >= student_Score <= 69:
                    grade = "D"

                else:
                    grade = "F"    


    elif user_option == 3:
        std_search = int(input("Enter Student ID: "))
        print("Searching for Student....")


    elif user_option == 4:
        print("Exiting Student Management System")

    else:
        print("Operation not found, Enter a Valid Number: ")


    


   