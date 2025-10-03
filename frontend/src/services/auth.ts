interface LoginCredentials {
  email: string;
  password: string;
}

interface AuthResponse {
  token: string;
  user: {
    email: string;
  };
}

export async function login({ email, password }: LoginCredentials): Promise<AuthResponse> {
  await new Promise(resolve => setTimeout(resolve, 500));
  
  if (!email || !password) {
    throw new Error('Email and password are required');
  }
  
  if (email === 'admin@example.com' && password === 'password') {
    return { 
      token: 'fake-jwt-token', 
      user: { email } 
    };
  }
  
  throw new Error('Invalid credentials');
}

export async function logout(): Promise<void> {
  // TODO: Implement logout functionality
  await new Promise(resolve => setTimeout(resolve, 100));
}

export function getAuthToken(): string | null {
  // TODO: Get token from localStorage or secure storage
  return localStorage.getItem('authToken');
}

export function setAuthToken(token: string): void {
  // TODO: Store token securely
  localStorage.setItem('authToken', token);
}
