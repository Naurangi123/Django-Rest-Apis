import React, { Suspense, lazy, useState, useEffect } from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import {ACCESS_TOKEN} from './constants'
import "./styles/base.css";
import "./styles/login.css";

// Lazily load components
const Register = lazy(() => import('./pages/Register'));
const Login = lazy(() => import('./pages/Login'));
const NotFound = lazy(() => import('./pages/NotFound'));
const ProtectedRoute = lazy(() => import('./components/ProtectedRoute'));
const MovieList = lazy(() => import('./components/MovieList'));
const CreateStream = lazy(() => import('./components/CreateStream'));
const WatchList = lazy(() => import('./components/WatchList'));
const Profile = lazy(() => import('./components/Profile'));
const WatchDetail = lazy(() => import('./components/WatchDetail'));
const Navbar = lazy(() => import('./Layout/Navbar')); 


const Logout = () => {
  sessionStorage.clear();
  return <Navigate to="/login" />;
};

const RegisterAndLogout = () => {
  sessionStorage.clear();
  return <Register />;
};

const routes = [
  { path: "/", element: <ProtectedRoute><MovieList /></ProtectedRoute> },
  { path: "/watch", element: <ProtectedRoute><WatchList /></ProtectedRoute> },
  { path: "/watch/:id", element: <ProtectedRoute><WatchDetail /></ProtectedRoute> },
  { path: "/home", element: <ProtectedRoute><CreateStream /></ProtectedRoute> },
  { path: "/profile", element: <ProtectedRoute><Profile /></ProtectedRoute> },
  { path: "/login", element: <Login /> },
  { path: "/register", element: <RegisterAndLogout /> },
  { path: "/logout", element: <Logout /> },
  { path: "*", element: <NotFound /> },
];

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);


  useEffect(() => {
    const token = sessionStorage.getItem(ACCESS_TOKEN);
    if (token) {
      setIsAuthenticated(true);
    }
  }, []);

  const loggedInUser = (status) => {
    setIsAuthenticated(status);
  };

  const handleLogout = () => {
    sessionStorage.removeItem(ACCESS_TOKEN);
    setIsAuthenticated(false);
  };

  return (
    <BrowserRouter>
      <Suspense fallback={<div>Loading...</div>}>
        <Navbar isAuthenticated={isAuthenticated} handleLogout={handleLogout} loggedInUser={loggedInUser} />
        <Routes>
          {routes.map((route, idx) => (
            <Route key={idx} path={route.path} element={route.element} />
          ))}
        </Routes>
      </Suspense>
    </BrowserRouter>
  );
}

export default App;


// import Movies from './components/Movies'
// import WatchLists from './components/WatchLists';

// import React from 'react'
// function App() {
//   return (
//     <>
//     {/* <Movies/> */}
//     <WatchLists/>
//     </>
//   );
// }

// export default App;
