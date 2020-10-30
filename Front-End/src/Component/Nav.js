import React from 'react';
import './Nav.css';
import example from '../Images/Example.PNG';
import { Link, withRouter } from 'react-router-dom';

   function Nav() {

   const YourItems = () => {}
   const Popular = () => {}
   const Recent = () => {}
   const AboutUs = () => {}
  
      const navStyle = {
         color: 'white'
      };

   return (
      <nav>
         <div id='TopBar'>
            <ul>
               <li className='top' id='left'><img src={example} className="Web-logo" alt="example" /></li>
               <li className='top' id='center'><input type="text" placeholder="Search threads.."></input></li>
               <u1 className="nav-links"><Link style={navStyle} to ='/profile'><button className='top' id='right'>Log In | Sign In</button></Link></u1>
            </ul>
         </div>

         <div id='SideBar'>
            <ul>
               <u1 className="nav-links"><Link style={navStyle} to ='/item'><li style={{paddingTop: "10px"}}><button style={{width: "120px"}} onClick={YourItems}>Your Items</button></li></Link></u1>
               <li style={{paddingTop: "10px"}}><button style={{width: "120px"}} onClick={Popular}>Popular Items</button></li>
               <li style={{paddingTop: "10px"}}><button style={{width: "120px"}} onClick={Recent}>Recently Added</button></li>
               <li id='AboutUs'><button style={{width: "120px"}} onClick={AboutUs}>About Us</button></li>
            </ul>
         </div>
      </nav>
   );
}
 
export default Nav;