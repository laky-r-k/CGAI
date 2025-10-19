// src/App.js
import React from 'react';
import './App.css';
import Login from './components/Login'; // 1. Import your component

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>My Awesome App</h1>
        <Login /> {/* 2. Add the component's tag here */}
      </header>
    </div>
  );
}

export default App;