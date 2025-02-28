import { RiMovie2AiFill } from "react-icons/ri";
import React from 'react';
import { Link } from 'react-router-dom';
import '../styles/nav.css';

export default function Navbar({ isAuthenticated, loggedInUser, handleLogout }) {
  return (
    <nav className="navbar">
      <div className="navbar-left">
        <Link to="/" className="logo">
          <RiMovie2AiFill size={25} color="white" />
        </Link>
      </div>
      <div>
        {isAuthenticated ? (
          <>
            <div className="navbar-right">
              <div>
                <Link to="/" className="navbar-item">Home</Link>
              </div>
              <div className="dropdown">
                <button className="dropdown-btn">Profile</button>
                <div className="dropdown-content">
                  <Link to="/profile" className="dropdown-item">My Profile</Link>
                  <Link to="/watch" className="dropdown-item">Watch List</Link>
                  <Link to="/reviews" className="dropdown-item">Reviews</Link>
                  <button className="dropdown-item" onClick={handleLogout}>Logout</button>
                </div>
              </div>
            </div>
          </>
        ) : (
          <>
            <Link to="/login" className="navbar-item">Login</Link>
            <Link to="/register" className="navbar-item">Register</Link>
          </>
        )}
      </div>
    </nav>
  );
};


