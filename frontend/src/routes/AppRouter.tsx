import { createBrowserRouter, RouterProvider } from 'react-router'; 
import Login from '../pages/Login/Login';
import Home from '../pages/Home/Home';
import OthersBets from '../pages/OthersBets/OthersBets';
import Leaderboard from '../pages/Leaderboard/Leaderboard';
import Rules from '../pages/Rules/Rules';
import Games from '../pages/Games/Games';
import UserDetails from '../pages/UserDetails/UserDetails';
import ProtectedRoute from '../components/ProtectedRoute';

const router = createBrowserRouter([
  {
    path: '/',
    element: (
      <ProtectedRoute>
        <Home />
      </ProtectedRoute>
    ),
    children: [
      { index: true, element: <Leaderboard /> },
      { path: 'leaderboard', element: <Leaderboard /> },
      { path: 'rules', element: <Rules /> },
      { path: 'games', element: <Games /> },
      { path: 'others-bets', element: <OthersBets /> },
      { path: 'profile', element: <UserDetails /> },
    ],
  },
  { path: '/login', element: <Login /> },
]);

export default function AppRouter() {
  return <RouterProvider router={router} />;
}
