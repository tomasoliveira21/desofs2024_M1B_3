import { toast } from "react-toastify";

export const postTweet = async (sessionToken: string, tweetContent: string) => {
  try {
    const response = await fetch("http://127.0.0.1:5000/tweet", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${sessionToken}`,
      },
      body: JSON.stringify({
        content: tweetContent,
      }),
    });

    if (!response.ok) {
      throw new Error("Network response was not ok");
    }

    toast.success("Tweet posted successfully!", {
      position: "bottom-right",
      autoClose: 5000,
      hideProgressBar: false,
      closeOnClick: true,
      pauseOnHover: true,
      draggable: true,
      progress: undefined,
      theme: "colored",
    });
  } catch (error) {
    toast.error('Failed to post tweet', {
      position: "bottom-right",
      autoClose: 5000,
      hideProgressBar: false,
      closeOnClick: true,
      pauseOnHover: true,
      draggable: true,
      progress: undefined,
      theme: "colored",
      });  }
};
