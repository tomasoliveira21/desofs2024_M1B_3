import React, { useEffect, useState } from "react";

import {
  BellIcon,
  HashtagIcon,
  MailIcon,
  UserIcon,
  HomeIcon,
  LogoutIcon,
  CogIcon,
} from "@heroicons/react/outline";

import SidebarRow from "./SidebarRow";
import { useRouter } from "next/navigation";
import { supabase } from "@/lib/supabase";
import { Session } from "@supabase/auth-helpers-nextjs";
import { fetchUser } from "@/utils/fetchUser";

interface FeedProps {
  session?: Session;
}

function Sidebar({ session }: FeedProps) {
  const router = useRouter();
  const [userData, setUserData] = useState<any>();

  const logout = async () => {
    await supabase.auth.signOut();
    router.refresh();
  };

  const goToHome = () => {
    router.push("/");
  };

  const goToExplore = () => {
    router.push("/trends");
  };

  const goToProfile = () => {
    router.push("/profile");
  };

  const goToAdmin = () => {
    router.push("/admin");
  };

  useEffect(() => {
    const getTweets = async () => {
      if (session) {
        const fetchedUser = await fetchUser(session.access_token);
        setUserData(fetchedUser);
      }
    };

    getTweets();
  }, [session]);

  if (!userData) {
    return <div>Loading...</div>;
  }

  return (
    <div className="flex flex-col col-span-2 items-center px-4 md:items-start">
      <img className="m-1 h-13 w-20" src="/soc.png" alt="" />
      <SidebarRow Icon={HomeIcon} title="Home" onClick={goToHome} />
      {userData?.role.name === "premium" || userData?.role.name === "admin" ? (
        <SidebarRow Icon={HashtagIcon} title="Trends" onClick={goToExplore} />
      ) : null}
      <SidebarRow Icon={UserIcon} title="Profile" onClick={goToProfile} />
      <SidebarRow Icon={BellIcon} title="Notifications" />
      <SidebarRow Icon={MailIcon} title="Messages" />
      {userData?.role.name === "admin" ? (
        <SidebarRow Icon={CogIcon} title="Manage" onClick={goToAdmin} />
      ) : null}
      <SidebarRow Icon={LogoutIcon} title="Sign Out" onClick={logout} />
    </div>
  );
}

export default Sidebar;
