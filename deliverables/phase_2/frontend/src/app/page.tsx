import Head from "next/head";
import Sidebar from "../../components/Sidebar";
import Feed from "../../components/Feed";
import Widgets from "../../components/Widgets";

export default function Home() {
  return (
    <div className="lg: max-w-6xl mx-auto mx-h-screen overflow-hidden">
      <main className="grid grid-cols-9">
        {/* SideBar */}
        <Sidebar />

        {/* Feed */}
        <Feed />
 
        {/* Widgets */}
        <Widgets />
      </main>
    </div>
  );
}
