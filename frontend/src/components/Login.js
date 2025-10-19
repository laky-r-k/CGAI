// src/components/Login.js
import React, { useState } from 'react';
import { auth } from '../firebase'; // Import auth from your config
import { signInWithEmailAndPassword } from 'firebase/auth';
import axios from 'axios'; // For making API calls

function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(null);
  const [userData, setUserData] = useState(null);

  // This function calls your Django API
  const callDjangoApi = async (token) => {
    try {
      // Make sure to use your Django server's URL
      const response = await axios.get('http://127.0.0.1:8000/api/users/me/', {
        headers: {
          // This is the critical part
          'Authorization': `Bearer ${token}`
        }
      });
      
      console.log('Success! Django API response:', response.data);
      setUserData(response.data); // Save the user data from your API
      setError(null);

    } catch (apiError) {
      console.error('Django API Error:', apiError.response.data);
      setError(apiError.response.data.detail || 'Failed to fetch user data.');
      setUserData(null);
    }
  };

  const handleLogin = async (e) => {
    e.preventDefault();
    setError(null);

    try {
      // 1. Sign in to Firebase
      const userCredential = await signInWithEmailAndPassword(auth, email, password);
      console.log('Firebase login successful:', userCredential.user.email);
      
      // 2. Get the ID Token 🔥
      const token = await userCredential.user.getIdToken();
      console.log('Got Firebase Token:', token);

      // 3. Call your Django API with the token
      await callDjangoApi(token);

    } catch (firebaseError) {
      console.error('Firebase Login Error:', firebaseError);
      setError(firebaseError.message);
    }
  };

  return (
    <div>
      <form onSubmit={handleLogin}>
        <h3>Login</h3>
        <input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="Email"
        />
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          placeholder="Password"
        />
        <button type="submit">Log In</button>
      </form>
      
      {error && <p style={{ color: 'red' }}>Error: {error}</p>}
      
      {userData && (
        <div style={{ marginTop: '20px' }}>
          <h4>Successfully fetched from Django:</h4>
          <pre>{JSON.stringify(userData, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default Login;