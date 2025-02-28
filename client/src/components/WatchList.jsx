import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import '../styles/movies.css'
import api from '../services/api';
import img from '../assests/images/img.jpg';

const WatchList = () => {
  const [watchlists, setWatchlists] = useState([]); 
  const [loading, setLoading] = useState(true); 
  const [error, setError] = useState(null); 
  const navigate=useNavigate()

  const fetchWatch = async () => {
    try {
      const response = await api.get('/watch/list');
      setWatchlists(response.data);
      setLoading(false);
    } catch (error) {
      setError(error.message);
    }
  };
  useEffect(() => {
    fetchWatch();
  }, []);

  const handleMovieClick = (id) => {
    navigate(`/watch/${id}/`);
  };
  if (loading) {
    return <div>Loading...</div>; 
  }
  if (error) {
    return <div>Error: {error}</div>; 
  }
  return (
    <div className="watchlist-container">
          {watchlists.length > 0 ? (
            watchlists.map(item => (
              <div key={item.id} className="watchlist-item" onClick={(id) => handleMovieClick(item.id)}>
                <h1 className="item-title"><strong>Title:</strong>{item.title}</h1>
                <div className='img-container'>
                  <img src={img} alt="movie_imge" />
                </div>
                <p className="item-storyline"><strong>Storyline:</strong>{item.storyline}</p>
                <p className="item-rating"><strong>Average Rating:</strong> {item.avg_rating}/5</p>
                <h4 className="reviews-heading">Reviews:</h4>
                {item.reviews && item.reviews.length > 0 ? (
                  item.reviews.map(review => (
                    <div key={review.id} className="review-item">
                      <p className="review-description"><strong>Description:</strong> {review.description}</p>
                    </div>
                  ))
                ) : (
                  <p className="no-reviews">No reviews for this movie.</p>
                )}
                <p className="reviews-btn" onClick={(id) => handleMovieClick(item.id)}>Leave Review</p>
              </div>
            ))
          ) : (
            <p className="no-watchlist">No items in the watchlist.</p>
          )}
    </div>
  );
  
};

export default WatchList;
