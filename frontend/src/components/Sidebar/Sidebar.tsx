import React from 'react';
import { NavLink, useNavigate } from 'react-router'; 
import { logout } from '../../services/auth';
import { useUser } from '../../contexts/UserContext';
import './Sidebar.scss';

export default function Sidebar() {
  const navigate = useNavigate();
  const { user, setUser } = useUser();

  const handleLogout = async () => {
    try {
      await logout();
      setUser(null);
      navigate('/login');
    } catch (error) {
      console.error('Logout failed:', error);
    }
  };

  return (
    <aside className="sidebar">
      <div className="sidebar__brand">
        <img className="symbol-bg" src="/images/symbol.png" alt="UEFA symbol background" width={48} height={48}/>
      </div>
      
      <nav className="sidebar__nav">
        <NavLink
          to="/leaderboard"
          className={({ isActive }) => `sidebar__item ${isActive ? 'active' : ''}`}
        >
          <div className="item__icon">🏆</div>
          Rankings
        </NavLink>
        <NavLink
          to="/games"
          className={({ isActive }) => `sidebar__item ${isActive ? 'active' : ''}`}
        >
          <div className="item__icon">⚽</div>
          My Predictions
        </NavLink>
        <NavLink
          to="/others-bets"
          className={({ isActive }) => `sidebar__item ${isActive ? 'active' : ''}`}
        >
          <div className="item__icon">👥</div>
          Community Predictions
        </NavLink>
        <NavLink
          to="/rules"
          className={({ isActive }) => `sidebar__item ${isActive ? 'active' : ''}`}
        >
          <div className="item__icon">📋</div>
          Game Rules
        </NavLink>
        <NavLink
          to="/profile"
          className={({ isActive }) => `sidebar__item ${isActive ? 'active' : ''}`}
        >
          <div className="item__icon">⚙️</div>
          My Profile
        </NavLink>
      </nav>
      
      <div className="sidebar__footer">
        <div className="user__section">
          <div className="user__avatar">
            {user ? user.username.charAt(0).toUpperCase() : 'U'}
          </div>
          <div className="user__info">
            <div className="user__name">{user ? user.username : 'User'}</div>
            <div className="user__role">
              {user?.is_superuser ? 'Administrator' : 'Player'}
            </div>
          </div>
        </div>
        
        <button 
          onClick={handleLogout}
          className="sidebar__logout"
        >
          Logout
        </button>
      </div>
    </aside>
  );
}
