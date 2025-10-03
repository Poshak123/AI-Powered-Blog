import { useState } from "react";
import Navbar from "../components/Navbar";
import BlogCard from "../components/BlogCard";

export default function Blogs() {
  const [blogs, setBlogs] = useState<
    Array<{ title: string; content: string }>
  >([]);
  const [prompt, setPrompt] = useState("");
  const [loading, setLoading] = useState(false);

  // Function to call FastAPI backend
  const generateBlog = async () => {
    if (!prompt) return;
    setLoading(true);

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/api/ai/generate",
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ prompt }),
        }
      );

      if (!response.ok) throw new Error("Failed to generate blog");

      const data = await response.json();
      setBlogs((prev) => [
        ...prev,
        { title: prompt, content: data.text || "No content generated" },
      ]);
      setPrompt(""); // Clear input after generation
    } catch (err) {
      console.error(err);
      alert("Error generating blog. Check console for details.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: "2rem" }}>
      <Navbar />
      <h1>All Blogs</h1>

      <div style={{ marginBottom: "1rem" }}>
        <input
          type="text"
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          placeholder="Enter blog topic"
          style={{ padding: "0.5rem", width: "300px" }}
        />
        <button
          onClick={generateBlog}
          disabled={loading}
          style={{ marginLeft: "1rem", padding: "0.5rem 1rem" }}
        >
          {loading ? "Generating..." : "Generate Blog"}
        </button>
      </div>

      {blogs.map((b, i) => (
        <BlogCard key={i} title={b.title} content={b.content} />
      ))}
    </div>
  );
}
