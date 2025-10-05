import React, { useState } from 'react';
import { useUser } from '../../contexts/UserContext';
import { apiService } from '../../services/api';
import './UserDetails.scss';

interface UpdateFormData {
  username: string;
  phone: string;
  password: string;
  confirmPassword: string;
}

export default function UserDetails() {
  const { user, setUser } = useUser();
  const [isEditing, setIsEditing] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string>('');
  const [success, setSuccess] = useState<string>('');
  
  const [formData, setFormData] = useState<UpdateFormData>({
    username: user?.username || '',
    phone: user?.phone || '',
    password: '',
    confirmPassword: '',
  });

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    setSuccess('');
    
    // Validation
    if (formData.password && formData.password !== formData.confirmPassword) {
      setError('Passwords do not match');
      return;
    }
    
    if (formData.password && formData.password.length < 6) {
      setError('Password must be at least 6 characters long');
      return;
    }

    setIsLoading(true);

    try {
      const updateData: { username?: string; phone?: string; password?: string } = {};
      
      if (formData.username !== user?.username) {
        updateData.username = formData.username;
      }
      
      if (formData.phone !== user?.phone) {
        updateData.phone = formData.phone;
      }
      
      if (formData.password) {
        updateData.password = formData.password;
      }

      const updatedUser = await apiService.updateCurrentUser(updateData);
      setUser(updatedUser);
      setSuccess('Profile updated successfully!');
      setIsEditing(false);
      
      // Clear password fields
      setFormData(prev => ({
        ...prev,
        password: '',
        confirmPassword: '',
      }));
    } catch (err: any) {
      setError(err.message || 'Failed to update profile');
    } finally {
      setIsLoading(false);
    }
  };

  const handleCancel = () => {
    setFormData({
      username: user?.username || '',
      phone: user?.phone || '',
      password: '',
      confirmPassword: '',
    });
    setError('');
    setSuccess('');
    setIsEditing(false);
  };

  if (!user) {
    return <div className="user-details">Loading...</div>;
  }

  return (
    <div className="user-details">
      <div className="user-details__header">
        <h1>User Details</h1>
        {!isEditing && (
          <button 
            className="btn btn--primary"
            onClick={() => setIsEditing(true)}
          >
            Edit Profile
          </button>
        )}
      </div>

      {success && (
        <div className="alert alert--success">
          {success}
        </div>
      )}

      {error && (
        <div className="alert alert--error">
          {error}
        </div>
      )}

      <div className="user-details__content">
        <div className="user-info">
          <div className="user-info__avatar">
            <div className="avatar">
              {user.username.charAt(0).toUpperCase()}
            </div>
          </div>
          
          <div className="user-info__details">
            <h2 style={{ textTransform: 'capitalize' }}>{user.username}</h2>
            <p className="user-role">
              {user.is_superuser ? 'Administrator' : 'Player'}
            </p>
            <p className="user-score">Score: {user.score}</p>
          </div>
        </div>

        <form className="user-form" onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="username">Username</label>
            <input
              type="text"
              id="username"
              name="username"
              value={formData.username}
              onChange={handleInputChange}
              disabled={!isEditing}
              required
            />
          </div>

          <div className="form-group">
            <label htmlFor="phone">Phone Number</label>
            <input
              type="tel"
              id="phone"
              name="phone"
              value={formData.phone}
              onChange={handleInputChange}
              disabled={!isEditing}
              required
            />
          </div>

          <div className="form-group">
            <label htmlFor="password">New Password (optional)</label>
            <input
              type="password"
              id="password"
              name="password"
              value={formData.password}
              onChange={handleInputChange}
              disabled={!isEditing}
              placeholder="Leave blank to keep current password"
            />
          </div>

          {formData.password && (
            <div className="form-group">
              <label htmlFor="confirmPassword">Confirm New Password</label>
              <input
                type="password"
                id="confirmPassword"
                name="confirmPassword"
                value={formData.confirmPassword}
                onChange={handleInputChange}
                disabled={!isEditing}
              />
            </div>
          )}

          {isEditing && (
            <div className="form-actions">
              <button 
                type="button" 
                className="btn btn--secondary"
                onClick={handleCancel}
                disabled={isLoading}
              >
                Cancel
              </button>
              <button 
                type="submit" 
                className="btn btn--primary"
                disabled={isLoading}
              >
                {isLoading ? 'Saving...' : 'Save Changes'}
              </button>
            </div>
          )}
        </form>
      </div>
    </div>
  );
}
