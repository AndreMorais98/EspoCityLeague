import React, { useEffect } from 'react';
import { NavLink, useNavigate } from 'react-router'; 
import { logout } from '../../services/auth';
import { useUser } from '../../contexts/UserContext';
import { useSidebar } from '../../contexts/SidebarContext';
import './Sidebar.scss';

export default function Sidebar() {
  const navigate = useNavigate();
  const { user, setUser } = useUser();
  const { isMobileOpen, toggleMobileSidebar } = useSidebar();

  // Manage body scroll when mobile sidebar is open
  useEffect(() => {
    if (isMobileOpen) {
      document.body.classList.add('sidebar-mobile-open');
    } else {
      document.body.classList.remove('sidebar-mobile-open');
    }

    // Cleanup on unmount
    return () => {
      document.body.classList.remove('sidebar-mobile-open');
    };
  }, [isMobileOpen]);

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
    <aside className={`sidebar ${isMobileOpen ? 'mobile-open' : ''}`}>
      <button 
        className="sidebar__toggle"
        onClick={toggleMobileSidebar}
        title="Toggle menu"
      >
        {isMobileOpen ? '✕' : '☰'}
      </button>
      
      <div className="sidebar__brand">
        <img className="symbol-bg" src="/images/symbol.png" alt="UEFA symbol background"/>
        <span className="brand-text">Espo City League</span>
      </div>
      
      <nav className="sidebar__nav">
        <NavLink
          to="/leaderboard"
          className={({ isActive }) => `sidebar__item ${isActive ? 'active' : ''}`}
        >
          <div className="item__icon">🏆</div>
          <span className="item__text">Rankings</span>
        </NavLink>
        <NavLink
          to="/games"
          className={({ isActive }) => `sidebar__item ${isActive ? 'active' : ''}`}
        >
          <div className="item__icon">⚽</div>
          <span className="item__text">My Predictions</span>
        </NavLink>
        <NavLink
          to="/others-bets"
          className={({ isActive }) => `sidebar__item ${isActive ? 'active' : ''}`}
        >
          <div className="item__icon">👥</div>
          <span className="item__text">Community Predictions</span>
        </NavLink>
        <NavLink
          to="/rules"
          className={({ isActive }) => `sidebar__item ${isActive ? 'active' : ''}`}
        >
          <div className="item__icon">📋</div>
          <span className="item__text">Game Rules</span>
        </NavLink>
        <NavLink
          to="/profile"
          className={({ isActive }) => `sidebar__item ${isActive ? 'active' : ''}`}
        >
          <div className="item__icon">⚙️</div>
          <span className="item__text">My Profile</span>
        </NavLink>
        {user?.is_superuser && (
          <NavLink
            to="/admin-matches"
            className={({ isActive }) => `sidebar__item ${isActive ? 'active' : ''}`}
          >
            <div className="item__icon">⚽</div>
            <span className="item__text">Manage Matches</span>
          </NavLink>
        )}
        {user?.is_superuser && (
          <NavLink
            to="/create-match"
            className={({ isActive }) => `sidebar__item ${isActive ? 'active' : ''}`}
          >
            <div className="item__icon">➕</div>
            <span className="item__text">Create Match</span>
          </NavLink>
        )}
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
