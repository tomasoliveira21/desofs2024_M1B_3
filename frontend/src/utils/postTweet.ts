export const postTweet = async (sessionToken: string, tweetContent: string) => {
    try {
      const response = await fetch('http://127.0.0.1:5000/tweet', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${sessionToken}`
        },
        body: JSON.stringify({
          content: tweetContent
        })
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await response.json();
      console.log('Tweet posted successfully:', data);
    } catch (error) {
      console.error('There was a problem with the fetch operation:', error);
    }
  };