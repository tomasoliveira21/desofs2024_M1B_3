import { RefreshIcon } from "@heroicons/react/outline";
import React, { useState, useEffect } from "react";
import Tweetbox from "./Tweetbox";
import { Session } from "@supabase/auth-helpers-nextjs";
import { fetchTweets } from "@/api/fetchTweets";
import TweetComponent from "./Tweet";
import toast from "react-hot-toast";
import { fetchProfilePicture } from "@/api/fetchProfilePicture";

interface FeedProps {
  session: Session;
}

function Feed({ session }: FeedProps) {
  const [tweets, setTweets] = useState<any[]>([]);
  const [profileImage, setProfileImage] = useState<any>();

  useEffect(() => {
    const getTweets = async () => {
      const fetchedTweets = await fetchTweets(session.access_token);
      setTweets(fetchedTweets);
    };

    getTweets();
  }, [session]);

  useEffect(() => {
    const getProfilePicture = async () => {
      if (session) {
        const fetchedProfilePicture = await fetchProfilePicture(session.access_token);
        if (fetchedProfilePicture) {
          setProfileImage(fetchedProfilePicture);
        } else {
          console.error('Fetched profile picture is null');
        }
      }
    };

    getProfilePicture();
  }, [session]);

  const handleRefresh = async () => {
    const refreshToast = toast.loading('Refreshing...'); 

    const tweets = await fetchTweets(session.access_token);
    setTweets(tweets);

    toast.success('Feed updated!', {
      id: refreshToast
    })
  }

  return (
    <div className="col-span-7 lg:col-span-5">
      <div className="flex items-center justify-between">
        <h1 className="p-5 pb-0 text-xl font-bold">Home</h1>
        <RefreshIcon onClick={handleRefresh} className="h-8 w-8 cursor-pointer text-socialNet mr-5 mt-5 transition-all duration-500 ease-out hover:rotate-180 active:scale-125" />
      </div>

      {/* Tweetbox */}
      <div>
        <Tweetbox session={session} profilePicture={profileImage}/>
      </div>

      {/* Feed */}
      <div>
        {tweets.map((tweet) => (
          <TweetComponent key={tweet.id} tweet={tweet} />
        ))}
      </div>
    </div>
  );
}

export default Feed;
