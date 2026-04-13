import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import {
  fetchStudentsAPI,
  addStudentAPI,
  deleteStudentAPI,
  updateMarksAPI,
} from "../api/StudentApi";

// Fetch
export const fetchStudents = createAsyncThunk(
  "students/fetch",
  async () => {
    const res = await fetchStudentsAPI();
    return res.data;
  }
);

// Add
export const addStudent = createAsyncThunk(
  "students/add",
  async (student) => {
    const res = await addStudentAPI(student);
    return res.data;
  }
);

// Delete
export const deleteStudent = createAsyncThunk(
  "students/delete",
  async (name) => {
    await deleteStudentAPI(name);
    return name;
  }
);

// Update
export const updateMarks = createAsyncThunk(
  "students/update",
  async ({ name, marks }) => {
    const res = await updateMarksAPI(name, marks);
    return res.data;
  }
);

const studentSlice = createSlice({
  name: "students",
  initialState: {
    list: [],
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchStudents.fulfilled, (state, action) => {
        state.list = action.payload;
      })
      .addCase(addStudent.fulfilled, (state, action) => {
        state.list.push(action.payload);
      })
      .addCase(deleteStudent.fulfilled, (state, action) => {
        state.list = state.list.filter(
          (s) => s.name !== action.payload
        );
      })
      .addCase(updateMarks.fulfilled, (state, action) => {
        const index = state.list.findIndex(
          (s) => s.name === action.payload.name
        );
        if (index !== -1) {
          state.list[index] = action.payload;
        }
      });
  },
});

export default studentSlice.reducer;