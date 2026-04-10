from manager import StudentManager
from utils import get_marks_input

def main():
    manager = StudentManager()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Update Marks")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            marks = get_marks_input()
            manager.add_student(name, marks)
            print("Student added successfully!")

        elif choice == "2":
            manager.display_students()

        elif choice == "3":
            name = input("Enter name to search: ")
            student = manager.find_student(name)
            if student:
                print(f"Name: {student.name}")
                print(f"Marks: {student.marks}")
                print(f"Average: {student.average():.2f}")
                print(f"Grade: {student.grade()}")
            else:
                print("Student not found")

        elif choice == "4":
            name = input("Enter name to delete: ")
            if manager.delete_student(name):
                print("Student deleted successfully!")
            else:
                print("Student not found")

        elif choice == "5":
            name = input("Enter student name: ")
            marks = get_marks_input()
            if manager.update_marks(name, marks):
                print("Marks updated")
            else:
                print("Student not found")

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

    manager.save_data()

if __name__ == "__main__":
    main()