"use client";

import { useState, useRef, useEffect } from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

type Message = {
  role: "user" | "assistant";
  content?: string;
  answer?: string;
  sources?: string[];
  loading?: boolean;
};

const suggestions = [
  "Schemes for women",
  "Farmer subsidy schemes",
  "Education scholarships",
  "Startup schemes in India",
];

export default function Home() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const chatRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    chatRef.current?.scrollTo({
      top: chatRef.current.scrollHeight,
      behavior: "smooth",
    });
  }, [messages]);

  const sendMessage = async (customInput?: string) => {
    const query = customInput || input;

    if (!query.trim() || loading) return;

    setLoading(true);
    setInput("");

    setMessages((prev) => [
      ...prev,
      { role: "user", content: query },
      { role: "assistant", answer: "", loading: true }
    ]);

    try {
      const res = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ query }),
      });

      if (!res.body) throw new Error("No response body");

      const reader = res.body.getReader();
      const decoder = new TextDecoder();

      let buffer = "";

      while (true) {
        const { value, done } = await reader.read();
        if (done) break;

        buffer += decoder.decode(value, { stream: true });

        const lines = buffer.split("\n");
        buffer = lines.pop() || "";

        for (const line of lines) {
          if (!line.trim()) continue;

          try {
            const data = JSON.parse(line);

            if (data.type === "token") {
              await new Promise((r) => setTimeout(r, 0));

              setMessages((prev) => {
                const updated = [...prev];
                const last = updated[updated.length - 1];

                updated[updated.length - 1] = {
                  ...last,
                  answer: (last.answer || "") + data.content
                };

                return updated;
              });
            }

            if (data.type === "end") {
              setMessages((prev) => {
                const updated = [...prev];
                const last = updated[updated.length - 1];

                updated[updated.length - 1] = {
                  ...last,
                  loading: false,
                  sources: data.sources || []
                };

                return updated;
              });

              setLoading(false);
            }

          } catch (err) {
            console.error("JSON parse error:", err);
          }
        }
      }

    } catch (err) {
      console.error(err);
      setLoading(false);
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter") {
      e.preventDefault();
      sendMessage();
    }
  };

  return (
    <div className="flex flex-col h-screen bg-[#f7f7f8]">

      {/* HEADER */}
      <div className="border-b bg-white px-6 py-3 flex justify-between items-center">
        <h1 className="font-semibold">TN Government Schemes Assistant</h1>
        <span className="text-sm text-gray-500">Powered by RAG + LLM</span>
      </div>

      {/* CHAT AREA */}
      <div
        ref={chatRef}
        className="flex-1 overflow-y-auto px-4 py-6"
      >
        <div className="max-w-3xl mx-auto space-y-6">

          {/* EMPTY STATE */}
          {messages.length === 0 && (
            <div className="text-center mt-20 space-y-6">

              <h2 className="text-2xl font-semibold">
                Govt Scheme Assistant
              </h2>

              <p className="text-gray-500 text-sm">
                Ask about Indian government schemes, eligibility, benefits, and more.
              </p>

              {/* CLICKABLE SUGGESTIONS */}
              <div className="grid grid-cols-1 md:grid-cols-2 gap-3 mt-6">
                {suggestions.map((s, i) => (
                  <button
                    key={i}
                    onClick={() => sendMessage(s)}
                    className="border rounded-xl p-3 bg-white hover:bg-gray-50 text-sm text-left"
                  >
                    {s}
                  </button>
                ))}
              </div>
            </div>
          )}

          {/* MESSAGES */}
          {messages.map((msg, idx) => (
            <div key={idx}>

              {/* USER */}
              {msg.role === "user" && (
                <div className="flex justify-end">
                  <div className="bg-blue-600 text-white px-4 py-3 rounded-2xl max-w-lg whitespace-pre-wrap">
                    {msg.content}
                  </div>
                </div>
              )}

              {/* ASSISTANT */}
              {msg.role === "assistant" && (
                <div className="flex gap-3">

                  <div className="w-8 h-8 rounded-full bg-gray-300 flex items-center justify-center text-sm font-semibold">
                    AI
                  </div>

                  <div className="flex-1 space-y-2 m-b-4">

                    <div className="bg-white border rounded-2xl p-4 shadow-sm">

                      {msg.loading ? (
                        <div className="whitespace-pre-wrap">
                          {msg.answer}
                          <span className="animate-pulse">▌</span>
                        </div>
                      ) : (
                        <ReactMarkdown remarkPlugins={[remarkGfm]}>
                          {msg.answer || ""}
                        </ReactMarkdown>
                      )}

                    </div>

                    {/* SOURCES */}
                    {!msg.loading && msg.sources && msg.sources.length > 0 && (
                      <div className="text-xs text-gray-500">
                        <span className="font-medium">Sources:</span>
                        <ul className="mt-1 space-y-1">
                          {msg.sources.map((s, i) => (
                            <li key={i}>
                              <a
                                href={s}
                                target="_blank"
                                className="underline text-blue-600"
                              >
                                {s}
                              </a>
                            </li>
                          ))}
                        </ul>
                      </div>
                    )}

                  </div>
                </div>
              )}

            </div>
          ))}

        </div>
      </div>

      {/* INPUT BAR (FIXED) */}
      <div className="border-t bg-white px-4 py-3 sticky bottom-0">
        <div className="max-w-3xl mx-auto flex gap-2">

          <input
            className="flex-1 p-3 border rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-50"
            placeholder="Ask about government schemes..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyDown}
            disabled={loading}
          />

          <button
            onClick={() => sendMessage()}
            disabled={loading}
            className={`px-4 py-2 rounded-xl text-white ${
              loading ? "bg-gray-400" : "bg-blue-600 hover:bg-blue-700"
            }`}
          >
            Send
          </button>

        </div>

        {/* DISCLAIMER */}
        <div className="text-xs text-gray-400 text-center mt-2">
          This AI may produce inaccurate information. Always verify with official government sources.
        </div>
      </div>

    </div>
  );
}