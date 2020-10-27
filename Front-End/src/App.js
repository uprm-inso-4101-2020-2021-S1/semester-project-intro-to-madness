import React from 'react';
import './Item.css';
import example from './Example.PNG';


function App() {
 
  // Unfinished functions that make the buttons open up another page
  const signIn = () => {}
  const YourItems = () => {}
  const Popular = () => {}
  const Recent = () => {}
  const AboutUs = () => {}
  const relatedPictures = () => {}
  const comments = () => {}

  // This would call on the backend to find the user information
  const [user, setUser] = React.useState({
      item: 'profesor',
      price: '$1000000',
      description: 'will vaguely flunk ',
      history: '$so much history idk '
  });

  return (
    <div className="ItemThread">
      <div id='TopBar'>
        <ul>
          <li className='top' id='left'><img src={example} className="Web-logo" alt="example" /></li>
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
      <div id='Table'>
        <table style={{backgroundColor: "#2F4F4F", borderStyle: "solid", position: "absolute", right: "0px", float: "right"} }>
          <tr><th>
              <div className='relatedTop'><h2>Related Items</h2></div>
              <div className='pictureSquare'><img id='relatedPictures' src={example} className="Web-logo" alt="example" /><a href="#" class="button" id='picturesButton'>Item Name</a></div>
              <div className='pictureSquare'><img id='relatedPictures' src={example} className="Web-logo" alt="example" /><a href="#" class="button" id='picturesButton'>Item Name</a></div>
              <div className='pictureSquare'><img id='relatedPictures' src={example} className="Web-logo" alt="example" /><a href="#" class="button" id='picturesButton'>Item Name</a></div>
              <div className='pictureSquare'><img id='relatedPictures' src={example} className="Web-logo" alt="example" /><a href="#" class="button" id='picturesButton'>Item Name</a></div>
              <div className='pictureSquare'><img id='relatedPictures' src={example} className="Web-logo" alt="example" /><a href="#" class="button" id='picturesButton'>Item Name</a></div>
            </th></tr>
        </table>
      </div>
      <div id='User'>
        <h1 className='body'>{user.item}</h1> <br></br>
        <div className='body'><img style={{width: "200px", height: "150px"}} src={example} className="Web-logo" alt="example" /></div>
        <h1 className='body'>{user.price}</h1>
        <h3 style={{position: "relative", left: "300px"}}>Item Description</h3>
        <div className='input'>{user.description}</div>
        <h3 style={{position: "relative", left: "300px"}}>Item History</h3>
        <p className='input' style={{borderStyle: "solid"}}>{user.history}</p>
        <h3 style={{position: "relative", left: "300px"}}>Comments:</h3>
        <p className='input' style={{borderStyle: "solid"}}>No comments</p>
      </div>
    </div>
  );
}

export default App;
