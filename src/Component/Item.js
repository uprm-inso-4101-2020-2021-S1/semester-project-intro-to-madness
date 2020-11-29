import React, {useState, useEffect} from 'react';
import './Item.css';
import example from '../Images/Example.PNG';

  // Unfinished functions that make the buttons open up another page

  class Item extends React.Component{
  render (){
    return(
    <div className="ItemThread">

    {/* Everything that's not the Top or Side Bar */}
    <div id='Body'>
        {/*<table style={{backgroundColor: "#2F4F4F", borderStyle: "solid", position: "relative", right: '0', float: "right", top: '60px'}}>
          <tr><th>
              <div className='relatedTop'><h2>Related Items</h2></div>
              <div className='relatedSquare'><img id='relatedPictures' src={example} className="Web-logo" alt="example" /><a href="#" class="button" id='relatedButton'>Item Name</a></div>
              <div className='relatedSquare'><img id='relatedPictures' src={example} className="Web-logo" alt="example" /><a href="#" class="button" id='relatedButton'>Item Name</a></div>
              <div className='relatedSquare'><img id='relatedPictures' src={example} className="Web-logo" alt="example" /><a href="#" class="button" id='relatedButton'>Item Name</a></div>
              <div className='relatedSquare'><img id='relatedPictures' src={example} className="Web-logo" alt="example" /><a href="#" class="button" id='relatedButton'>Item Name</a></div>
              <div className='relatedSquare'><img id='relatedPictures' src={example} className="Web-logo" alt="example" /><a href="#" class="button" id='relatedButton'>Item Name</a></div>
            </th></tr>
    </table>*/}


      <table style={{backgroundColor: "#2F4F4F", borderStyle: "solid", position: "relative", margin: "auto", top: '60px'} }>
          <tr><th>
              <div className='bodyItem'><h2>{JSON.stringify(this.props.location.state.item)}</h2></div>
              <div className='bodySquare'><img id='picture' src={this.props.location.state.image} className="Web-logo" alt="filler" /></div>
              <div className='bodySquare'><h3>Price:</h3><p id='input'>${JSON.stringify(this.props.location.state.price)}</p></div>
              <div className='bodySquare'><h3>Item Description</h3><p id='input'>{JSON.stringify(this.props.location.state.description)}</p></div>
              <div className='bodySquare'><h3>Item History</h3><p id='input'>{JSON.stringify(this.props.location.state.history)}</p></div>
              <div className='bodySquare'><h3>Comments:</h3><p id='input'>No comments</p></div>
            </th></tr>
        </table>
      </div>
    </div>
    );
  }
}

export default Item;
