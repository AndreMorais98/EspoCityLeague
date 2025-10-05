import './App.css';
import AppRouter from './routes/AppRouter';
import { UserProvider } from './contexts/UserContext';

function App() {
  return (
    <UserProvider>
      <AppRouter />
    </UserProvider>
  );
}

export default App;

