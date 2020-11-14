import React, {useState, useEffect} from 'react';
import './Home.css';
import example from '../Images/Example.PNG';
import {Link} from 'react-router-dom'

function Home() {
  // This would find the most recent threads from the backend
  const [recentThread, setRecentThread] = useState([{}]);

  useEffect(()=> {
    fetch('/api').then(
      response => response.json()
    ).then(data => setRecentThread(data))
  }, []);

  // This would be a List of Threads
  const recents = [recentThread, recentThread, recentThread];
  
  return (
    <div className="Home">

      <h1><span>Collector's Wiki</span></h1>

      <h2 style={{marginLeft: '200px'}}>Recent Threads: </h2>
      <div className='threads-div'>

      {recents.map((recent) => (

        <table className='threads-table'><tr>
          <th><Link to='/item'><img src={example} className="threadImage" alt="filler"></img></Link></th>
          <th><h2><b>{recent.item}</b></h2>
          <h2>By: <i>{recent.OP}</i></h2>
          <h2>On: <i>{recent.date}</i></h2></th>
          <th><h2>Latest Comment:</h2>
          <h2>{recent.collaborator} on <i>{recent.latestPing}</i></h2></th>    
        </tr></table>
      ))}
      </div>
    </div>
  );
}

export default Home;
