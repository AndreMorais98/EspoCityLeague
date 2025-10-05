import React from 'react';
import { Outlet } from 'react-router'; 
import Sidebar from '../../components/Sidebar/Sidebar';
import './Home.scss';

export default function Home() {
  return (
    <div className="layout">
      <Sidebar />
      <main className="content">
        <Outlet />
      </main>
    </div>
  );
}
