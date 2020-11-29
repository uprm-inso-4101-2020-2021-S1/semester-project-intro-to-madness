import React, {Component} from 'react';
import './CreateThread.css';
import {createThread} from './UserFunctions.js';

class CreateThread extends Component {

    constructor() {
        super()
        this.state = {
          item_name: '',
          item_description: '',
          item_history: '',
          average_price: '',
          image_url: '',
          errors: {}
        }
    
        this.onChange = this.onChange.bind(this)
        this.onSubmit = this.onSubmit.bind(this)
      }
    
      onChange(e) {
        this.setState({ [e.target.name]: e.target.value })
      }
      onSubmit(e) {
        e.preventDefault()
    
        const newItem = {
            item_name: this.state.item_name,    
            average_price: this.state.average_price,
            item_history: this.state.item_history,
            item_description: this.state.item_description,
            image_url: this.state.image_url,
            user_ID: 1
        }
    
        createThread(newItem).then(res => {
          this.props.history.push('/')
        })
      }

    render (){
        return(
        <div className="CreateThread">
    
          <table style={{backgroundColor: "#2F4F4F", borderStyle: "solid", position: "relative", margin: "auto", top: '60px'} }>
              <tr><th>
              
              <form noValidate onSubmit={this.onSubmit}>
              <h1 className="h3 mb-3 font-weight-normal">Create Item</h1>
              <div className="form-group">
                <label style={{float:"center"}} htmlFor="item_name">Item</label>
                <input
                  type="text"
                  className="form-control"
                  name="item_name"
                  placeholder="Enter the item's name"
                  value={this.state.item_name}
                  onChange={this.onChange}
                />
              <div className="form-group">
                <label style={{float:"center"}} htmlFor="average_price">Suggested Price</label>
                <input
                  type="text"
                  className="form-control"
                  name="average_price"
                  placeholder="Enter price"
                  value={this.state.average_price}
                  onChange={this.onChange}
                />
              </div>
              <div className="form-group">
                <label style={{float:"center"}} htmlFor="item_description">Description</label>
                <input
                  type="text"
                  className="form-control"
                  name="item_description"
                  placeholder="Describe the item"
                  value={this.state.item_description}
                  onChange={this.onChange}
                />
              </div>
              <div className="form-group">
                <label style={{float:"center"}} htmlFor="item_history">History</label>
                <input
                  type="text"
                  className="form-control"
                  name="item_history"
                  placeholder="Enter item's history"
                  value={this.state.item_history}
                  onChange={this.onChange}
                />
              </div>
              <div className="form-group">
                <label style={{float:"center"}} htmlFor="image_url">Picture</label>
                <input
                  type="text"
                  className="form-control"
                  name="image_url"
                  placeholder="Url"
                  value={this.state.image_url}
                  onChange={this.onChange}
                />
              </div>
              <button
                type="submit"
                className="btn btn-lg btn-primary btn-block"
              >
                Create!
              </button>
              </div>
            </form>
                  {/* <div className='bodyItem'><h2>Item Name: </h2></div>
                  <div className='bodySquare'><img id='picture' src={filler} className="Web-logo" alt="filler" /></div>
                  <div className='bodySquare'><h3>Price:</h3><p id='input'>$   </p></div>
                  <div className='bodySquare'><h3>Item Description</h3><p id='input'>   </p></div>
                  <div className='bodySquare'><h3>Item History</h3><p id='input'>   </p></div>
                  <div className='bodySquare'><h3>Comments:</h3><p id='input'>No comments</p></div> */}
                </th></tr>
            </table>
          </div>
        );
      }
}

export default CreateThread;