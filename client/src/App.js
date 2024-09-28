import React, { useState } from 'react';
import axios from 'axios';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min'; 

function App() {
  const [record, setRecord] = useState('');
  const [lastRecord, setLastRecord] = useState(null);
  const [message] = useState('');

  const handleAddRecord = () => {
    if (record.trim() !== '') {
      axios.post('http://localhost:5001/record', { record })
        .then(response => {
          console.log(response.data);
          setRecord('');
        })
        .catch(error => {
          console.error('There was an error adding the record!', error);
        });
    }
  };

  const handleGetRecord = () => {
    axios.get('http://localhost:5001/record')
      .then(response => {
        setLastRecord(response.data.record);
        console.log(response)
      })
      .catch(error => {
        console.error('There was an error fetching the record!', error);
        setLastRecord(null);
      });
  };

  return (
    <div className="container mt-5">
      <div className="card p-4 shadow-sm">
        <h1 className="text-primary text-center mb-4">Record Logger</h1>
        <div className="row">
          <div className="col-md-6">
            <h2>Insert a Record</h2>
            <div className="mb-3">
              <input 
                type="text" 
                value={record} 
                onChange={(e) => setRecord(e.target.value)} 
                className="form-control"
                placeholder="Enter a record" 
              />
            </div>
            <button className="btn btn-primary w-100 mb-2" onClick={handleAddRecord}>Add Record</button>
            {message && <div className="alert alert-info mt-2">{message}</div>}
          </div>
          <div className="col-md-6">
            <h2>Get the Last Record</h2>
            <button className="btn btn-secondary w-100 mb-3" onClick={handleGetRecord}>Get Last Record</button>
            {lastRecord !== null && (
              <div className="card p-3">
                <h5 className="card-title">Last Record</h5>
                <p className="card-text">{lastRecord}</p>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;

