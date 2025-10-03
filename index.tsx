"use client"; // keep this if you’re in app/ directory with Next.js 13+

import { useState } from "react";

export default function Home() {
  const [prompt, setPrompt] = useState<string>("");
  const [generatedContent, setGeneratedContent] = useState<string>("");

  const handleGenerate = async () => {
    setGeneratedContent("Generating...");

    try {
      const response = await fetch("http://127.0.0.1:8000/generate", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ prompt }),
      });

      if (!response.ok) {
        throw new Error(`Error: ${response.status}`);
      }

      const data: { content: string } = await response.json();

      // ✅ update with backend response
      setGeneratedContent(data.content);
    } catch (error: any) {
      setGeneratedContent(`Error generating content: ${error.message}`);
    }
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h1>AI-Powered Blog</h1>

      <textarea
        rows={4}
        cols={50}
        placeholder="Enter your prompt..."
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
      />

      <br />

      <button onClick={handleGenerate}>Generate</button>

      <h2>Generated Content:</h2>
      <p>{generatedContent}</p>
    </div>
  );
}
