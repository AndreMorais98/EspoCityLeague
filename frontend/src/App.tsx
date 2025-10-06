import './App.css';
import AppRouter from './routes/AppRouter';
import { UserProvider } from './contexts/UserContext';
import { SidebarProvider } from './contexts/SidebarContext';

function App() {
  return (
    <UserProvider>
      <SidebarProvider>
        <AppRouter />
      </SidebarProvider>
    </UserProvider>
  );
}

export default App;

