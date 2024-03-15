import React, { useState } from 'react';
import '../styles/Sidebar.css';

interface SidebarProps {
  items: string[]; // Массив элементов боковой панели
}

export const Sidebar: React.FC = () => {
  const [selectedItem, setSelectedItem] = useState<string | null>(null);

  const handleItemClick = (item: string) => {
    setSelectedItem(item);
    // Здесь можно добавить дополнительную логику при выборе элемента
  };

  return (
    <div className="sidebar">
      <p>Admin</p>
      <ul className='ull'>
        {['Главная', 'Новости', 'Расписание', "Информация"].map((item, index) => (
          <li
            key={index}
            className={selectedItem === item ? 'selected' : ''}
            onClick={() => handleItemClick(item)}
          >
            {item}
          </li>
        ))}
      </ul>
    </div>
  );
};

