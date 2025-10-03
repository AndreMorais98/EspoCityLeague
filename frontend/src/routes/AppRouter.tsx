import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import Login from '../pages/Login/Login';
import Home from '../pages/Home/Home';
import OthersBets from '../pages/OthersBets/OthersBets';
import Leaderboard from '../pages/Leaderboard/Leaderboard';
import Rules from '../pages/Rules/Rules';
import Games from '../pages/Games/Games';

const router = createBrowserRouter([
  {
    path: '/',
    element: <Home />,
    children: [
      { index: true, element: <Games /> },
      { path: 'leaderboard', element: <Leaderboard /> },
      { path: 'rules', element: <Rules /> },
      { path: 'games', element: <Games /> },
      { path: '/others-bets', element: <OthersBets /> },
    ],
  },
  { path: '/login', element: <Login /> },
]);

export default function AppRouter() {
  return <RouterProvider router={router} />;
}
