from student import Student
import json

class StudentManager:
    def __init__(self, file_path="data.json"):
        self.file_path = file_path
        self.students = self.load_data()

    def load_data(self):
        try:
            with open(self.file_path, "r") as f:
                data = json.load(f)
                return [Student.from_dict(s) for s in data]
        except FileNotFoundError:
            return []

    def save_data(self):
        with open(self.file_path, "w") as f:
            json.dump([s.to_dict() for s in self.students], f, indent=4)

    def add_student(self, name, marks):
        student = Student(name, marks)
        self.students.append(student)
        self.save_data()

    def display_students(self):
        if not self.students:
            print("No students found")
            return
        
        for s in self.students:
            print(f"Name: {s.name}")
            print(f"Marks: {s.marks}")
            print(f"Average: {s.average():.2f}")
            print(f"Grade: {s.grade()}")
            print("-" * 20)

    def find_student(self, name):
        for s in self.students:
            if s.name.lower() == name.lower():
                return s
        return None
    
    def delete_student(self, name):
        student = self.find_student(name)
        if student:
            self.students.remove(student)
            self.save_data()
            return True
        return False
    
    def update_marks(self, name, new_marks):
        student = self.find_student(name)
        if student:
            student.marks = new_marks
            self.save_data()
            return True
        return False
    
    