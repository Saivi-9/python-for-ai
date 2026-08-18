Students = [{
    "id": 23247194,
    "name": "Olaoluwa",
    "score": 79
}]

student_record = {}

while True:
    print("\nStudent Management System")
    print()
    print("1. Add Student")
    print()
    print("2. View All Students")
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
            student_Score = int(input("Enter Student Score: "))

            student_record = {
                "id": student_ID,
                "name": student_Name,
                "score": student_Score
            }

            Students.append(student_record)

        print("\nStudent(s) Added Successfully!")

    elif user_option == 2:
        print("\nAll Student Records\n")

        student_no = len(Students)

        if student_no == 0:
            print("No Students found!")
        else:
            for students in range(student_no):

                std_id = Students[students]["id"]
                std_name = Students[students]["name"]
                std_score = Students[students]["score"]

                if std_score >= 90:
                    grade = "A"
                elif 80 <= std_score <= 89:
                    grade = "B"
                elif 70 <= std_score <= 79:
                    grade = "C"
                elif 60 <= std_score <= 69:
                    grade = "D"
                else:
                    grade = "F"

                print(f"Student ID: {std_id}")
                print(f"Student Name: {std_name}")
                print(f"Student Score: {std_score}")
                print(f"Student Grade: {grade}")
                print()

    elif user_option == 3:
        std_search = int(input("Enter Student ID: "))
        print("Searching for Student...\n")

        found = False

        for student_record in Students:
            if student_record["id"] == std_search:

                std_score = student_record["score"]

                if std_score >= 90:
                    grade = "A"
                elif 80 <= std_score <= 89:
                    grade = "B"
                elif 70 <= std_score <= 79:
                    grade = "C"
                elif 60 <= std_score <= 69:
                    grade = "D"
                else:
                    grade = "F"

                print(f"Student ID: {student_record['id']}")
                print(f"Student Name: {student_record['name']}")
                print(f"Student Score: {student_record['score']}")
                print(f"Student Grade: {grade}")

                found = True
                break

        if not found:
            print("Student Not Found!")

    elif user_option == 4:
        print("Exiting Program...")
        break

    else:
        print("Operation not found, Enter a Valid Number.")