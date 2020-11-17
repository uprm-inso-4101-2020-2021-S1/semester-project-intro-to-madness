import React, {useState, useEffect} from 'react';
import './Home.css';
import {Link} from 'react-router-dom'
// lol
function Home() {
  // This would find the most recent threads from the backend
  const [recentThread, setRecentThread] = useState([{}]);

  

  useEffect(()=> {
    fetch('/items').then(
      response => response.json()
    ).then(data => setRecentThread(data.Item))
  }, []);
  
  return (
    <div className="Home">

      <h1><span>Collector's Wiki</span></h1>

      <h2 style={{marginLeft: '200px'}}>Recent Threads: </h2>
      <div className='threads-div'>

      {recentThread.map((recent) => (

        <table className='threads-table'><tr>
          <th><Link to='/item'><img src={recent.image_url} className="threadImage" alt="Filler" /></Link></th>
          <th><h2>Item: <i>{recent.item_name}</i></h2>
          <h2>Price: <i>${recent.average_price}</i></h2></th>
          <th><h2>Date Created:</h2>
          <h2>*Filler Date*</h2></th>
        </tr></table>
      ))}
      </div>
    </div>
  );
}

export default Home;
