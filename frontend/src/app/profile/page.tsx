"use client";

import React, { useEffect, useState } from "react";
import Sidebar from "../../../components/Sidebar";
import UserInfo from "../../../components/UserInfo";
import { Session } from "@supabase/auth-helpers-nextjs";
import { supabase } from "@/lib/supabase";
import { fetchTweetsByUser } from "@/api/fetchTweetsByUser";
import TweetComponent from "../../../components/Tweet";
import { fetchUser } from "@/api/fetchUser";
import { fetchProfilePicture } from "@/api/fetchProfilePicture";

export default function Profile() {
  const [session, setSession] = useState<Session | null>(null);
  const [tweets, setTweets] = useState<any[]>([]);
  const [selectedImage, setSelectedImage] = useState(
    "https://miamistonesource.com/wp-content/uploads/2018/05/no-avatar-25359d55aa3c93ab3466622fd2ce712d1.jpg"
  );
  const [userData, setUserData] = useState<any>();

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

  useEffect(() => {
    const getUser = async () => {
      if (session) {
        const fetchedUser = await fetchUser(session.access_token);
        setUserData(fetchedUser);
      }
    };

    getUser();
  }, [session]);

  useEffect(() => {
    const getProfilePicture = async () => {
      if (session) {
        const fetchedProfilePicture = await fetchProfilePicture(session.access_token);
        if (fetchedProfilePicture) {
          setSelectedImage(fetchedProfilePicture);
        } else {
          console.error('Fetched profile picture is null');
        }
      }
    };

    getProfilePicture();
  }, [session]);

  if (!session) {
    return <div>Loading...</div>;
  }

  if (!userData) {
    return <div>Loading...</div>;
  }

  return (
    <div className="lg:max-w-6xl mx-auto h-auto overflow-hidden bg-black">
      <main className="grid grid-cols-9 h-full text-white">
        <Sidebar session={session}/>
        <div className="col-span-7 flex flex-col items-start">
          <UserInfo
            selectedImage={selectedImage}
            handleImageChange={handleImageChange}
            userName={userData.username}
            email={userData.email}
          />
          <div className="w-full mt-4">
            {tweets.map((tweet) => (
              <TweetComponent key={tweet.id} tweet={tweet} userInfo={userData} profilePicture={selectedImage}/>
            ))}
          </div>
        </div>
      </main>
    </div>
  );
}
