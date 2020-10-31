import React from 'react';
import './Nav.css';
import example from '../Images/logo.png';
import { Link, withRouter } from 'react-router-dom';

   function Nav() {

   const YourItems = () => {}
   const Popular = () => {}
   const Recent = () => {}
   const About = () => {}
   const Home = () => {}
  
      const navStyle = {
         color: 'white'
      };

   return (
      <nav>
         <div id='TopBar'>
            <ul>
               <li className='top' id='left'><Link style={navStyle} to = '/'><img src={example} className="Web-logo" alt="example" /></Link></li>
               <li className='top'><input type="text" placeholder="Search threads.." id='searchBar'></input></li>
               <u1 className="nav-links"><Link style={navStyle} to ='/profile'><button id='right'>Log In | Sign In</button></Link></u1>
            </ul>
         </div>

         <div id='SideBar'>
            <ul>
               <u1 className="nav-links"><Link style={navStyle} to ='/'><li style={{paddingTop: "10px"}}><button style={{width: "120px"}} onClick={Home}>Home</button></li></Link></u1>
               <u1 className="nav-links"><Link style={navStyle} to ='/item'><li><button style={{width: "120px"}} onClick={YourItems}>Your Items</button></li></Link></u1>
               <li style={{paddingTop: "10px"}}><button style={{width: "120px"}} onClick={Popular}>Popular Items</button></li>
               <li style={{paddingTop: "10px"}}><button style={{width: "120px"}} onClick={Recent}>Recently Added</button></li>
               <u1 className="nav-links"><Link style={navStyle} to ='/about'><li id='AboutUs'><button style={{width: "120px"}} onClick={About}>About Us</button></li></Link></u1>
            </ul>
         </div>
      </nav>
   );
}
 
export default Nav;