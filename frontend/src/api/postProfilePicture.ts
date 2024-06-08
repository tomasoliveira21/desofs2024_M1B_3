export const postProfilePicture = async (sessionToken: string, image: string) => {
    try {
      const response = await fetch('http://127.0.0.1:5000/user/profile_picture', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${sessionToken}`
        },
        body: JSON.stringify({
          image: image,
        }),
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
  