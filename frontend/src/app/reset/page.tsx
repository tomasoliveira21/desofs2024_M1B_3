"use client";

import { supabase } from "@/lib/supabase";
import { useRouter } from "next/navigation";
import { useState } from "react";

export default function Reset() {
  const [data, setData] = useState<{
    password: string;
    confirmPassword: string;
  }>({
    password: "",
    confirmPassword: "",
  });

  const router = useRouter();

  const [showPassword, setShowPassword] = useState<boolean>(false);

  const confirmPassword = async () => {
    const { password, confirmPassword } = data;
    if (password !== confirmPassword) return alert("Your password are incorrect");

    const { data: resetData, error } = await supabase.auth.updateUser({
      password: data.password
    });

    if (resetData) {
      router.push('/');
    }
    if (error) console.log(error);
  };

  const handleChange = (e: any) => {
    const { name, value } = e.target;
    setData((prev: any) => ({
      ...prev,
      [name]: value,
    }));
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-black">
      <div className="bg-gray-800 p-8 rounded-lg shadow-md w-[400px]">
        <h2 className="text-2xl font-bold mb-6 text-center text-white">Reset Password</h2>
        <div className="grid mb-4">
          <label className="mb-2 text-gray-300">Password</label>
          <input
            type={showPassword ? "text" : "password"}
            name="password"
            value={data?.password}
            onChange={handleChange}
            className="p-2 border border-gray-600 rounded bg-gray-700 text-white"
          />
        </div>
        <div className="grid mb-6">
          <label className="mb-2 text-gray-300">Confirm Password</label>
          <input
            type={showPassword ? "text" : "password"}
            name="confirmPassword"
            value={data?.confirmPassword}
            onChange={handleChange}
            className="p-2 border border-gray-600 rounded bg-gray-700 text-white"
          />
        </div>
        <div className="mb-4 cursor-pointer hover:underline text-sm text-blue-400" onClick={() => setShowPassword(!showPassword)}>
          {showPassword ? "Hide passwords" : "Show passwords"}
        </div>
        <div>
          <button
            onClick={confirmPassword}
            className="w-full bg-blue-500 text-white py-2 rounded hover:bg-blue-600 transition duration-200"
          >
            Confirm
          </button>
        </div>
      </div>
    </div>
  );
}
