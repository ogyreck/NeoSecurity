import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import { Login } from './components/Login';
import { Main } from './components/Main';
import { InfoList } from './components/InfoList';
import { Sidebar } from './components/Sidebar';

const App: React.FC = () => {
  const [loggedIn, setLoggedIn] = useState(false);

  const handleLogin = () => {
    setLoggedIn(true);
  };

  return (
    <Router>
      <div>
        {loggedIn && <Sidebar />}
        <Routes>
          <Route path="/" element={loggedIn ? <Main /> : <Login onLogin={handleLogin} />} />
          <Route path="/info" element={<InfoList />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
