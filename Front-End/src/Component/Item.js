import React from 'react';
import './Item.css';
import example from '../Images/Example.PNG';
import { NavLink } from 'react-router-dom';

  // Unfinished functions that make the buttons open up another page
  function Item() {


  // This would call on the backend to find the user information
  const [item, setUser] = React.useState({
      item: 'profesor',
      price: '$1000000',
      description: 'will vaguely flunk ',
      history: 'so much history idk '
  });

  return (
    <div className="ItemThread">

    {/* Everything that's not the Top or Side Bar */}
    <div id='Body'>
        <table style={{backgroundColor: "#2F4F4F", borderStyle: "solid", position: "relative", right: '0', float: "right", top: '60px'}}>
          <tr><th>
              <div className='relatedTop'><h2>Related Items</h2></div>
              <div className='relatedSquare'><img id='relatedPictures' src={example} className="Web-logo" alt="example" /><a href="#" class="button" id='relatedButton'>Item Name</a></div>
              <div className='relatedSquare'><img id='relatedPictures' src={example} className="Web-logo" alt="example" /><a href="#" class="button" id='relatedButton'>Item Name</a></div>
              <div className='relatedSquare'><img id='relatedPictures' src={example} className="Web-logo" alt="example" /><a href="#" class="button" id='relatedButton'>Item Name</a></div>
              <div className='relatedSquare'><img id='relatedPictures' src={example} className="Web-logo" alt="example" /><a href="#" class="button" id='relatedButton'>Item Name</a></div>
              <div className='relatedSquare'><img id='relatedPictures' src={example} className="Web-logo" alt="example" /><a href="#" class="button" id='relatedButton'>Item Name</a></div>
            </th></tr>
        </table>


      <table style={{backgroundColor: "#2F4F4F", borderStyle: "solid", position: "relative", margin: "auto", top: '60px'} }>
          <tr><th>
              <div className='bodyItem'><h2>{item.item}</h2></div>
              <div className='bodySquare'><img id='picture' src={example} className="Web-logo" alt="example" /></div>
              <div className='bodySquare'><h3>Price:</h3><p id='input'>{item.price}</p></div>
              <div className='bodySquare'><h3>Item Description</h3><p id='input'>{item.description}</p></div>
              <div className='bodySquare'><h3>Item History</h3><p id='input'>{item.history}</p></div>
              <div className='bodySquare'><h3>Commments:</h3><p id='input'>No comments</p></div>
            </th></tr>
        </table>
      </div>
    </div>
  );
}

export default Item;
