import React from 'react';
import './Home.css';
import {Link, withRouter} from 'react-router-dom'

function Home() {
  return (
    <nav>
        <h3>Home</h3>
        <u1 className = "nav-links">
          <Link to='/item'> <li id='list'>Item</li></Link>
          <Link to='/profile'><li id='list'>Profiles</li></Link>
        </u1>
    </nav>
  );
}

export default Home;
