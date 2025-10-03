import axios from "axios";

const API_URL = "http://127.0.0.1:8000"; // FastAPI backend

export const fetchSuggestion = async (prompt: string) => {
  try {
    const res = await axios.get(`${API_URL}/suggest`, { params: { prompt } });
    return res.data.suggestion;
  } catch (err) {
    console.error(err);
    return "Error fetching suggestion";
  }
};

// Later: Add blog saving API
export const saveBlog = async (title: string, content: string) => {
  try {
    const res = await axios.post(`${API_URL}/blogs`, { title, content });
    return res.data;
  } catch (err) {
    console.error(err);
    return null;
  }
};
