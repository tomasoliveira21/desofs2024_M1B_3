import React, { useState } from "react";
import {
  BellIcon,
  HashtagIcon,
  BookmarkIcon,
  CollectionIcon,
  DotsCircleHorizontalIcon,
  MailIcon,
  UserIcon,
  HomeIcon,
  SearchCircleIcon,
  EmojiHappyIcon,
  CalendarIcon,
  LocationMarkerIcon,
  PhotographIcon,
} from "@heroicons/react/outline";
import { Session } from "@supabase/auth-helpers-nextjs";
import { postTweet } from "@/utils/postTweet";

interface TweetboxProps {
  session: Session;
}

function Tweetbox({ session }: TweetboxProps) {
  const sessionToken = session.access_token;
  const [input, setInput] = useState<string>("");

  const handleSubmit = (e: { preventDefault: () => void; }) => {
    e.preventDefault();
    postTweet(sessionToken, input);
    setInput("");
  };

  return (
    <div className="flex space-x-2 p-5">
      <img
        className="h-14 w-14 object-cover rounded-full mt-4"
        src="https://links.papareact.com/gll"
        alt=""
      />

      <div className="flex flex-1 items-center pl-2">
        <form className="flex flex-1 flex-col" onSubmit={handleSubmit}>
          <input
            value={input}
            onChange={(text) => setInput(text.target.value)}
            type="text"
            placeholder="What's Happening?"
            className="h-24 w-full text-xl outline-none placeholder:text-xl text-black"
          />
          <div className="flex items-center">
            <div className="flex space-x-2 text-socialNet flex-1">
              <PhotographIcon className="h-5 w-5 cursor-pointer transition-transform duration-150 ease-out hover:scale-150" />
              <SearchCircleIcon className="h-5 w-5" />
              <EmojiHappyIcon className="h-5 w-5" />
              <CalendarIcon className="h-5 w-5" />
              <LocationMarkerIcon className="h-5 w-5" />
            </div>

            <button
              disabled={!input}
              className="bg-socialNet px-5 py-2 font-bold text-white rounded-full disabled:opacity-40"
            >
              Tweet
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default Tweetbox;
