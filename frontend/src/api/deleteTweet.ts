export const deleteTweet = async (sessionToken: string, tweetUUID: string) => {
  try {
    const response = await fetch("http://127.0.0.1:5000/tweet", {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${sessionToken}`,
      },
      body: JSON.stringify({
        uuid: tweetUUID,
      }),
    });

    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
  } catch (error) {
    console.log(error);
  }
};