import { useState } from "react";
import axios from "axios";
import ReactMarkdown from "react-markdown";

function App() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const askRag = async () => {
    if (!question.trim()) return;
    setLoading(true);
    setAnswer("");
    try {
      const res = await axios.post("/query", { question });
      setAnswer(res.data.answer);
    } catch (err) {
      setAnswer("Error: " + err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center p-6 bg-gradient-to-br from-gray-900 via-gray-950 to-indigo-950 text-gray-100">
      {/* Header */}
      <h1 className="text-4xl font-bold mb-8 text-indigo-400 tracking-tight text-center">
        RAG Tutor
      </h1>

      {/* Main Card */}
      <div className="w-8/10  bg-gray-900/60 backdrop-blur-lg border border-indigo-800 shadow-lg rounded-3xl p-8 space-y-6 transition-all duration-300">
        <textarea
          rows={2}
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Ask me anything like What is Context-Based Recommendation?"
          className="w-full border border-gray-700 rounded-2xl p-4 bg-gray-800/70 text-gray-200 focus:outline-none focus:ring-4 focus:ring-indigo-800 placeholder:text-gray-500 resize-none transition-all duration-200"
        />

        <div className="flex justify-end">
          <button
            onClick={askRag}
            disabled={loading}
            className={`px-6 py-2.5 rounded-xl font-semibold transition-all duration-200 ${
              loading
                ? "bg-gray-600 text-gray-300 cursor-not-allowed"
                : "bg-indigo-600 hover:bg-indigo-500 text-white shadow-sm"
            }`}
          >
            {loading ? "Thinking..." : "Ask"}
          </button>
        </div>

        {/* Answer */}
        {answer && (
          <div className="border-t border-indigo-800 pt-6 text-gray-100">
            <h2 className="font-semibold mb-3 text-indigo-400 text-lg">
              Answer:
            </h2>
            <div className="prose prose-invert prose-indigo max-w-none leading-relaxed">
              <ReactMarkdown>{answer}</ReactMarkdown>
            </div>
          </div>
        )}
      </div>

      {/* Footer */}
      <p className="text-sm text-gray-500 mt-8 tracking-wide text-center">
        Powered by Gemini · LangChain · FastAPI
      </p>
    </div>
  );
}

export default App;
