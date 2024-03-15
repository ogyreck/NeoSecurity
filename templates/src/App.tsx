import React, { useState } from 'react';
import { Login } from './Login';
import { Main } from './Main';
import { Sidebar } from './components/Sidebar';

const App: React.FC = () => {
  const [loggedIn, setLoggedIn] = useState(false);

  const handleLogin = () => {
    setLoggedIn(true);
  };

  return (
    <div>
      {loggedIn ? (
        <div>
          <Main />
        </div>
      ) : (
        <Login onLogin={handleLogin} />
      )}
    </div>
  );
};

export default App;
