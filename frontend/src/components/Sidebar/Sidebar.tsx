import React from 'react';
import { NavLink, useNavigate } from 'react-router'; 
import { logout } from '../../services/auth';
import { useUser } from '../../contexts/UserContext';
import { useSidebar } from '../../contexts/SidebarContext';
import './Sidebar.scss';

export default function Sidebar() {
  const navigate = useNavigate();
  const { user, setUser } = useUser();
  const { isCollapsed, toggleSidebar, isMobileOpen } = useSidebar();

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
    <aside className={`sidebar ${isCollapsed ? 'collapsed' : ''} ${isMobileOpen ? 'mobile-open' : ''}`}>
      <button 
        className="sidebar__toggle"
        onClick={toggleSidebar}
        title={isCollapsed ? 'Expand sidebar' : 'Collapse sidebar'}
      >
        {isCollapsed ? '>' : '<'}
      </button>
      
      <div className="sidebar__brand">
        <img className="symbol-bg" src="/images/symbol.png" alt="UEFA symbol background"/>
        {!isCollapsed && <span className="brand-text">Espo City League</span>}
      </div>
      
      <nav className="sidebar__nav">
        <NavLink
          to="/leaderboard"
          className={({ isActive }) => `sidebar__item ${isActive ? 'active' : ''}`}
          title={isCollapsed ? 'Rankings' : ''}
        >
          <div className="item__icon">🏆</div>
          {!isCollapsed && <span className="item__text">Rankings</span>}
        </NavLink>
        <NavLink
          to="/games"
          className={({ isActive }) => `sidebar__item ${isActive ? 'active' : ''}`}
          title={isCollapsed ? 'My Predictions' : ''}
        >
          <div className="item__icon">⚽</div>
          {!isCollapsed && <span className="item__text">My Predictions</span>}
        </NavLink>
        <NavLink
          to="/others-bets"
          className={({ isActive }) => `sidebar__item ${isActive ? 'active' : ''}`}
          title={isCollapsed ? 'Community Predictions' : ''}
        >
          <div className="item__icon">👥</div>
          {!isCollapsed && <span className="item__text">Community Predictions</span>}
        </NavLink>
        <NavLink
          to="/rules"
          className={({ isActive }) => `sidebar__item ${isActive ? 'active' : ''}`}
          title={isCollapsed ? 'Game Rules' : ''}
        >
          <div className="item__icon">📋</div>
          {!isCollapsed && <span className="item__text">Game Rules</span>}
        </NavLink>
        <NavLink
          to="/profile"
          className={({ isActive }) => `sidebar__item ${isActive ? 'active' : ''}`}
          title={isCollapsed ? 'My Profile' : ''}
        >
          <div className="item__icon">⚙️</div>
          {!isCollapsed && <span className="item__text">My Profile</span>}
        </NavLink>
        {user?.is_superuser && (
          <NavLink
            to="/admin-matches"
            className={({ isActive }) => `sidebar__item ${isActive ? 'active' : ''}`}
            title={isCollapsed ? 'Manage Matches' : ''}
          >
            <div className="item__icon">⚽</div>
            {!isCollapsed && <span className="item__text">Manage Matches</span>}
          </NavLink>
        )}
        {user?.is_superuser && (
          <NavLink
            to="/create-match"
            className={({ isActive }) => `sidebar__item ${isActive ? 'active' : ''}`}
            title={isCollapsed ? 'Create Match' : ''}
          >
            <div className="item__icon">➕</div>
            {!isCollapsed && <span className="item__text">Create Match</span>}
          </NavLink>
        )}
      </nav>
      
      <div className="sidebar__footer">
        <div className="user__section">
          <div className="user__avatar">
            {user ? user.username.charAt(0).toUpperCase() : 'U'}
          </div>
          {!isCollapsed && (
            <div className="user__info">
              <div className="user__name">{user ? user.username : 'User'}</div>
              <div className="user__role">
                {user?.is_superuser ? 'Administrator' : 'Player'}
              </div>
            </div>
          )}
        </div>
        
        <button 
          onClick={handleLogout}
          className="sidebar__logout"
          title={isCollapsed ? 'Logout' : ''}
        >
          {isCollapsed ? '🚪' : 'Logout'}
        </button>
      </div>
    </aside>
  );
}
