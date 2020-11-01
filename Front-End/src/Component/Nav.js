import React from 'react';
import './Nav.css';
import example from '../Images/logo.png';
import { Link, withRouter } from 'react-router-dom';

   function Nav() {
  
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
               <u1 className="nav-links"><Link style={navStyle} to ='/'><li style={{paddingTop: "10px"}}><button style={{width: "120px"}}>Home</button></li></Link></u1>
               <u1 className="nav-links"><Link style={navStyle} to ='/item'><li><button style={{width: "120px"}}>Your Items</button></li></Link></u1>
               <u1 className="nav-links"><Link style={navStyle} to ='/search'><li><button style={{width: "120px"}}>Popular Items</button></li></Link></u1>
               <u1 className="nav-links"><Link style={navStyle} to ='/'><li><button style={{width: "120px"}}>Recently Added</button></li></Link></u1>
               <u1 className="nav-links"><Link style={navStyle} to ='/about'><li id='AboutUs'><button style={{width: "120px"}}>About Us</button></li></Link></u1>
            </ul>
         </div>
      </nav>
   );
}
 
export default Nav;