import React from 'react';
import { render, screen } from '@testing-library/react';
import Widgets from '../Widgets';
import { SearchIcon } from '@heroicons/react/outline';

jest.mock('react-twitter-embed', () => ({
  TwitterTimelineEmbed: () => <div data-testid="twitter-timeline-embed" />,
}));

describe('Widgets', () => {
  it('renders correctly', () => {
    render(<Widgets />);

    // Check if the search icon is rendered
    const searchIcon = screen.getByRole('img', { name: /search icon/i });
    expect(searchIcon).toBeInTheDocument();

    // Check if the search input is rendered
    const searchInput = screen.getByPlaceholderText('Search SocialNet');
    expect(searchInput).toBeInTheDocument();

    // Check if the Twitter timeline embed is rendered
    expect(screen.getByTestId('twitter-timeline-embed')).toBeInTheDocument();
  });
});
