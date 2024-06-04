import React from "react";
import TimeAgo from "react-timeago";
import { ChatAlt2Icon, HeartIcon, UploadIcon } from "@heroicons/react/outline";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faRetweet } from "@fortawesome/free-solid-svg-icons";

function Tweet({ tweet }: any) {
  return (
    <div className="flex flex-col space-x-3 border-y p-5 border-gray-100">
      <div className="flex space-x-3">
        <img
          className="h-10 w-10 object-cover rounded-full"
          src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/2f78629c-8d75-479c-8387-43b742f81e09/de4vbn3-0913b9a0-2c24-4882-b8a1-9ef71450bf8e.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzJmNzg2MjljLThkNzUtNDc5Yy04Mzg3LTQzYjc0MmY4MWUwOVwvZGU0dmJuMy0wOTEzYjlhMC0yYzI0LTQ4ODItYjhhMS05ZWY3MTQ1MGJmOGUucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.6MXaLcwFyC2W1gZi0w07LGvDimzy8P8K-ijkE6gmDeg"
          alt=""
        />

        <div>
          <div className="flex items-center space-x-1">
            <p className="mr-1 font-bold">{tweet.user_uuid}</p>

            <TimeAgo
              className="text-sm text-gray-500"
              date={tweet.created_at}
            />
          </div>

          <p>{tweet.content}</p>

          {tweet.image && (
            <img
              src={tweet.image}
              alt=""
              className="m-5 ml-0 mb-1 max-h-60 rounded-lg object-cover shadow-sm"
            />
          )}
        </div>
      </div>
      <div className="mt-5 flex justify-between">
        <div className="flex cursor-pointer items-center space-x-3 text-gray-400">
          <ChatAlt2Icon className="h-5 w-5" />
          <p>7</p>
        </div>
        <div className="flex cursor-pointer items-center space-x-3 text-gray-400">
          <FontAwesomeIcon icon={faRetweet} className="h-5 w-5" />
        </div>
        <div className="flex cursor-pointer items-center space-x-3 text-gray-400">
          <HeartIcon className="h-5 w-5" />
        </div>
        <div className="flex cursor-pointer items-center space-x-3 text-gray-400">
          <UploadIcon className="h-5 w-5" />
        </div>
      </div>
    </div>
  );
}

export default Tweet;
