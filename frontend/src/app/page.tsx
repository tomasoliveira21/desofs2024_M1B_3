"use client";

import Sidebar from "../../components/Sidebar";
import Feed from "../../components/Feed";
import Widgets from "../../components/Widgets";
import { supabase } from "@/lib/supabase";
import { useEffect, useState } from "react";
import { Session } from "@supabase/auth-helpers-nextjs";

export default function Home() {
  const [session, setSession] = useState<Session | null>(null);

  useEffect(() => {
    async function getSession() {
      const {
        data: { session },
      } = await supabase.auth.getSession();
      setSession(session);
    }
    getSession();
  }, []);

  if (!session) {
    return <div>Loading...</div>;
  }

  return (
    <div className="lg:max-w-6xl mx-auto mx-h-screen overflow-hidden">
      <main className="grid grid-cols-9">
        <Sidebar />
        <Feed session={session} />
        <Widgets />
      </main>
    </div>
  );
}
