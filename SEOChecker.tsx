"use client";
import { useState } from "react";

export default function SEOChecker({ content }: { content: string }) {
  const [keyword, setKeyword] = useState("");
  const density = keyword ? ((content.match(new RegExp(`\\b${keyword}\\b`, "gi")) || []).length / Math.max(1, content.split(/\s+/).length) * 100).toFixed(2) : "0.00";

  return (
    <div className="bg-white p-4 rounded-md shadow-soft mt-4">
      <h4 className="font-semibold mb-2">SEO Tools</h4>
      <div className="flex gap-2">
        <input value={keyword} onChange={(e) => setKeyword(e.target.value)} placeholder="Focus keyword" className="border p-2 rounded flex-1" />
        <div className="px-3 py-2 text-sm bg-gray-100 rounded">{density}% density</div>
      </div>
    </div>
  );
}

