import React, { useState } from 'react';
import loginImage1 from '../images/login-1.png';
import loginImage2 from '../images/login-2.png';
import '../styles/Login.css';

const Person = {
  login: 'gaziz@a',
  password: '123'
}

type LoginProps = {
  onLogin: () => void; // тип пропса onLogin
}

export const Login: React.FC<LoginProps> = ({ onLogin }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loggedIn, setLoggedIn] = useState(false);

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (email === Person.login && password === Person.password) {
      setLoggedIn(true);
      onLogin(); // вызываем функцию onLogin при успешной аутентификации
    }
  };

  return (
    <div className="login-container">
      <img src={loginImage1} alt="" className='login-img-1'/>
      <img src={loginImage2} alt="" className='login-img-2'/>
      <form className="login-form" onSubmit={handleSubmit}>
        <h2 className="login-header">Авторизация</h2>
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          className="login-input"
          required
        />
        <input
          type="password"
          placeholder="Пароль"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="login-input"
          required
        />
        <button type="submit" className="login-button">
          Войти
        </button>
      </form>
      {loggedIn && <p>Вы успешно вошли в систему!</p>}
    </div>
  );
};
