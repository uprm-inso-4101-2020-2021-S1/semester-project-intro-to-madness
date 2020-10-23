import React from 'react';
import './App.css';
import logo from './logo.png';

function App() {
 
  // Unfinished functions that make the buttons open up another page
  const signIn = () => {}
  const YourItems = () => {}
  const Popular = () => {}
  const Recent = () => {}
  const AboutUs = () => {}

  // This would call on the backend to find the user information
  const [user, setUser] = React.useState({
    username: 'Lordeth Diego',
    name: 'Diego',
    lastName: 'Cintrón',
    gender: 'Male',
    role: 'Moderator',
    threads: 2,
    description: 'Here is where I would put my description... IF I HAD ONE',
    activities: ['Commented on "Glass Mickey Figurine"', 'Posted a thread on "Holographic Charizard Card"', 'Replied to your Moms DMs' ,'Created Account']
  });

  return (
    <div className="UserProfile">
      <div id='TopBar'>
        <ul>
          <li className='top' id='left'><img src={logo} className="Web-logo" alt="logo" /></li>
          <li className='top' id='center'><input type="text" placeholder="Search threads.."></input></li>
          <li className='top' id='right'><button onClick={signIn}>Log In | Sign In</button></li>
        </ul>
      </div>

      <div id='SideBar'>
        <ul>
          <li style={{paddingTop: "10px"}}><button style={{width: "120px"}} onClick={YourItems}>Your Items</button></li>
          <li style={{paddingTop: "10px"}}><button style={{width: "120px"}} onClick={Popular}>Popular Items</button></li>
          <li style={{paddingTop: "10px"}}><button style={{width: "120px"}} onClick={Recent}>Recently Added</button></li>
          <li id='AboutUs'><button style={{width: "120px"}} onClick={AboutUs}>About Us</button></li>
        </ul>
      </div>

    {/* Everything that's not the Top or Side Bar */}
      <div id='Body'>
        <h1><span>{user.username} | {user.role}</span></h1> <br></br>
        
        {/* Square with user's info */}
        <table style={{backgroundColor: "blanchedalmond", borderStyle: "solid", marginLeft:"200px"}}>
          <tr><th>
            {/* This is the first column TODO: you know*/}
            <div className='infoSquare'><h2>Name: {user.name + ' ' + user.lastName}</h2></div>
            <div className='infoSquare'><h2>Gender: {user.gender}</h2></div>
            <div className='infoSquare'><h2>{user.threads} threads posted</h2></div>
            <div className='infoSquare' style={{height:"200px"}}><h2>Description: {user.description}</h2></div>
            </th><th>

            {/* This is the "User Activity", aka the right side of the table */}
            <div className='infoSquare' style={{height:"444px"}}>
              <h2>User Activity</h2>
              <div className='actSquare'><h2>{user.activities[0]}</h2></div>
              <div className='actSquare'><h2>{user.activities[1]}</h2></div>
              <div className='actSquare'><h2>{user.activities[2]}</h2></div>
              <div className='actSquare'><h2>{user.activities[3]}</h2></div>
            </div>
          </th></tr>
        </table>
        {/* End of squares */}
      </div>
    </div>
  );
}

export default App;
