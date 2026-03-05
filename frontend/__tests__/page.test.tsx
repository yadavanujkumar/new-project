import { render, screen } from '@testing-library/react';
import Home from '../app/page';

describe('Home Dashboard', () => {
  it('renders the main orchestrator heading', () => {
    render(<Home />);
    const heading = screen.getByRole('heading', { name: /MediFed XAI Resource Orchestrator/i });
    expect(heading).toBeInTheDocument();
  });
});
