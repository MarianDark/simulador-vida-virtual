import { render, screen } from '@testing-library/react';
import App from './App';

test('renders simulador de vida virtual con IA', () => {
  render(<App />);
  const headingElement = screen.getByText(/Simulador de Vida Virtual con IA/i);
  expect(headingElement).toBeInTheDocument();
});
