import React from 'react';
import { Provider } from 'react-redux';
import store from './store/store';
import './styles/globals.css';

function App() {
  return (
    <Provider store={store}>
      <div className="app-container">
        <h1>Niche Fabric Research Tool</h1>
        <p>Multi-Platform Product Research & Analysis</p>
      </div>
    </Provider>
  );
}

export default App;
