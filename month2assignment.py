# =========================================
# CLI Student Management System
# =========================================

import os


# =========================================
# STUDENT CLASS (OOP)
# =========================================
class Student:
    def __init__(self, name, age, program, contact):
        self.name = name.title()
        self.age = age
        self.program = program.title()
        self.contact = contact

    def __str__(self):
        return f"{self.name},{self.age},{self.program},{self.contact}"


# =========================================
# FILE NAMES
# =========================================
STUDENT_FILE = "students.txt"
USER_FILE = "users.txt"


# =========================================
# CREATE DEFAULT USER
# =========================================
def create_default_user():
    """
    Creates a default login if users.txt does not exist
    Username: admin
    Password: admin123
    """
    if not os.path.exists(USER_FILE):
        with open(USER_FILE, "w") as file:
            file.write("admin,admin123\n")


# =========================================
# LOGIN SYSTEM
# =========================================
def login_system():
    print("\n========== LOGIN SYSTEM ==========")

    username = input("Enter Username: ").strip()
    password = input("Enter Password: ").strip()

    try:
        with open(USER_FILE, "r") as file:
            users = file.readlines()

            for user in users:
                saved_username, saved_password = user.strip().split(",")

                if username == saved_username and password == saved_password:
                    print("\nLogin Successful!\n")
                    return True

            print("\nInvalid Username or Password!\n")
            return False

    except FileNotFoundError:
        print("User file not found!")
        return False


# =========================================
# LOAD STUDENTS FROM FILE
# =========================================
def load_students():
    students = []

    if os.path.exists(STUDENT_FILE):
        try:
            with open(STUDENT_FILE, "r") as file:
                lines = file.readlines()

                for line in lines:
                    data = line.strip().split(",")

                    if len(data) == 4:
                        student = Student(
                            data[0],
                            data[1],
                            data[2],
                            data[3]
                        )
                        students.append(student)

        except Exception as e:
            print("Error loading students:", e)

    return students


# =========================================
# SAVE STUDENTS TO FILE
# =========================================
def save_students(students):
    try:
        with open(STUDENT_FILE, "w") as file:
            for student in students:
                file.write(str(student) + "\n")

        print("\nStudents saved successfully!\n")

    except Exception as e:
        print("Error saving students:", e)


# =========================================
# ADD STUDENT
# =========================================
def add_student(students):
    print("\n========== ADD STUDENT ==========")

    name = input("Enter Student Name: ").strip()

    # AGE VALIDATION
    while True:
        age = input("Enter Age: ").strip()

        if age.isdigit():
            break
        else:
            print("Invalid input! Age must contain numbers only.")

    program = input("Enter Program/Class: ").strip()

    # CONTACT VALIDATION
    while True:
        contact = input("Enter Contact Number: ").strip()

        if contact.isdigit():
            break
        else:
            print("Invalid input! Contact number must contain numbers only.")

    student = Student(name, age, program, contact)
    students.append(student)

    print("\nStudent added successfully!\n")


# =========================================
# VIEW STUDENTS
# =========================================
def view_students(students):
    print("\n========== STUDENT LIST ==========")

    if len(students) == 0:
        print("No students found.\n")
        return

    for index, student in enumerate(students, start=1):
        print(f"\nStudent #{index}")
        print(f"Name    : {student.name}")
        print(f"Age     : {student.age}")
        print(f"Program : {student.program}")
        print(f"Contact : {student.contact}")

    print()


# =========================================
# SEARCH STUDENT
# =========================================
def search_student(students):
    print("\n========== SEARCH STUDENT ==========")

    search_name = input("Enter student name to search: ").strip().title()

    found = False

    for student in students:
        if student.name == search_name:
            print("\nStudent Found!")
            print(f"Name    : {student.name}")
            print(f"Age     : {student.age}")
            print(f"Program : {student.program}")
            print(f"Contact : {student.contact}")
            found = True
            break

    if not found:
        print("\nStudent not found.")

    print()


# =========================================
# DELETE STUDENT
# =========================================
def delete_student(students):
    print("\n========== DELETE STUDENT ==========")

    delete_name = input("Enter student name to delete: ").strip().title()

    for student in students:
        if student.name == delete_name:
            students.remove(student)
            print("\nStudent deleted successfully!\n")
            return

    print("\nStudent not found.\n")


# =========================================
# DISPLAY MENU
# =========================================
def display_menu():
    print("========== STUDENT MANAGEMENT SYSTEM ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Save Students to File")
    print("6. Login System")
    print("0. Exit")


# =========================================
# MAIN PROGRAM
# =========================================
def main():
    create_default_user()

    students = load_students()

    logged_in = False

    while True:
        display_menu()

        choice = input("Enter your choice: ").strip()

        # LOGIN
        if choice == "6":
            logged_in = login_system()

        # REQUIRE LOGIN FOR OTHER FEATURES
        elif choice in ["1", "2", "3", "4", "5"]:

            if not logged_in:
                print("\nPlease login first!\n")
                continue

            if choice == "1":
                add_student(students)

            elif choice == "2":
                view_students(students)

            elif choice == "3":
                search_student(students)

            elif choice == "4":
                delete_student(students)

            elif choice == "5":
                save_students(students)

        # EXIT
        elif choice == "0":
            print("\nExiting program...")

            # Auto-save before exit
            save_students(students)

            print("Goodbye!")
            break

        else:
            print("\nInvalid choice! Please try again.\n")


# =========================================
# RUN PROGRAM
# =========================================
if __name__ == "__main__":
    main()