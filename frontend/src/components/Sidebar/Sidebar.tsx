import React from 'react';
import { NavLink } from 'react-router-dom';
import './Sidebar.scss';

export default function Sidebar() {
  return (
    <aside className="sidebar">
      <div className="sidebar__brand">EspoCityLeague</div>
      <nav className="sidebar__nav">
        <NavLink
          to="/leaderboard"
          className={({ isActive }) => `sidebar__item ${isActive ? 'active' : ''}`}
        >
          Leaderboard
        </NavLink>
        <NavLink
          to="/games"
          className={({ isActive }) => `sidebar__item ${isActive ? 'active' : ''}`}
        >
          Games
        </NavLink>
        <NavLink
          to="/rules"
          className={({ isActive }) => `sidebar__item ${isActive ? 'active' : ''}`}
        >
          Rules
        </NavLink>
        <NavLink
          to="/others-bets"
          className={({ isActive }) => `sidebar__item ${isActive ? 'active' : ''}`}
        >
          Other's Bets
        </NavLink>
      </nav>
    </aside>
  );
}
