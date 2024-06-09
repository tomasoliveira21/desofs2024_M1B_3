export const postProfilePicture = async (sessionToken: string, image: string) => {
  try {
    const fetchResponse = await fetch(image);
    const blob = await fetchResponse.blob();

    const formData = new FormData();
    formData.append('image', blob, 'profile_picture.jpg');

    const response = await fetch('http://127.0.0.1:5000/user/profile_picture', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${sessionToken}`,
      },
      body: formData,
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
