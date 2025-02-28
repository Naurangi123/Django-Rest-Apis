import React, { useState } from 'react';
import { useNavigate} from 'react-router-dom';
import api from '../services/api';
import { ACCESS_TOKEN,REFRESH_TOKEN } from '../constants';
import Loader from '../components/Loader';
import '../styles/login.css';

const Login = () => {
  const[username,setUsername]=useState("")
  const[password,setPassword]=useState("")
  const[loading,setloading]=useState(false)
  const navigate=useNavigate()


  const handleSubmit=async(e)=>{
    setloading(true)
    e.preventDefault()
    try {
        const res =await api.post("/account/api/token/",{username,password})
        if(res.status===200){
            sessionStorage.setItem(ACCESS_TOKEN,res.data.access)
            sessionStorage.setItem(REFRESH_TOKEN,res.data.refresh)
            navigate('/')
        }else{
            navigate('/login')
        }
    } catch (error) {
        alert(error.message)
    }
    finally{
        setloading(false)
    }
  }
  return (
    <div className='login'>
      <h1>Login</h1>
      <form onSubmit={handleSubmit} className='form-container'>
          <input 
              type="text" 
              value={username} 
              onChange={(e)=>setUsername(e.target.value)}
              placeholder='Username' 
          />
          <input 
              type="password" 
              value={password} 
              onChange={(e)=>setPassword(e.target.value)}
              placeholder='Password'  
          />
          {loading && <Loader/>}
          <button type='submit'>Login</button>
      </form>
    </div>
  )
}

export default Login;