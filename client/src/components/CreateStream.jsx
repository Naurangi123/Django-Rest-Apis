import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';  
import api from '../services/api';


const StreamForm = () => {
  const [name, setName] = useState("");
  const [about, setAbout] = useState("");
  const [website, setWebsite] = useState("");
  const navigate = useNavigate();  
  const createStream = async (e) => {
    e.preventDefault();

    try {
      const res = await api.post("/watch/streams/", { name, about, website });

      if (res.status === 200) {
        alert("Stream created successfully");
        setName("");
        setAbout("");
        setWebsite("");
        navigate("/", { replace: true })
      } else {
        alert("Error creating stream");
      }
    } catch (error) {
      alert(`Error: ${error.message}`);
    }
  }
  return (
    <div>
      <h1>Create a Stream</h1>
      <form onSubmit={createStream}>
      <input
        type="text"
        placeholder="Stream Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <textarea
        placeholder="About the Stream"
        value={about}
        onChange={(e) => setAbout(e.target.value)}
      />
      <input
        type="url"
        placeholder="Website"
        value={website}
        onChange={(e) => setWebsite(e.target.value)}
      />
      <button type="submit">Create Stream</button>
    </form>
    </div>
  );
}
export default StreamForm;
