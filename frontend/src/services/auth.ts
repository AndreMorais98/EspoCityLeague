interface LoginCredentials {
  username: string;
  password: string;
}

export interface User {
  id: number;
  username: string;
  phone: string;
  score: number;
  is_active: boolean;
  is_superuser: boolean;
}

interface AuthResponse {
  access_token: string;
  token_type: string;
  user: User;
}

export async function login({ username, password }: LoginCredentials): Promise<AuthResponse> {
  const response = await fetch('http://localhost:8000/auth/login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ username, password }),
  });
  
  if (!response.ok) {
    throw new Error('Invalid credentials');
  }
  
  return response.json();
}

export async function logout(): Promise<void> {
  localStorage.removeItem('authToken');
}

export function getAuthToken(): string | null {
  return localStorage.getItem('authToken');
}

export function setAuthToken(token: string): void {
  localStorage.setItem('authToken', token);
}

export function isAuthenticated(): boolean {
  return getAuthToken() !== null;
}

export async function getCurrentUser(): Promise<User> {
  const token = getAuthToken();
  if (!token) {
    throw new Error('No authentication token found');
  }

  const response = await fetch('http://localhost:8000/auth/me', {
    headers: {
      'Authorization': `Bearer ${token}`,
    },
  });

  if (!response.ok) {
    throw new Error('Failed to fetch user info');
  }

  return response.json();
}
