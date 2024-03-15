import React, { useState } from 'react';
import { NavLink } from 'react-router-dom';
import '../styles/Sidebar.css';

export const Sidebar: React.FC = () => {
  const [selectedItem, setSelectedItem] = useState<string | null>(null);

  const handleItemClick = (item: string) => {
    setSelectedItem(item);
  };

  return (
    <div className="sidebar">
      <p>Admin</p>
      <ul>
        {['Главная', 'Новости', 'Расписание', 'Информация'].map((item, index) => (
          <li
            key={index}
            className={selectedItem === item ? 'selected' : ''}
            onClick={() => handleItemClick(item)}
          >
            <NavLink to={item === 'Информация' ? '/info' : '/'}>{item}</NavLink>
          </li>
        ))}
      </ul>
    </div>
  );
};
