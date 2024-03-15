import React, { useState } from 'react';
import { Sidebar } from './Sidebar';
import "../styles/InfoList.css";
import { info } from "../testDB/testsdb";

export const InfoList: React.FC = () => {
  return (
    <div>
      <Sidebar/>
      {Object.values(info).map((item, index) => (
        <div key={index} className={`info-item ${item.prioritet < 5 ? 'disabled' : ''}`}>
          <h3>{item.title}</h3>
          <p>Приоритет: {item.prioritet}</p>
          <p>{item.inf}</p>
        </div>
      ))}
    </div>
  );
};

