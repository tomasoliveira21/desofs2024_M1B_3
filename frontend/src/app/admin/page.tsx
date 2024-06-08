"use client";

import { supabase } from "@/lib/supabase";
import { useEffect, useState } from "react";
import { Session } from "@supabase/auth-helpers-nextjs";
import { Toaster } from "react-hot-toast";
import { ToastContainer } from "react-toastify";
import Sidebar from "../../../components/Sidebar";
import "react-toastify/dist/ReactToastify.css";
import { fetchTrends } from "@/api/fetchTrends";
import TrendTable from "../../../components/TrendTable";
import { fetchTweets } from "@/api/fetchTweets";
import TweetComponent from "../../../components/Tweet";

export default function Admin() {
  const [session, setSession] = useState<Session | null>(null);
  const [tweets, setTweets] = useState<any[]>([]);
  const [trends, setTrends] = useState<any[]>([]);
  const isAdmin = true;

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
        setTrends(trendsData);
      }
    }
    getTrends();
  }, [session]);

  useEffect(() => {
    const getTweets = async () => {
      if (session) {
        const fetchedTweets = await fetchTweets(session.access_token);
        setTweets(fetchedTweets);
      }
    };

    getTweets();
  }, [session]);

  if (!session) {
    return <div>Loading...</div>;
  }

  return (
    <div className="lg:max-w-6xl mx-auto mx-h-screen overflow-hidden">
      <main className="grid grid-cols-9">
        <Sidebar session={session} />
        <div className="col-span-7 lg:col-span-5">
          <div className="flex items-center justify-between">
            <h1 className="pl-40 pt-10 pb-0 text-xl font-bold">Manage Posts</h1>
          </div>

          <div className="pt-10 text-md">
            {tweets.map((tweet) => (
              <TweetComponent key={tweet.id} tweet={tweet} isAdmin={isAdmin} session={session}/>
            ))}
          </div>
        </div>
      </main>
    </div>
  );
}
