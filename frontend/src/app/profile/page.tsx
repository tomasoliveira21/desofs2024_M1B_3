"use client";

import React, { useEffect, useState } from "react";
import Sidebar from "../../../components/Sidebar";
import UserInfo from "../../../components/UserInfo";
import { Session } from "@supabase/auth-helpers-nextjs";
import { supabase } from "@/lib/supabase";
import { fetchTweetsByUser } from "@/utils/fetchTweetsByUser";
import TweetComponent from "../../../components/Tweet";

export default function Profile() {
  const [session, setSession] = useState<Session | null>(null);
  const [tweets, setTweets] = useState<any[]>([]);
  const [selectedImage, setSelectedImage] = useState(
    "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/2f78629c-8d75-479c-8387-43b742f81e09/de4vbn3-0913b9a0-2c24-4882-b8a1-9ef71450bf8e.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzJmNzg2MjljLThkNzUtNDc5Yy04Mzg3LTQzYjc0MmY4MWUwOVwvZGU0dmJuMy0wOTEzYjlhMC0yYzI0LTQ4ODItYjhhMS05ZWY3MTQ1MGJmOGUucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.6MXaLcwFyC2W1gZi0w07LGvDimzy8P8K-ijkE6gmDeg"
  );

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
    const getTweets = async () => {
      if (session) {
        const fetchedTweets = await fetchTweetsByUser(
          session.access_token
        );
        setTweets(fetchedTweets);
      }
    };

    getTweets();
  }, [session]);

  console.log('tweets: ', tweets);

  const handleImageChange = (e: any) => {
    if (e.target.files && e.target.files[0]) {
      const reader = new FileReader();
      reader.onload = (event) => {
        if (event.target?.result) {
          setSelectedImage(event.target.result as string);
        }
      };
      reader.readAsDataURL(e.target.files[0]);
    }
  };

  if (!session) {
    return <div>Loading...</div>;
  }

  return (
    <div className="lg:max-w-6xl mx-auto h-screen overflow-hidden bg-black">
      <main className="grid grid-cols-9 h-full text-white">
        <Sidebar session={session}/>
        <UserInfo
          selectedImage={selectedImage}
          handleImageChange={handleImageChange}
        />

        <div>
          {tweets.map((tweet) => (
            <TweetComponent key={tweet.id} tweet={tweet} />
          ))}
        </div>
      </main>
    </div>
  );
}
