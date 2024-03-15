import React from 'react';
import { Sidebar } from './Sidebar';

import '../styles/Sidebar.css'



export const Main: React.FC = () => {
  return (
    <div>
      <Sidebar />
      <div className="main-content">
        <h1>Добро пожаловать, Andy_Panda!</h1>
      </div>
    </div>
  );
};
