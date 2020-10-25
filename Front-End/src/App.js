import React from 'react';
import './Item.css';
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
      item: 'profesor',
      price: 'so much wow',
      description: 'will vaguely flunk you',
      history: 'so much history idk'
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
          
      </div>
    </div>
  );
}

export default App;
