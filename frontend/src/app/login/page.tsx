"use client"

import { supabase } from "@/lib/supabase"
import { useRouter } from "next/navigation"
import { useState } from "react"

export default function Login() {
  const [data, setData] = useState<{
    email: string,
    password: string
  }>({
    email: '',
    password: ''
  })

  const [resetPassword, setResetPassword] = useState<boolean>(false);
  const [message, setMessage] = useState<string | null>(null);

  const router = useRouter();

  const login = async () => {
    try {
      let { data: dataUser, error } = await supabase.auth.signInWithPassword({
        email: data.email,
        password: data.password
      })

      if (dataUser) {
        router.refresh();
      } else if (error) {
        setMessage("Login failed: " + error.message);
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

  const sendResetPassword = async () => {
    try {
      const { data: resetData, error } = await supabase.auth.resetPasswordForEmail(data.email, {
        redirectTo: `${window.location.href}reset`
      });
      console.log(data.email);
    } catch (error) {
      setMessage("An error occurred: " + error);
    }
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-black">
      <div className="bg-gray-800 p-8 rounded-lg shadow-md w-[400px]">
        <h2 className="text-2xl font-bold mb-6 text-center text-white">
          {resetPassword ? "Reset Password" : "SocialNet Login"}
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
        {!resetPassword && (
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
        )}
        {message && <div className="mb-4 text-center text-white">{message}</div>}
        <div>
          {resetPassword ? (
            <button
              onClick={sendResetPassword}
              className="w-full bg-blue-500 text-white py-2 rounded hover:bg-blue-600 transition duration-200"
            >
              Reset Password
            </button>
          ) : (
            <button
              onClick={login}
              className="w-full bg-blue-500 text-white py-2 rounded hover:bg-blue-600 transition duration-200"
            >
              Login
            </button>
          )}
        </div>
        <div className="mt-4 text-center">
          <button
            onClick={() => setResetPassword(!resetPassword)}
            className="text-blue-400 hover:underline"
          >
            {resetPassword ? "Back to Login" : "Forgot Password?"}
          </button>
        </div>
      </div>
    </div>
  )
}
