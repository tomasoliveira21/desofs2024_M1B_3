export const fetchProfilePicture = async (sessionToken: string) => {
  try {
    const response = await fetch('http://127.0.0.1:5000/user/profile_picture', {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${sessionToken}`
      }
    });

    if (!response.ok) {
      console.error('Network response was not ok', response.statusText);
      throw new Error('Network response was not ok');
    }

    const blob = await response.blob();
    const url = URL.createObjectURL(blob);
    console.log('Fetched profile picture URL:', url); // Log da URL gerada
    return url;
  } catch (error) {
    console.error('There was a problem with the fetch operation:', error);
    return null;
  }
};
