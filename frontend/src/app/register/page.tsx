"use client"

import { supabase } from "@/lib/supabase"
import { useRouter } from "next/navigation"
import { useState } from "react"

export default function Register() {
  const [data, setData] = useState<{
    email: string,
    password: string
  }>({
    email: '',
    password: ''
  })

  const [message, setMessage] = useState<string | null>(null);

  const router = useRouter();

  const register = async () => {
    try {
      const { data: user, error } = await supabase.auth.signUp({
        email: data.email,
        password: data.password,
      })

      if (user) {
        router.push('/');
      } else if (error) {
        setMessage("Registration failed: " + error.message);
      }

    } catch (error) {
      setMessage("An error occurred: " + error);
    }
  }

  const handleChange = (e: any) => {
    const { name, value } = e.target;
    setData((prev: any) => ({
      ...prev,
      [name]: value,
    }))
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-black">
      <div className="bg-gray-800 p-8 rounded-lg shadow-md w-[400px]">
        <h2 className="text-2xl font-bold mb-6 text-center text-white">
          Register
        </h2>
        <div className="grid mb-4">
          <label className="mb-2 text-gray-300">Email</label>
          <input
            type="text"
            name="email"
            value={data?.email}
            onChange={handleChange}
            className="p-2 border border-gray-600 rounded bg-gray-700 text-white"
          />
        </div>
        <div className="grid mb-6">
          <label className="mb-2 text-gray-300">Password</label>
          <input
            type="password"
            name="password"
            value={data?.password}
            onChange={handleChange}
            className="p-2 border border-gray-600 rounded bg-gray-700 text-white"
          />
        </div>
        {message && <div className="mb-4 text-center text-white">{message}</div>}
        <div>
          <button
            onClick={register}
            className="w-full bg-blue-500 text-white py-2 rounded hover:bg-blue-600 transition duration-200"
          >
            Register
          </button>
        </div>
        <div className="mt-4 text-center">
          <button
            onClick={() => router.push('/')}
            className="text-blue-400 hover:underline"
          >
            Back to Login
          </button>
        </div>
      </div>
    </div>
  )
}
