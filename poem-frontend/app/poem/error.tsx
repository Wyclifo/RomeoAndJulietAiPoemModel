"use client";
import { useEffect } from "react";
import { useRouter } from "next/navigation";
export default function Error({ error }: { error: Error }) {
  const router = useRouter();   
    useEffect(() => {
        console.error(error);
        router.push("/poem");
    }
    , [error, router]);
    return (<div className="flex flex-col items-center justify-center h-screen">
        <h1 className="text-2xl font-bold mb-4">An error occurred</h1>
        <p className="text-gray-600 mb-4">{error.message}</p>
        <button className="px-4 py-2 bg-blue-500 text-white rounded" onClick={() => router.push("/poem")}>
            Go back to Poem
        </button>
    </div>);
}
