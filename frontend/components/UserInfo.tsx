import React from 'react'

interface UserInfoProps {
    selectedImage: string;
    handleImageChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
    userName: string;
    email: string;
  }

function UserInfo({ selectedImage, handleImageChange, userName, email }: UserInfoProps) {
    return (
        <div className="col-span-7 lg:col-span-5 p-10 shadow-lg rounded-lg">
          <div className="flex items-center justify-between mb-8">
            <h1 className="text-3xl font-bold text-white">Profile</h1>
          </div>
    
          <div className="text-md">
            <div className="flex items-center mb-5">
              <div className="relative">
                <img
                  className="h-24 w-24 object-cover rounded-full shadow-md transition duration-300 ease-in-out transform hover:scale-105"
                  src={selectedImage}
                  alt="Profile"
                />
                <label htmlFor="fileInput" className="absolute bottom-0 right-0 bg-blue-600 text-white p-2 rounded-full cursor-pointer shadow-md transition duration-300 ease-in-out transform hover:scale-110">
                  &#9998;
                </label>
                <input
                  id="fileInput"
                  type="file"
                  className="hidden"
                  onChange={handleImageChange}
                />
              </div>
              <div className="ml-6">
                <p className="font-semibold text-xl text-gray-100">User name: <span className="text-blue-400">{userName}</span></p>
                <p className="font-semibold text-xl text-gray-100">Email: <span className="text-blue-400">{email}</span></p>
              </div>
            </div>
          </div>
        </div>
      );
}

export default UserInfo;
