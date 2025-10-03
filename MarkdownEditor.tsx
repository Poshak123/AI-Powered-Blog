import { useState } from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

interface Props {
  content: string;
  setContent: (value: string) => void;
}

export default function MarkdownEditor({ content, setContent }: Props) {
  return (
    <div style={{ display: "flex", gap: "2rem" }}>
      <textarea
        value={content}
        onChange={(e) => setContent(e.target.value)}
        style={{ width: "50%", height: "300px", padding: "0.5rem" }}
      />
      <div style={{ width: "50%", border: "1px solid #ccc", padding: "0.5rem", height: "300px", overflowY: "scroll" }}>
        <ReactMarkdown remarkPlugins={[remarkGfm]}>{content}</ReactMarkdown>
      </div>
    </div>
  );
}
