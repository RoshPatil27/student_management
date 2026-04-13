from flask import Flask, request, jsonify
from flask_cors import CORS
from manager import StudentManager

app = Flask(__name__)
CORS(app)

manager = StudentManager()

# ✅ 1. Add Student
@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()

    name = data.get("name")
    marks = data.get("marks")

    if not name or not marks:
        return jsonify({"error": "Invalid input"}), 400

    manager.add_student(name, marks)

    # ✅ get newly added student
    student = manager.find_student(name)

    return jsonify({
        "name": student.name,
        "marks": student.marks,
        "average": round(student.average(), 2),
        "grade": student.grade()
    })

# ✅ 2. View All Students
@app.route("/students", methods=["GET"])
def get_students():
    students = manager.students

    result = []
    for s in students:
        result.append({
            "name": s.name,
            "marks": s.marks,
            "average": round(s.average(), 2),
            "grade": s.grade()
        })

    return jsonify(result)


# ✅ 3. Search Student
@app.route("/students/<name>", methods=["GET"])
def get_student(name):
    student = manager.find_student(name)

    if not student:
        return jsonify({"error": "Student not found"}), 404

    return jsonify({
        "name": student.name,
        "marks": student.marks,
        "average": round(student.average(), 2),
        "grade": student.grade()
    })


# ✅ 4. Delete Student
@app.route("/students/<name>", methods=["DELETE"])
def delete_student(name):
    if manager.delete_student(name):
        manager.save_data()
        return jsonify({"message": "Student deleted successfully"})

    return jsonify({"error": "Student not found"}), 404


# ✅ 5. Update Marks
@app.route("/students/<name>", methods=["PUT"])
def update_marks(name):
    data = request.get_json()
    marks = data.get("marks")

    if not marks:
        return jsonify({"error": "Invalid input"}), 400

    if manager.update_marks(name, marks):
        student = manager.find_student(name)

        return jsonify({
            "name": student.name,
            "marks": student.marks,
            "average": round(student.average(), 2),
            "grade": student.grade()
        })

    return jsonify({"error": "Student not found"}), 404

# ✅ Root test
@app.route("/")
def home():
    return "Student API Running 🚀"


if __name__ == "__main__":
    app.run(debug=True)