import React from 'react';
import { Outlet } from 'react-router'; 
import Sidebar from '../../components/Sidebar/Sidebar';
import { useSidebar } from '../../contexts/SidebarContext';
import './Home.scss';

export default function Home() {
  const { isMobileOpen, toggleMobileSidebar } = useSidebar();
  
  return (
    <div className="layout">
      <Sidebar />
      <button 
        className="mobile-menu-toggle"
        onClick={toggleMobileSidebar}
        title="Toggle menu"
      >
        ☰
      </button>
      <div 
        className={`mobile-overlay ${isMobileOpen ? 'active' : ''}`}
        onClick={toggleMobileSidebar}
      />
      <main className="content">
        <Outlet />
      </main>
    </div>
  );
}
