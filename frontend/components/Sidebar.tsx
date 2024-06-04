import React from 'react'

import {
    BellIcon,
    HashtagIcon,
    MailIcon,
    UserIcon,
    HomeIcon
} from '@heroicons/react/outline';

import SidebarRow from './SidebarRow';  
import { useRouter } from 'next/navigation';
import { supabase } from '@/lib/supabase';

function Sidebar() {

  const router = useRouter();


  const logout = async () => {
    await supabase
      .auth
      .signOut()

    router.refresh();
  }

  return (
    <div className='flex flex-col col-span-2 items-center px-4 md:items-start'>
        <img className="m-1 h-13 w-20" src="/soc.png" alt=""/>
        <SidebarRow Icon={HomeIcon} title="Home"/>
        <SidebarRow Icon={HashtagIcon} title="Explore"/>
        <SidebarRow Icon={BellIcon} title="Notifications"/>
        <SidebarRow Icon={MailIcon} title="Messages"/>
        <SidebarRow Icon={UserIcon} title="Sign Out" onClick={logout}/>
    </div>
  )
}

export default Sidebar