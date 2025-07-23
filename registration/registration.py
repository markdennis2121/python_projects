from student import Student

def run_student_input():
    list_of_student = []

    while True:
            try:
                name = input("Enter your name: ").strip()
                while not name:
                    print("⚠️ Name cannot be empty.")
                    name = input("Enter your name: ").lower().strip()

                gender = input("Enter your gender: ").lower().strip()
                while gender not in Student.valid_gender:
                    print("⚠️ Please select (Male / Female)")
                    gender = input("Enter your gender: ").lower().strip()

                course = input("Enter your course: ").lower().strip()
                while course not in Student.valid_course:
                    print("⚠️ Invalid course, please try again.")
                    course = input("Enter your course: ").lower().strip()

                year = input("Enter your year: ").lower().strip()
                while year not in Student.valid_year:
                    print("⚠️ Please input valid year.")
                    year = input("Enter your year: ").lower().strip()

                student = Student(name,gender,course,year)
                list_of_student.append(student)

                ask =input("Want to continue? (y/n): ").lower().strip()
                if ask != "y":
                    print(" ")
                    print(" ")
                    print("=== List of Students ===")
                    break
            except ValueError:
                print("⚠️ Error has been occur, please try again.")
                continue
    with open("students.txt", "a") as file:
        for student in list_of_student:
            seperator = "-" * 24
            info = student.display()

            print(seperator)
            print(info)
            print(seperator)

            file.write(seperator + "\n")
            file.write(info + "\n")
            file.write(seperator + "\n")

if __name__ == "__main__":
    run_student_input()
