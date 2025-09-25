import React, { useState, useEffect } from 'react';
import axios from 'axios';
import PostCard from './PostCard';

function PostList({ onSelectPost }) {
  const [posts, setPosts] = useState([]);
  const [page, setPage] = useState(1);
  const [total, setTotal] = useState(0);
  const perPage = 20;

  useEffect(() => {
    fetchPosts(page);
  }, [page]);

const fetchPosts = async (page) => {
  try {
    const res = await axios.get('http://localhost:5000/api/posts', {
      params: { page, per_page: perPage }
    });
    console.log('Fetched posts:', res.data.posts);
    setPosts(res.data.posts);
    setTotal(res.data.total);
  } catch (err) {
    console.error('Error fetching posts:', err);
  }
};

  const nextPage = () => {
    if (page * perPage < total) setPage(page + 1);
  };

  const prevPage = () => {
    if (page > 1) setPage(page - 1);
  };

  return (
    <div>
      <h2>Posts</h2>
      {posts.length === 0 ? (
        <p>No posts to display.</p>
      ) : (
        posts.map(post => (
          <PostCard key={post.id} post={post} onDetailsClick={onSelectPost} />
        ))
      )}
      <button onClick={prevPage} disabled={page === 1}>Prev</button>
      <button onClick={nextPage} disabled={page * perPage >= total}>Next</button>
      <p>Page {page} of {Math.ceil(total / perPage)}</p>
    </div>
  );
}

export default PostList;
