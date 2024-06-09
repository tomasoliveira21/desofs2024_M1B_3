import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import Sidebar from '../Sidebar';
import { Session } from '@supabase/auth-helpers-nextjs';
import { useRouter } from 'next/navigation';
import { fetchUser } from '@/api/fetchUser';
import { supabase } from '@/lib/supabase';

// Mock the necessary modules
jest.mock('next/navigation', () => ({
  useRouter: jest.fn(),
}));
jest.mock('@/api/fetchUser');
jest.mock('@/lib/supabase', () => ({
  supabase: {
    auth: {
      signOut: jest.fn(),
    },
  },
}));

const mockSession: Session = {
  access_token: 'mock_access_token',
  // add other necessary session properties if needed
} as Session;

const mockUser = {
  role: {
    name: 'admin',
  },
};

describe('Sidebar', () => {
  beforeEach(() => {
    (fetchUser as jest.Mock).mockResolvedValue(mockUser);
    (useRouter as jest.Mock).mockReturnValue({
      push: jest.fn(),
      refresh: jest.fn(),
    });
  });

  afterEach(() => {
    jest.clearAllMocks();
  });

  it('renders correctly and matches snapshot', async () => {
    const { asFragment } = render(<Sidebar session={mockSession} />);
    
    // Wait for useEffect to finish
    await waitFor(() => expect(fetchUser).toHaveBeenCalledWith(mockSession.access_token));

    // Check if loading is gone
    expect(screen.queryByText('Loading...')).not.toBeInTheDocument();

    // Check if elements are rendered
    expect(screen.getByText('Home')).toBeInTheDocument();
    expect(screen.getByText('Profile')).toBeInTheDocument();
    expect(screen.getByText('Notifications')).toBeInTheDocument();
    expect(screen.getByText('Messages')).toBeInTheDocument();
    expect(screen.getByText('Manage')).toBeInTheDocument();
    expect(screen.getByText('Sign Out')).toBeInTheDocument();

    // Snapshot test
    expect(asFragment()).toMatchSnapshot();
  });

  it('calls logout and navigates correctly', async () => {
    render(<Sidebar session={mockSession} />);
    
    // Wait for useEffect to finish
    await waitFor(() => expect(fetchUser).toHaveBeenCalledWith(mockSession.access_token));

    const { push, refresh } = useRouter();

    // Test navigation to Home
    fireEvent.click(screen.getByText('Home'));
    expect(push).toHaveBeenCalledWith('/');

    // Test navigation to Profile
    fireEvent.click(screen.getByText('Profile'));
    expect(push).toHaveBeenCalledWith('/profile');

    // Test navigation to Trends
    fireEvent.click(screen.getByText('Trends'));
    expect(push).toHaveBeenCalledWith('/trends');

    // Test navigation to Manage
    fireEvent.click(screen.getByText('Manage'));
    expect(push).toHaveBeenCalledWith('/admin');

    // Test logout
    fireEvent.click(screen.getByText('Sign Out'));
    expect(supabase.auth.signOut).toHaveBeenCalled();
    expect(refresh).toHaveBeenCalled();
  });
});
