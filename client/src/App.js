import {BrowserRouter,Routes,Route,Navigate} from 'react-router-dom'
import Register from './pages/Register'
import Login from './pages/Login'
import NotFound from './pages/NotFound'
import ProtectedRoute from './components/ProtectedRoute'
import MovieList from './components/MovieList'
import CreateStream from './components/CreateStream'
import WatchList from './components/WatchList'
import WatchDetail from './components/WatchDetail'


function Logout(){
  localStorage.clear()
  return <Navigate to="/login" />
}

function RegisterAndLogout() {
  localStorage.clear()
  return <Register />
}


function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route 
        path="/" 
        element={
          <ProtectedRoute>
            <MovieList />
          </ProtectedRoute>
        } 
        />
        <Route path="/watch" element={<WatchList />} />
        <Route path="/watch/:id" element={<WatchDetail />} />
        <Route path="/home" element={<CreateStream />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<RegisterAndLogout />} />
        <Route path="/logout" element={<Logout />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;