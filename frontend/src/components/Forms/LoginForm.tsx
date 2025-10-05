import React, { useState } from 'react';
import { useNavigate } from 'react-router'; 
import { login, setAuthToken } from '../../services/auth';
import { useUser } from '../../contexts/UserContext';

export default function LoginForm() {
  const [username, setUsername] = useState<string>('');
  const [password, setPassword] = useState<string>('');
  const [isSubmitting, setIsSubmitting] = useState<boolean>(false);
  const [error, setError] = useState<string>('');
  const navigate = useNavigate();
  const { setUser } = useUser();

  const handleSubmit = async (e: any) => {
    e.preventDefault();
    setError('');
    setIsSubmitting(true);
    
    try {
      const response = await login({ username, password });
      console.log(response);
      setAuthToken(response.access_token);
      // Set user in context from API response
      setUser(response.user);
      navigate('/leaderboard');
    } catch (err: any) {
      setError(err?.message || 'Failed to sign in');
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <form className="login-form" onSubmit={handleSubmit}>
      {error && <div className="login-error">{error}</div>}
      
      <div className="login-form-group">
        <label className="login-label" htmlFor="username">
          Username
        </label>
        <input
          id="username"
          type="text"
          className="login-input"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          placeholder="Enter your username"
          required
        />
      </div>

      <div className="login-form-group">
        <label className="login-label" htmlFor="password">
          Password
        </label>
        <input
          id="password"
          type="password"
          className="login-input"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          placeholder="Enter your password"
          required
        />
      </div>

      <button 
        className="login-button" 
        type="submit" 
        disabled={isSubmitting}
      >
        {isSubmitting ? 'Signing In...' : 'Sign In'}
      </button>
      
      <div className="login-footer">
        <a href="#" onClick={(e) => e.preventDefault()}>
          Forgot your password?
        </a>
      </div>
    </form>
  );
}
