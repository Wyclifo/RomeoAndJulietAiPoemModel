"use server";

export async function generatePoem(formData: FormData) {
  const res = await fetch(`http://localhost:8000/api/v1/generate`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      text: formData.get("text"),
      temperature: Number(formData.get("temperature")),
      words: Number(formData.get("words")),
    }),
    cache: "no-store",
  });

  if (!res.ok) throw new Error("Failed");

  return await res.json();
}