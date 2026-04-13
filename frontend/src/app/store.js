import { configureStore } from "@reduxjs/toolkit";
import studentReducer from "../app/StudentSlice";

export const store = configureStore({
  reducer: {
    students: studentReducer,
  },
});