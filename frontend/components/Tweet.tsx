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
          src="https://links.papareact.com/gll"
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
