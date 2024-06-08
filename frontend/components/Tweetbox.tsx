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
import { postTweet } from "@/api/postTweet";

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
        src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/2f78629c-8d75-479c-8387-43b742f81e09/de4vbn3-0913b9a0-2c24-4882-b8a1-9ef71450bf8e.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzJmNzg2MjljLThkNzUtNDc5Yy04Mzg3LTQzYjc0MmY4MWUwOVwvZGU0dmJuMy0wOTEzYjlhMC0yYzI0LTQ4ODItYjhhMS05ZWY3MTQ1MGJmOGUucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.6MXaLcwFyC2W1gZi0w07LGvDimzy8P8K-ijkE6gmDeg"
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
