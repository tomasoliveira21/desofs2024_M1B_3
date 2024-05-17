"use client"

import Sidebar from "../../components/Sidebar";
import Feed from "../../components/Feed";
import Widgets from "../../components/Widgets";

export default function Home() {
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
