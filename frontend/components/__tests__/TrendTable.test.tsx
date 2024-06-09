import React from 'react';
import { render, screen } from '@testing-library/react';
import TrendTable from '../TrendTable';

const mockTrends = [
  { position: 1, name: 'Trend 1', count: 1000 },
  { position: 2, name: 'Trend 2', count: 2000 },
  { position: 3, name: 'Trend 3', count: 3000 },
];

describe('TrendTable', () => {
  it('renders correctly with no trends', () => {
    render(<TrendTable trends={[]} />);

    // Check if the table is rendered
    const table = screen.getByRole('table');
    expect(table).toBeInTheDocument();

    // Check if the header is not rendered
    const header = screen.queryByText('Position');
    expect(header).not.toBeInTheDocument();
  });

  it('renders correctly with trends', () => {
    render(<TrendTable trends={mockTrends} />);

    // Check if the table is rendered
    const table = screen.getByRole('table');
    expect(table).toBeInTheDocument();

    // Check if the header is rendered
    expect(screen.getByText('Position')).toBeInTheDocument();
    expect(screen.getByText('Name')).toBeInTheDocument();
    expect(screen.getByText('Count')).toBeInTheDocument();

    // Check if the trends are rendered
    mockTrends.forEach(trend => {
      expect(screen.getByText(`#${trend.position}`)).toBeInTheDocument();
      expect(screen.getByText(trend.name)).toBeInTheDocument();
      expect(screen.getByText(trend.count)).toBeInTheDocument();
    });
  });
});
