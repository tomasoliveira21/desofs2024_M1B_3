export const fetchTweetsByUser = async (sessionToken: string, userUUID: string) => {
    try {
      const response = await fetch(`http://127.0.0.1:5000/tweet/${userUUID}`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${sessionToken}`
        }
      });
  
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
  
      const data = await response.json();
      return data;
    } catch (error) {
      console.error('There was a problem with the fetch operation:', error);
    }
  };
  