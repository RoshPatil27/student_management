import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import {
  fetchStudents,
  addStudent,
  deleteStudent,
} from "../app/StudentSlice";

export default function StudentList() {
  const dispatch = useDispatch();
  const students = useSelector((state) => state.students.list);

  const [name, setName] = useState("");
  const [marks, setMarks] = useState("");

  useEffect(() => {
    dispatch(fetchStudents());
  }, [dispatch]);

  const handleAdd = () => {
    if (!name || !marks) return;

    const marksArray = marks.split(",").map(Number);
    dispatch(addStudent({ name, marks: marksArray }));

    setName("");
    setMarks("");
  };

  return (
    <div
      style={{
        width: "500px",
        margin: "auto",
        padding: "20px",
        fontFamily: "Arial",
      }}
    >
      <h2 style={{ textAlign: "center" }}>📚 Student Management</h2>

      {/* Form */}
      <div
        style={{
          display: "flex",
          gap: "10px",
          marginBottom: "20px",
        }}
      >
        <input
          placeholder="Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          style={{
            padding: "8px",
            flex: 1,
          }}
        />
        <input
          placeholder="Marks (comma separated)"
          value={marks}
          onChange={(e) => setMarks(e.target.value)}
          style={{
            padding: "8px",
            flex: 1,
          }}
        />
        <button
          onClick={handleAdd}
          style={{
            padding: "8px 12px",
            background: "#4caf50",
            color: "white",
            border: "none",
            cursor: "pointer",
          }}
        >
          Add
        </button>
      </div>

      {/* Student List */}
      <ul style={{ listStyle: "none", padding: 0 }}>
        {students.map((s, i) => (
          <li
            key={i}
            style={{
              display: "flex",
              justifyContent: "space-between",
              background: "#f3f3f3",
              padding: "10px",
              marginBottom: "10px",
              borderRadius: "8px",
            }}
          >
            <div>
              <strong>{s.name}</strong>
              <p>Marks: {s.marks.join(", ")}</p>
              <p>Avg: {s.average?.toFixed?.(2) || "N/A"}</p>
              <p>Grade: {s.grade || "N/A"}</p>
            </div>

            <button
              onClick={() => dispatch(deleteStudent(s.name))}
              style={{
                background: "red",
                color: "white",
                border: "none",
                padding: "6px 10px",
                cursor: "pointer",
              }}
            >
              Delete
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}