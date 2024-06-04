"use client";

import React from 'react';
import Sidebar from '../../../components/Sidebar';

export default function Profile() {
  return (
    <div className="lg:max-w-6xl mx-auto mx-h-screen overflow-hidden">
      <main className="grid grid-cols-9">
        <Sidebar />
      </main>
    </div>
  );
}