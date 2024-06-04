"use client";

import React from "react";
import Sidebar from "../../../components/Sidebar";
import { fetchTrends } from "@/utils/fetchTrends";

export default function Explore() {

  //const test = fetchTrends

  return (
    <div className="lg:max-w-6xl mx-auto mx-h-screen overflow-hidden">
      <main className="grid grid-cols-9">
        <Sidebar/>
        <div className="col-span-7 lg:col-span-5">
          <div className="flex items-center justify-between">
            <h1 className="pl-40 pt-10 pb-0 text-xl font-bold">Trends</h1>
          </div>

          <div>
            <p className="pl-40 pt-10 text-md">text</p>
          </div>
        </div>
      </main>
    </div>
  );
}
