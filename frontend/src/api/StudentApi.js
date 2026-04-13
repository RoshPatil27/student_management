import axios from "axios";

const API = "http://127.0.0.1:5000";

export const fetchStudentsAPI = () => axios.get(`${API}/students`);

export const addStudentAPI = (student) =>
  axios.post(`${API}/students`, student);

export const deleteStudentAPI = (name) =>
  axios.delete(`${API}/students/${name}`);

export const updateMarksAPI = (name, marks) =>
  axios.put(`${API}/students/${name}`, { marks });

export const searchStudentAPI = (name) =>
  axios.get(`${API}/students/${name}`);