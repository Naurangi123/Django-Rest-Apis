import React, { useState, useEffect, useCallback } from 'react';
import { useParams } from 'react-router-dom';
import { ACCESS_TOKEN } from '../constants'
import api from '../services/api';
import '../styles/movies.css';

export default function WatchDetail(){
  const { id } = useParams();
  const [movie, setMovie] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [reviewText, setReviewText] = useState('');
  const [rating, setRating] = useState(1);
  const[isActive, setIsActive] = useState(false);
  const [isVisible, setIsVisible] = useState(false);
  const [userReviewed, setUserReviewed] = useState(false);
  const [user,setUser]= useState(null);

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
      }
      catch(error){
        setError(error.message);
      }
    }
    getUser();
  },[])

  const fetchMovieDetail = useCallback(async () => {
    setLoading(true);
    try {
      const response = await api.get(`/watch/${id}/`);
      setMovie(response.data);
      setLoading(false);
      const userReview=response.data.reviews.find(review=>review.review_user===user?.id);
      if(userReview){
        setUserReviewed(true);
      }
    } catch (error) {
      setError(error.message);
      setLoading(false);
    }
  }, [id,user]);

  const handleReviewSubmit = async (e) => {
    e.preventDefault();

    if(userReviewed){
      alert("You have already reviewed this movie.");
      return;
    }
    try {
      const newReview = {
        description: reviewText,
        rating,
        isActive,
      };
      await api.post(`/watch/${id}/review-create/`, newReview,{
        headers: {
          Authorization: `Bearer ${sessionStorage.getItem('access')}`,
        },
      });
      setReviewText('');
      setRating(1);
      fetchMovieDetail();
    } catch (err) {
      setError("Failed to submit review");
    }
  };

  useEffect(() => {
    fetchMovieDetail();
  }, [id, fetchMovieDetail]);

  const toggleVisibility = () => {
    setIsVisible(!isVisible);
  };

  if (loading) {
    return <div className="loading">Loading...</div>;
  }

  if (error) {
    return <div className="error-message">Error: {error}</div>;
  }

  if (!movie) {
    return <div className="error-message">No movie found.</div>;
  }

  return (
    <div className="movie-detail-container">
      <div className='movie_detail'>
        <h2>{movie.title}</h2>
        <p><strong>Storyline:</strong> {movie.storyline}</p>
        <p><strong>Average Rating:</strong> {movie.avg_rating}/5</p>

        <h3>Reviews:</h3>
        {movie.reviews && movie.reviews.length > 0 ? (
          movie.reviews.map((review) => (
            <div key={review.id} className="review-item">
              <p><strong>Description:</strong> {review.description}</p>
              <p><strong>Review User:</strong> {review.review_user}</p>
              <p><strong>Rating:</strong> {review.rating}/5</p>
            </div>
          ))
        ) : (
          <div>
            <p>No reviews for this movie.</p>
          </div>
        )}
        <button onClick={toggleVisibility}>Write a Review</button>
        {isVisible && !userReviewed && (
          <div className="review-form">
            <h4>Write a Review</h4>
            <form onSubmit={handleReviewSubmit}>
              <textarea
                value={reviewText}
                onChange={(e) => setReviewText(e.target.value)}
                placeholder="Write your review here..."
                required
              />
              <div>
                <label>Is Active:</label>
                <select
                  value={isActive}
                  onChange={(e) => setIsActive(e.target.value === "true")}
                  required
                >
                  <option value={true}>Active</option>
                  <option value={false}>Inactive</option>
                </select>
              </div>
              <div>
                <label>Rating:</label>
                <select
                  value={rating}
                  onChange={(e) => setRating(Number(e.target.value))}
                  required
                >
                  {[1, 2, 3, 4, 5].map((rate) => (
                    <option key={rate} value={rate}>
                      {rate}
                    </option>
                  ))}
                </select>
              </div>
              <button type="submit">Submit Review</button>
            </form>
          </div>
        )}
        </div>
      </div>
  );
};


