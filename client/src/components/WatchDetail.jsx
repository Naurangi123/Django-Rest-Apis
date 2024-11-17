import React, { useState, useEffect, useCallback } from 'react';
import { useParams } from 'react-router-dom';  
import api from '../api';

const WatchDetail = () => {
  const { id } = useParams();  
  const [movie, setMovie] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchMovieDetail = useCallback(async () => {
    setLoading(true); 
    try {
      const response = await api.get(`/watch/${id}/`);
      setMovie(response.data);
      console.log(response.data);
      setLoading(false);
    } catch (error) {
      setError(error.message);
      setLoading(false);
    }
  }, [id]);

  useEffect(() => {
    console.log("Fetching details for movie with ID:", id);
    fetchMovieDetail();
  }, [id, fetchMovieDetail]); 

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  if (!movie) {
    return <div>No movie found.</div>;
  }

  return (
    <div className="movie-detail-container">
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
        <p>No reviews for this movie.</p>
      )}
    </div>
  );
};

export default WatchDetail;
