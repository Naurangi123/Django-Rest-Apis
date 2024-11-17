import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import '../styles/movies.css'
import api from '../api';

const WatchList = () => {
  const [watchlists, setWatchlists] = useState([]); 
  const [loading, setLoading] = useState(true); 
  const [error, setError] = useState(null); 
  const navigate=useNavigate()

  const fetchWatch = async () => {
    try {
      const response = await api.get('/watch/list');
      setWatchlists(response.data);
      console.log(response.data);
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
    <div className="stream-container">
          <h3 className="watchlist-heading">Watchlist:</h3>
          {watchlists.length > 0 ? (
            watchlists.map(item => (
              <div key={item.id} className="watchlist-item" onClick={(id) => handleMovieClick(item.id)}>
                <p className="item-title"><strong>Title:</strong> {item.title}</p>
                <p className="item-storyline"><strong>Storyline:</strong> {item.storyline}</p>
                <p className="item-rating"><strong>Average Rating:</strong> {item.avg_rating}/5</p>
                <h4 className="reviews-heading">Reviews:</h4>
                {item.reviews && item.reviews.length > 0 ? (
                  item.reviews.map(review => (
                    <div key={review.id} className="review-item">
                      <p className="review-description"><strong>Description:</strong> {review.description}</p>
                      <p className="review-user"><strong>Review User:</strong> {review.review_user}</p>
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
    </div>
  );
  
};

export default WatchList;
