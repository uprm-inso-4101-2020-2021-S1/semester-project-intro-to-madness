import React, {useState, useEffect} from 'react';
import './Home.css';
import {Link} from 'react-router-dom'

function Home() {

  // This finds  the most recent threads from the backend
  const [threads, setThreads] = useState([{}]);

  const [items, setItems] = useState([{}]);

  useEffect(()=> {
    fetch('/threads').then(
      response => response.json()
    ).then(data => setThreads(data.Thread.slice(-3)))
  }, []);

  useEffect(()=> {
    fetch('/items').then(
      response => response.json()
    ).then(data => setItems(data.Item.slice(-3)))
  }, []);
  
  var i = 0;

  return (
    <div className="Home">

      <h1><span>Collector's Wiki</span></h1>

      <h2 style={{marginLeft: '200px'}}>Recent Threads: </h2>
      <div className='threads-div'>

      {items.map((recent) => (

        <table className='threads-table'><tr>
          <th><Link to={{
            pathname: "/item",
            search: recent.item_name,
            state:{
              item: recent.item_name,
              image: recent.image_url,
              price: recent.average_price,
              description: recent.item_description,
              history: recent.item_history
            }
            }}><img src={recent.image_url} className="threadImage" alt="Filler" /></Link></th>
          <th><h2>Item: <i>{recent.item_name}</i></h2>
          <h2>Price: <i>${recent.average_price}</i></h2></th>
          <th><h2>Date Created:</h2>
          <h2>{threads[i++].Date}</h2></th>
        </tr></table>
      ))}
      </div>
    </div>
  );
}

export default Home;
