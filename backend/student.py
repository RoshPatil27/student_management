class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  # list of marks

    def average(self):
        return sum(self.marks) / len(self.marks) if self.marks else 0

    def grade(self):
        avg = self.average()
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 50:
            return "C"
        else:
            return "Fail"

    def to_dict(self):
        return {
            "name": self.name,
            "marks": self.marks
        }

    @staticmethod
    def from_dict(data):
        return Student(data["name"], data["marks"])