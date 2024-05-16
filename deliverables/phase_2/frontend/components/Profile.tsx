// components/Profile.js
import { RefreshIcon } from '@heroicons/react/outline';
import React from 'react';
import Tweetbox from './Tweetbox';
import Tweet from './Tweet';

const Profile = () => {
    return (
        <div className='col-span-7 lg:col-span-5'>

            {/* User Bio */}
            <div className="bg-gray-100 p-4 mt-4 rounded-lg w-full max-w-3x1">
                {/* User Photo */}
                <div><img
                    className="rounded-full h-24 w-24"
                    src="ronaldo.jpg" alt=""
                /></div>
                <h2 className="text-xl font-bold mb-2">Cristiano Ronaldo</h2>
                <p className="text-gray-600">Welcome to the official page of Cristiano Ronaldo..</p>
            </div>

            {/* Tweetbox */}
            <div className="w-full max-w-3x1 mt-4">
                <Tweet />
            </div>
        </div>
    );
};

export default Profile;
