"use client";

import { supabase } from "@/lib/supabase";
import { useEffect, useState } from "react";
import { Session } from "@supabase/auth-helpers-nextjs";
import { Toaster } from "react-hot-toast";
import { ToastContainer } from "react-toastify";
import Sidebar from "../../../components/Sidebar";
import "react-toastify/dist/ReactToastify.css";
import { fetchTrends } from "@/utils/fetchTrends";
import TrendTable from "../../../components/TrendTable";

export default function Trends() {

  const [session, setSession] = useState<Session | null>(null);
  const [trends, setTrends] = useState<any[]>([]);

  useEffect(() => {
    async function getSession() {
      const {
        data: { session },
      } = await supabase.auth.getSession();
      setSession(session);
    }
    getSession();
  }, []);

  useEffect(() => {
    async function getTrends() {
      if (session) {
        const trendsData = await fetchTrends(session.access_token);
        setTrends(trendsData.slice(0, 5));
      }
    }
    getTrends();
  }, [session]);

  if (!session) {
    return <div>Loading...</div>;
  }

  return (
    <div className="lg:max-w-6xl mx-auto mx-h-screen overflow-hidden">
      <main className="grid grid-cols-9">
        <Sidebar />
        <div className="col-span-7 lg:col-span-5">
          <div className="flex items-center justify-between">
            <h1 className="pl-40 pt-10 pb-0 text-xl font-bold">Trends</h1>
          </div>

          <div className="pl-40 pt-10 text-md">
            <TrendTable trends={trends} />
          </div>
        </div>
      </main>
    </div>
  );
}
