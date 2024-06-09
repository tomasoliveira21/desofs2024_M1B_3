import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import SidebarRow from '../SidebarRow';
import { SVGProps } from 'react';

// Mock Icon component
const MockIcon = (props: SVGProps<SVGSVGElement>) => (
  <svg {...props}>
    <title>Mock Icon</title>
  </svg>
);

describe('SidebarRow', () => {
  it('renders correctly with given props', () => {
    render(<SidebarRow Icon={MockIcon} title="Test Title" />);

    // Check if the title is rendered
    expect(screen.getByText('Test Title')).toBeInTheDocument();

    // Check if the icon is rendered
    const icon = screen.getByTitle('Mock Icon');
    expect(icon).toBeInTheDocument();
    expect(icon).toHaveAttribute('class', 'h-6 w-6');
  });

  it('calls onClick function when clicked', () => {
    const handleClick = jest.fn();
    render(<SidebarRow Icon={MockIcon} title="Test Title" onClick={handleClick} />);

    // Find the clickable div
    const clickableDiv = screen.getByText('Test Title').closest('div');
    expect(clickableDiv).toBeInTheDocument();

    // Simulate click event
    fireEvent.click(clickableDiv!);

    // Check if the handleClick function is called
    expect(handleClick).toHaveBeenCalledTimes(1);
  });
});
