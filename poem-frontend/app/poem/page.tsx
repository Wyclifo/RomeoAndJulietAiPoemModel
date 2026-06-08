"use client";

import { useState, useTransition } from "react";
import { generatePoem } from "@/app/actions/actions";
import Link from "next/dist/client/link";

type PoemItem = {
  text: string;
  temperature: number;
  words: number;
  result: string;
  time: number;
};

export default function Page() {
  const [poems, setPoems] = useState<PoemItem[]>([]);
  const [isPending, startTransition] = useTransition();

  async function handleSubmit(formData: FormData) {
    startTransition(async () => {
      try {
        const res = await generatePoem(formData);

        // IMPORTANT: your server action must RETURN data now (NOT redirect)
        const newPoem: PoemItem = {
          text: formData.get("text")?.toString() || "",
          temperature: Number(formData.get("temperature") || 0.8),
          words: Number(formData.get("words") || 40),
          result: res.generated_poem,
          time: Date.now(),
        };

        setPoems((prev) => [newPoem, ...prev]);
      } catch (err) {
        console.error("Poem generation failed", err);
      }
    });
  }

  return (
    <main className="min-h-screen bg-gradient-to-br from-gray-950 via-gray-900 to-black text-white flex justify-center p-6">

      <div className="w-full max-w-4xl grid grid-cols-1 md:grid-cols-2 gap-6">

        {/* LEFT: FORM */}
        <div className="bg-gray-900 border border-gray-800 rounded-2xl shadow-xl p-6">

          <div className="text-center mb-6">
            <h1 className="text-3xl font-bold">AI Poem Generator</h1>
            <p className="text-gray-400 text-sm">
              Generate and store poetic expressions
            </p>
          </div>
          {/* back link */}
          <Link href="/" className="text-blue-400 hover:text-blue-300 text-sm mt-4 inline-block">
            ← Back to Home
          </Link>

          <form action={handleSubmit} className="space-y-5">

            {/* Theme */}
            <div className="space-y-1">
              <label className="text-sm text-gray-300">Theme</label>
              <input
                name="text"
                required
                placeholder="love, war, dreams, ocean..."
                className="w-full p-3 rounded bg-gray-800 border border-gray-700
                           focus:border-blue-500 focus:ring-2 focus:ring-blue-500 outline-none"
              />
            </div>

            {/* Controls */}
            <div className="grid grid-cols-2 gap-3">

              <div className="space-y-1">
                <label className="text-sm text-gray-300">Creativity</label>
                <input
                  name="temperature"
                  type="number"
                  step="0.1"
                  defaultValue={0.8}
                  className="w-full p-3 rounded bg-gray-800 border border-gray-700
                             focus:border-blue-500 focus:ring-2 focus:ring-blue-500 outline-none"
                />
              </div>

              <div className="space-y-1">
                <label className="text-sm text-gray-300">Words</label>
                <input
                  name="words"
                  type="number"
                  defaultValue={40}
                  className="w-full p-3 rounded bg-gray-800 border border-gray-700
                             focus:border-blue-500 focus:ring-2 focus:ring-blue-500 outline-none"
                />
              </div>

            </div>

            {/* BUTTON */}
            <button
              type="submit"
              disabled={isPending}
              className="w-full bg-blue-600 hover:bg-blue-700 transition
                         p-3 rounded font-semibold shadow-md disabled:opacity-50"
            >
              {isPending ? "Generating..." : "Generate Poem"}
            </button>

          </form>
        </div>

        {/* RIGHT: POEM HISTORY */}
        <div className="bg-gray-900 border border-gray-800 rounded-2xl shadow-xl p-6">

          <h2 className="text-xl font-bold mb-4">Generated Poems</h2>

          {poems.length === 0 ? (
            <p className="text-gray-500 text-sm">
              No poems yet. Generate one to see it here.
            </p>
          ) : (
            <div className="space-y-4 max-h-[75vh] overflow-y-auto pr-2">

              {poems.map((p, idx) => (
                <div
                  key={idx}
                  className="bg-gray-800 border border-gray-700 rounded-xl p-4"
                >

                  {/* metadata */}
                  <div className="text-xs text-gray-400 mb-2 flex justify-between">
                    <span>Theme: {p.text}</span>
                    <span>{new Date(p.time).toLocaleTimeString()}</span>
                  </div>

                  <div className="text-xs text-gray-500 mb-3">
                    Temp: {p.temperature} | Words: {p.words}
                  </div>

                  {/* poem */}
                  <pre className="whitespace-pre-wrap font-serif text-gray-100 leading-relaxed">
                    {p.result}
                  </pre>

                </div>
              ))}

            </div>
          )}
        </div>

      </div>
    </main>
  );
}