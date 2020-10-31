import React from 'react';
import './Home.css';
import example from '../Images/Example.PNG';
import {Link, withRouter} from 'react-router-dom'

function Home() {
  // This would find the most recent threads... somehow?
  // This would be a List of Threads
  // const [recentThreads, setRecentThreads] = React.useState({
    
  // });

  /* For now its hard-coded*/
  const [thread1, setThread1] = React.useState({
    item: "Holographic Charizard",
    image: example,
    OP: "Lordeth Diego",
    collaborator: "TeylorSwish",
    date: "2020/10/30",
    latestPing: "2020/10/31"
  });
  const recents = [thread1, thread1, thread1];
  
  return (
    <div className="Home">

      <h1><span>Collector's Wiki</span></h1>
      {/* <div className = "nav-links">
        <u1>
          <h3>Quick Links:</h3>
          <Link to='/item'><li id='list'>Item</li></Link>
          <Link to='/profile'><li id='list'>Profiles</li></Link>
        </u1>
      </div> */}

      <h2 style={{marginLeft: '200px'}}>Recent Threads: </h2>
      <div id='Recents'>

      {recents.map((recent) => (

        <table className='threads'><tr>
          <th><Link to='/item'><img src={recent.image} className="threadImage"></img></Link></th>
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
