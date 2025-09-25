import React, { useState } from 'react';
import PostList from './components/PostList';
import PostDetail from './components/PostDetail';

function App() {
  const [selectedPostId, setSelectedPostId] = useState(null);

  return (
    <div className="App" style={{ maxWidth: 800, margin: 'auto', padding: 20 }}>
      <h1>Disaster Posts Viewer</h1>
      {selectedPostId ? (
        <PostDetail postId={selectedPostId} onBack={() => setSelectedPostId(null)} />
      ) : (
        <PostList onSelectPost={setSelectedPostId} />
      )}
    </div>
  );
}

export default App;
