import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import '../styles/movies.css'
import api from '../services/api';

const MovieList = () => {
  const [streams, setStream] = useState([]); 
  const [loading, setLoading] = useState(true); 
  const [error, setError] = useState(null); 
  const navigate = useNavigate();

  const fetchStreams = async () => {
    try {
      const response = await api.get('/watch/streams');
      setStream(response.data);
      setLoading(false);
    } catch (error) {
      setError(error.message);
    }
  };

  function handleMovieClick(){
    navigate('/watch/');
  }
  
  useEffect(() => {
    fetchStreams();
  }, []);

  if (loading) {
    return <div>Loading...</div>; 
  }

  if (error) {
    return <div>Error: {error}</div>; 
  }

  return (
    <div className="stream-container">
      {streams.map(stream => (
        <div className="stream-details" key={stream.id}>
          <hr className="divider" />
          <h1 className="stream-title">{stream.name}</h1>
          <p className="stream-description">{stream.about}</p>
  
          <h3 className="watchlist-heading">Watchlist:</h3>
          {stream.watchlist.length > 0 ? (
            stream.watchlist.map(item => (
              <div key={item.id} className="watchlist-item">
                <p className="item-title" onClick={()=>{handleMovieClick()}}><strong>Title:</strong> {item.title}</p>
                {item.reviews && item.reviews.length > 0 ? (
                  item.reviews.map(review => (
                    <div key={review.id} className="review-item">
                      <p className="review-description"><strong>Review Description:</strong> {review.description}</p>
                      <p className="review-rating"><strong>Rating:</strong> {review.rating}/5</p>
                    </div>
                  ))
                ) : (
                  <p className="no-reviews">No reviews for this movie.</p>
                )}
              </div>
            ))
          ) : (
            <p className="no-watchlist">No items in the watchlist.</p>
          )}
  
          <p className="stream-website">
            Website: <a href={stream.website} target="_blank" rel="noopener noreferrer">{stream.website}</a>
          </p>
        </div>
      ))}
    </div>
  );
  
};

export default MovieList;
