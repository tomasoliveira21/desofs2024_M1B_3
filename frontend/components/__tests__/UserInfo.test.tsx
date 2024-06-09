import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import UserInfo from '../UserInfo';

describe('UserInfo', () => {
  const mockHandleImageChange = jest.fn();
  const mockProps = {
    selectedImage: 'https://example.com/profile.jpg',
    handleImageChange: mockHandleImageChange,
    userName: 'mockuser',
    email: 'mockuser@example.com',
  };

  it('renders correctly with given props', () => {
    render(<UserInfo {...mockProps} />);

    // Check if the profile heading is rendered
    expect(screen.getByText('Profile')).toBeInTheDocument();

    // Check if the profile image is rendered
    const profileImage = screen.getByAltText('Profile');
    expect(profileImage).toBeInTheDocument();
    expect(profileImage).toHaveAttribute('src', mockProps.selectedImage);

    // Check if the user name and email are rendered
    expect(screen.getByText(`User name: ${mockProps.userName}`)).toBeInTheDocument();
    expect(screen.getByText(`Email: ${mockProps.email}`)).toBeInTheDocument();
  });

  it('calls handleImageChange when image input is changed', () => {
    render(<UserInfo {...mockProps} />);

    const fileInput = screen.getByLabelText('✎');
    expect(fileInput).toBeInTheDocument();

    // Simulate file input change
    fireEvent.change(fileInput, { target: { files: [new File([''], 'profile.jpg', { type: 'image/jpeg' })] } });

    // Check if handleImageChange function is called
    expect(mockHandleImageChange).toHaveBeenCalled();
  });
});
