import React from 'react';
import './Profiles.css';
import logo from '../Images/logo.png';

function Profiles() {
 
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

    {/* Everything that's not the Top or Side Bar */}
      <div id='Body'>
        <h1><span>{user.username} | {user.role}</span></h1> <br></br>
        
        {/* Square with user's info */}
        <table style={{backgroundColor: "blanchedalmond", borderStyle: "solid", marginLeft:"200px"}}>
          <tr><th>
            {/* This is the first column TODO: you know*/}
            <div className='infoSquare'><h2>Name: <i>{user.name + ' ' + user.lastName}</i></h2></div>
            <div className='infoSquare'><h2>Gender: <i>{user.gender}</i></h2></div>
            <div className='infoSquare'><h2><i>{user.threads}</i> threads posted</h2></div>
            <div className='infoSquare' style={{height:"200px"}}><h2>Description: <i>{user.description}</i></h2></div>
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

export default Profiles;


  