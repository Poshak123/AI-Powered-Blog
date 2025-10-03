import { useState, useEffect } from "react";
import MarkdownEditor from "./MarkdownEditor";
import { saveBlog } from "../utils/api";

interface Props {
  suggestion: string;
}

export default function CreateBlog({ suggestion }: Props) {
  const [title, setTitle] = useState("");
  const [content, setContent] = useState(suggestion);

  useEffect(() => {
    setContent(suggestion);
  }, [suggestion]);

  const handleSave = async () => {
    const res = await saveBlog(title, content);
    if (res) alert("Blog saved successfully!");
    else alert("Failed to save blog");
  };

  return (
    <div style={{ marginTop: "2rem" }}>
      <h2>Create Blog</h2>
      <input
        type="text"
        placeholder="Blog title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        style={{ padding: "0.5rem", width: "300px" }}
      />
      <MarkdownEditor content={content} setContent={setContent} />
      <button onClick={handleSave} style={{ marginTop: "1rem" }}>
        Save Blog
      </button>
    </div>
  );
}
