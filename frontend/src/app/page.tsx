"use client"

import Sidebar from "../../components/Sidebar";
import Feed from "../../components/Feed";
import Widgets from "../../components/Widgets";
import { supabase } from "@/lib/supabase";
import { useRouter } from "next/navigation";

export default function Home() {

  /*
  const router = useRouter();


  const logout = async () => {
    await supabase
      .auth
      .signOut()

    router.refresh();
  }
  */

  return (
    <div className="lg:max-w-6xl mx-auto mx-h-screen overflow-hidden">
      <main className="grid grid-cols-9">
        <Sidebar />

        <Feed />
 
        <Widgets />
      </main>
    </div>
  );
}
