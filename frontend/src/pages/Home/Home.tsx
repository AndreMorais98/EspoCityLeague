import React from 'react';
import { Outlet } from 'react-router'; 
import Sidebar from '../../components/Sidebar/Sidebar';
import { useSidebar } from '../../contexts/SidebarContext';
import './Home.scss';

export default function Home() {
  const { isCollapsed } = useSidebar();
  
  return (
    <div className="layout">
      <Sidebar />
      <main className={`content ${isCollapsed ? 'sidebar-collapsed' : ''}`}>
        <Outlet />
      </main>
    </div>
  );
}
