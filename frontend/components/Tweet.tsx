import React from "react";
import TimeAgo from "react-timeago";
import {
  ChatAlt2Icon,
  HeartIcon,
  UploadIcon,
  TrashIcon,
} from "@heroicons/react/outline";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faRetweet } from "@fortawesome/free-solid-svg-icons";
import { deleteTweet } from "@/api/deleteTweet";
import toast from "react-hot-toast";

function Tweet({ tweet, isAdmin, userInfo, session, profilePicture }: any) {

  const handleDelete = async () => {
    await deleteTweet(session.access_token, tweet.uuid);
  };

  return (
    <div className="max-w-lg mx-auto">
      <div className="flex flex-col space-x-3 border-y p-5 border-gray-100 break-words">
        <div className="flex space-x-3">
          <img
            className="h-10 w-10 object-cover rounded-full"
            src={profilePicture ? profilePicture : "https://miamistonesource.com/wp-content/uploads/2018/05/no-avatar-25359d55aa3c93ab3466622fd2ce712d1.jpg"}
            alt=""
          />

          <div className="w-full">
            <div className="flex items-center justify-between">
              <div className="flex items-center space-x-1">
                <p className="mr-1 font-bold">
                  {userInfo ? userInfo.username : tweet.user_uuid}
                </p>

                <TimeAgo
                  className="text-sm text-gray-500"
                  date={tweet.created_at}
                />

                {isAdmin && (
                  <TrashIcon
                    className="h-5 w-5 text-red-500 cursor-pointer"
                    onClick={handleDelete}
                  />
                )}
              </div>
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
    </div>
  );
}

export default Tweet;
