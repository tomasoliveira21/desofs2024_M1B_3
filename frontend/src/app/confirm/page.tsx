"use client"

import { supabase } from "@/lib/supabase"
import { useRouter } from "next/navigation"
import { useEffect, useState } from "react"

export default function Confirm() {
  const [message, setMessage] = useState<string | null>(null);
  const router = useRouter();

  useEffect(() => {
    const confirmUser = async () => {
      const params = new URLSearchParams(window.location.search);
      const tokenHash = params.get('token_hash');
      const type = params.get('type');
      const email = params.get('email');

      if (tokenHash && type === 'signup' && email) {
        try {
          const { error } = await supabase.auth.verifyOtp({
            email: email,
            token: tokenHash,
            type: 'signup'
          });

          if (error) {
            setMessage("Verification failed: " + error.message);
          } else {
            setMessage("Verification successful! Redirecting to login...");
            setTimeout(() => router.push('/login'), 3000);
          }
        } catch (error) {
          setMessage("An error occurred: " + error);
        }
      } else {
        setMessage("Invalid verification link.");
      }
    };

    confirmUser();
  }, [router]);

  return (
    <div className="min-h-screen flex items-center justify-center bg-black">
      <div className="bg-gray-800 p-8 rounded-lg shadow-md w-[400px]">
        <h2 className="text-2xl font-bold mb-6 text-center text-white">
          Email Verification
        </h2>
        {message && <div className="mb-4 text-center text-white">{message}</div>}
      </div>
    </div>
  )
}
