import { useEffect, useState } from 'react';
import './App.css';

// Import the API function
import { getSamples } from './services/api';

function App() {
  const [samples, setSamples] = useState([]);

  useEffect(() => {
    getSamples().then(data => {
        console.log("Fetched samples in App.js:", data); // Debugging log
        setSamples(data || []); // Update state with the fetched data
    });
}, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Sample Management Dashboard</h1>
        <p>Below are the samples fetched from the backend:</p>
        <ul>
        {samples.length > 0 ? (
            samples.map((sample, index) => {
                console.log("Rendering sample:", sample);
                return <li key={index}>{JSON.stringify(sample)}</li>;
            })
        ) : (
            <p>No samples available</p>
        )}
        </ul>
      </header>
    </div>
  );
}

export default App;
