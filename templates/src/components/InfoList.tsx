import React, { useState } from 'react';
import { Sidebar } from './Sidebar';
import "../styles/InfoList.css";
import { info } from "../testDB/testsdb";

export const InfoList: React.FC = () => {
  return (
    <div>
      <Sidebar/>
      <div className="space">
        {Object.values(info).map((item, index) => (
          <div key={index} className={`info-item ${item.prioritet < 5 ? 'disabled' : ''}`}>
            <h3>{item.title}</h3>
          </div>
        ))}
      </div>
    </div>
  );
};

