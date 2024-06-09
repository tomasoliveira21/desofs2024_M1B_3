import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import Tweet from '../Tweet';
import { deleteTweet } from '@/api/deleteTweet';
import '@testing-library/jest-dom/extend-expect';

// Mock the deleteTweet API
jest.mock('@/api/deleteTweet');

const mockTweet = {
  uuid: '1',
  user_uuid: 'user-123',
  content: 'This is a tweet',
  created_at: new Date().toISOString(),
  image: 'https://example.com/image.jpg',
};

const mockSession = {
  access_token: 'mock_access_token',
};

const mockUserInfo = {
  username: 'mockuser',
};

describe('Tweet', () => {
  afterEach(() => {
    jest.clearAllMocks();
  });

  it('renders correctly with all props', () => {
    render(
      <Tweet
        tweet={mockTweet}
        isAdmin={true}
        userInfo={mockUserInfo}
        session={mockSession}
        profilePicture="https://example.com/profile.jpg"
      />
    );

    // Check if the tweet content is rendered
    expect(screen.getByText('This is a tweet')).toBeInTheDocument();

    // Check if the username is rendered
    expect(screen.getByText('mockuser')).toBeInTheDocument();

    // Check if the profile picture is rendered
    expect(screen.getByAltText('')).toHaveAttribute('src', 'https://example.com/profile.jpg');

    // Check if the image is rendered
    expect(screen.getByAltText('')).toHaveAttribute('src', 'https://example.com/image.jpg');

    // Check if the delete icon is rendered
    expect(screen.getByRole('button', { name: /trash/i })).toBeInTheDocument();
  });

  it('calls handleDelete when delete icon is clicked', async () => {
    render(
      <Tweet
        tweet={mockTweet}
        isAdmin={true}
        userInfo={mockUserInfo}
        session={mockSession}
        profilePicture="https://example.com/profile.jpg"
      />
    );

    // Simulate click event on delete icon
    fireEvent.click(screen.getByRole('button', { name: /trash/i }));

    // Check if the deleteTweet function is called
    await waitFor(() => {
      expect(deleteTweet).toHaveBeenCalledWith(mockSession.access_token, mockTweet.uuid);
    });
  });
});
