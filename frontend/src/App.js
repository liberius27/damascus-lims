import { useEffect, useState } from 'react';
import './App.css';
import { getSamples } from './services/api';

function App() {
    const [samples, setSamples] = useState([]);

    useEffect(() => {
        getSamples().then(data => {
            console.log("Fetched samples:", data);
            setSamples(data || []);
        });
    }, []);

    return (
        <div className="App">
            <header className="App-header">
                <h1>Sample Management Dashboard</h1>
                <p>Below are the samples fetched from the backend:</p>
                <ul>
                    {samples.length > 0 ? (
                        samples.map((sample, index) => (
                            <li key={index}>{JSON.stringify(sample)}</li>
                        ))
                    ) : (
                        <p>No samples available</p>
                    )}
                </ul>
            </header>
        </div>
    );
}

export default App;