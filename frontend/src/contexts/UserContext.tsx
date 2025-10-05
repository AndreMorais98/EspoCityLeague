import React, { createContext, useContext, useState, useEffect, ReactNode } from 'react';
import { getAuthToken, User } from '../services/auth';
import { apiService } from '../services/api';

interface UserContextType {
  user: User | null;
  setUser: (user: User | null) => void;
  isLoading: boolean;
  updateUserScore: (newScore: number) => void;
}

const UserContext = createContext<UserContextType | undefined>(undefined);

export const useUser = () => {
  const context = useContext(UserContext);
  if (context === undefined) {
    throw new Error('useUser must be used within a UserProvider');
  }
  return context;
};

interface UserProviderProps {
  children: ReactNode;
}

export const UserProvider: React.FC<UserProviderProps> = ({ children }) => {
  const [user, setUser] = useState<User | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [hasFetched, setHasFetched] = useState(false);

  useEffect(() => {
    // Prevent duplicate calls if we've already fetched
    if (hasFetched) {
      return;
    }

    const fetchUserInfo = async () => {
      const token = getAuthToken();
      if (!token) {
        setIsLoading(false);
        setHasFetched(true);
        return;
      }

      try {
        console.log('Fetching user info...');
        const userData = await apiService.getCurrentUser();
        console.log('User data received:', userData);
        setUser(userData);
      } catch (error) {
        console.error('Failed to fetch user info:', error);
        setUser(null);
      } finally {
        setIsLoading(false);
        setHasFetched(true);
      }
    };

    fetchUserInfo();
  }, [hasFetched]);

  const updateUserScore = (newScore: number) => {
    if (user) {
      setUser({ ...user, score: newScore });
    }
  };

  const value: UserContextType = {
    user,
    setUser,
    isLoading,
    updateUserScore,
  };

  return (
    <UserContext.Provider value={value}>
      {children}
    </UserContext.Provider>
  );
};
