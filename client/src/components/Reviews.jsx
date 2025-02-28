import { useState, useEffect } from 'react';
// import { useNavigate } from 'react-router-dom';
import '../styles/movies.css'
import api from '../services/api';
// import img from '../assests/images/img.jpg';

export default function WatchList() {
  const [watchlists, setWatchlists] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  // const navigate = useNavigate()

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

  if (loading) {
    return <div>Loading...</div>;
  }
  if (error) {
    return <div>Error: {error}</div>;
  }
  return (
    <div className="stream-container">
      <h4 className="reviews-heading">Reviews:</h4>
      {watchlists.reviews && watchlists.reviews.length > 0 ? (
        watchlists.reviews.map(review => (
          <div key={review.id} className="review-item">
            <p className="review-description"><strong>Description:</strong> {review.description}</p>
            <p className="review-user"><strong>Review User:</strong> {review.review_user}</p>
            <p className="review-rating"><strong>Rating:</strong> {review.rating}/5</p>
          </div>
        ))
      ) : (
        <p className="no-reviews">No reviews for this movie.</p>
      )}
      <a href="/reviews">Leave Review</a>
    </div>
  );

};


