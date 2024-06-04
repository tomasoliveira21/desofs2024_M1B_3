import React from 'react';

import {
  BellIcon,
  HashtagIcon,
  MailIcon,
  UserIcon,
  HomeIcon,
  LogoutIcon
} from '@heroicons/react/outline';

import SidebarRow from './SidebarRow';  
import { useRouter } from 'next/navigation';
import { supabase } from '@/lib/supabase';

const Sidebar: React.FC = () => {
  const router = useRouter();

  const logout = async () => {
    await supabase.auth.signOut();
    router.refresh();
  };

  const goToHome = () => {
    router.push('/');
  };

  const goToExplore = () => {
    router.push('/explore');
  };

  const goToProfile = () => {
    router.push('/profile');
  };

  return (
    <div className='flex flex-col col-span-2 items-center px-4 md:items-start'>
      <img className="m-1 h-13 w-20" src="/soc.png" alt=""/>
      <SidebarRow Icon={HomeIcon} title="Home" onClick={goToHome}/>
      <SidebarRow Icon={HashtagIcon} title="Explore" onClick={goToExplore}/>
      <SidebarRow Icon={UserIcon} title="Profile" onClick={goToProfile}/>
      <SidebarRow Icon={BellIcon} title="Notifications"/>
      <SidebarRow Icon={MailIcon} title="Messages"/>
      <SidebarRow Icon={LogoutIcon} title="Sign Out" onClick={logout}/>
    </div>
  );
}

export default Sidebar;
