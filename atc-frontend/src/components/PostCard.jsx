import React from 'react';

function PostCard({ post, onDetailsClick }) {
  return (
    <div style={{
      border: '1px solid #ccc',
      borderRadius: 8,
      padding: 15,
      marginBottom: 15,
      backgroundColor: '#fafafa',
    }}>
      <strong>{post.user}</strong>
      <p>{post.text.length > 100 ? post.text.substring(0, 100) + '...' : post.text}</p>
      <button onClick={() => onDetailsClick(post.id)}>Details</button>
    </div>
  );
}

export default PostCard;
