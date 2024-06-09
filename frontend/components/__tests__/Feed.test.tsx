// frontend/components/__tests__/Feed.test.tsx
import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import Feed from '../Feed';
import { Session } from '@supabase/auth-helpers-nextjs';
import { fetchTweets } from '@/api/fetchTweets';
import toast from 'react-hot-toast';

// Mock the necessary modules
jest.mock('@/api/fetchTweets');
jest.mock('react-hot-toast');

const mockSession: Session = {
  access_token: 'mock_access_token',
  // add other necessary session properties if needed
} as Session;

const mockTweets = [
  { id: 1, content: 'First tweet' },
  { id: 2, content: 'Second tweet' },
];

describe('Feed', () => {
  beforeEach(() => {
    (fetchTweets as jest.Mock).mockResolvedValue(mockTweets);
    (toast.loading as jest.Mock).mockReturnValue('loading-toast-id');
    (toast.success as jest.Mock).mockReturnValue('success-toast-id');
  });

  afterEach(() => {
    jest.clearAllMocks();
  });

  it('renders correctly and matches snapshot', async () => {
    const { asFragment } = render(<Feed session={mockSession} />);
    
    // Wait for useEffect to finish
    await waitFor(() => expect(fetchTweets).toHaveBeenCalledWith(mockSession.access_token));

    // Check if tweets are rendered
    expect(screen.getByText('First tweet')).toBeInTheDocument();
    expect(screen.getByText('Second tweet')).toBeInTheDocument();

    // Snapshot test
    expect(asFragment()).toMatchSnapshot();
  });

  it('handles refresh correctly', async () => {
    render(<Feed session={mockSession} />);
    
    // Wait for initial fetch to complete
    await waitFor(() => expect(fetchTweets).toHaveBeenCalledTimes(1));

    const refreshIcon = screen.getByRole('button');
    fireEvent.click(refreshIcon);

    // Wait for refresh fetch to complete
    await waitFor(() => expect(fetchTweets).toHaveBeenCalledTimes(2));
    expect(toast.loading).toHaveBeenCalledWith('Refreshing...');
    expect(toast.success).toHaveBeenCalledWith('Feed updated!', { id: 'loading-toast-id' });
  });
});
