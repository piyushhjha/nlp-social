import React, { useState, useEffect } from 'react';
import axios from 'axios';

function PostDetail({ postId, onBack }) {
  const [post, setPost] = useState(null);

  useEffect(() => {
    if (postId) {
      fetchPost(postId);
    }
  }, [postId]);

  const fetchPost = async (id) => {
    try {
      const res = await axios.get(`http://localhost:5000/api/posts/${id}`);
      setPost(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  if (!post) return <div>Loading...</div>;

  return (
    <div>
      <button onClick={onBack}>Back to List</button>
      <h3>Post by {post.user}</h3>
      <p>{post.text}</p>
      <p><strong>Created:</strong> {post.created_at}</p>
      <p><strong>Location:</strong> {post.location_text || 'N/A'}</p>
      <p><strong>Likes:</strong> {post.likes} | <strong>Retweets:</strong> {post.retweets}</p>
      {/* <h4>NLP Analysis</h4>
      <pre style={{ backgroundColor: '#eee', padding: '10px', whiteSpace: 'pre-wrap' }}>
        {JSON.stringify(post.nlp, null, 2)}
      </pre> */}
    </div>
  );
}

export default PostDetail;
