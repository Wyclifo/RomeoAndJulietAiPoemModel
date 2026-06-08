import Link from "next/link";

export default function Home() {
  return (
    <main className="min-h-screen bg-gradient-to-br from-black via-gray-950 to-gray-900 text-white">

      {/* HERO SECTION */}
      <section className="flex flex-col items-center justify-center text-center px-6 pt-20 pb-10">

        <h1 className="text-5xl md:text-6xl font-bold tracking-tight">
          AI Poem Generator
        </h1>
  

        <p className="mt-5 text-gray-300 text-lg max-w-2xl leading-relaxed">
          Transform simple ideas into expressive, emotional poetry using advanced AI.
          Write less. Feel more.
        </p>

        {/* FEATURE BADGES */}
        <div className="flex flex-wrap gap-3 justify-center mt-6 text-sm text-gray-400">
          <span className="bg-gray-800 px-3 py-1 rounded-full">✍️ Creative Writing AI</span>
          <span className="bg-gray-800 px-3 py-1 rounded-full">⚡ Instant Generation</span>
          <span className="bg-gray-800 px-3 py-1 rounded-full">🎭 Emotional Tone Control</span>
        </div>
      </section>

      {/* MAIN CONTENT */}
      <section className="flex justify-center px-6 pb-20">

        <div className="w-full max-w-3xl bg-gray-900 border border-gray-800 rounded-2xl shadow-2xl p-8">

          {/* FORM TITLE */}
          <Link href="/poem" className="text-center mb-6">
            <h2 className="text-2xl font-semibold">
              Create Your Poem
            </h2>
            <p className="text-gray-400 text-sm mt-1">
              Enter a theme and let AI compose your poetry
            </p>
          </Link>

        </div>
      </section>

      {/* FEATURES SECTION */}
      <section className="px-6 pb-24">
        <div className="max-w-5xl mx-auto grid md:grid-cols-3 gap-6 text-center">

          <div className="bg-gray-900 border border-gray-800 p-6 rounded-xl">
            <h3 className="font-semibold text-lg">Deep Creativity</h3>
            <p className="text-gray-400 text-sm mt-2">
              Generate poems with emotional depth and variation.
            </p>
          </div>

          <div className="bg-gray-900 border border-gray-800 p-6 rounded-xl">
            <h3 className="font-semibold text-lg">Fast Generation</h3>
            <p className="text-gray-400 text-sm mt-2">
              Get results instantly from AI-powered backend.
            </p>
          </div>

          <div className="bg-gray-900 border border-gray-800 p-6 rounded-xl">
            <h3 className="font-semibold text-lg">Custom Control</h3>
            <p className="text-gray-400 text-sm mt-2">
              Adjust creativity and length to match your style.
            </p>
          </div>
        

        </div>
      </section>

    </main>
  );
}