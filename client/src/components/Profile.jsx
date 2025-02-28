import React, { useState, useEffect } from 'react';
import { ACCESS_TOKEN } from '../constants';
import api from '../services/api.js';
import '../styles/userProfile.css';

const UserProfile = () => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const getUser=async()=>{
      const token=sessionStorage.getItem(ACCESS_TOKEN)
      if(!token){
        return null;
      }
      try{
        const response=await api.get('/account/api/user/',{
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        setUser(response.data);
        setLoading(false)
      }
      catch(error){
        setError(error.message);
      }
    }
    getUser();
  },[])

  if (loading) {
    return <div className="loading">Loading...</div>;
  }

  if (error) {
    return <div className="error-message">Error: {error}</div>;
  }

  return (
    <div className="user-profile-container">
      <h2>User Profile</h2>

      {user ? (
        <div className="profile-details">
          <p><strong>Name:</strong> {user.username}</p>
          <p><strong>Email:</strong> {user.email}</p>
        </div>
      ) : (
        <p>No user data available.</p>
      )}
    </div>
  );
};

export default UserProfile;
