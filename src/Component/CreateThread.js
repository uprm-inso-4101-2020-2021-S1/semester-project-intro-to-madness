import React, {Component} from 'react';
import './CreateThread.css';
import {createItem} from './UserFunctions.js';
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
          category: '',
          isDuplicate: false,
          date: new Date().toDateString(),
          user_ID: 0,
          errors: {}
        }
    
        this.onChange = this.onChange.bind(this)
        this.onSubmit = this.onSubmit.bind(this)
      }

      componentDidMount() {
        fetch('http://127.0.0.1:5000/users')
        .then(res => res.json())
        .then(json => {
          this.setState({
            user_ID: json.User[json.User.length-1].ID
          })
        })
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
            user_ID: this.state.user_ID
        }

        const newThread = {
            category: this.state.category,  
            date: this.state.date,
            isDuplicate: true,
            user_ID: this.state.user_ID
        }
    
        createItem(newItem).then(res => {})

        createThread(newThread).then(res => {
          this.props.history.push('/')
        })
      }

    render (){
        return(
        <div className="CreateThread">
    
          <table style={{backgroundColor: "#2F4F4F", borderStyle: "solid", position: "relative", margin: "auto", top: '60px'} }>
              <tr><th>
                
                <form noValidate onSubmit={this.onSubmit}>
                <h1 className="h3 mb-3 font-weight-normal" style={{marginLeft: "0", padding: "20px 20px"}}>Create Item</h1>
                <div className="form-group">
                  <label style={{float:"center"}} htmlFor="item_name">Item</label>
                  <input
                    type="text"
                    className="form-control"
                    name="item_name"
                    placeholder="Enter the item's name"
                    value={this.state.item_name}
                    onChange={this.onChange}/>
                <div className="form-group">
                  <label style={{float:"center"}} htmlFor="average_price">Suggested Price</label>
                  <input
                    type="text"
                    className="form-control"
                    name="average_price"
                    placeholder="Enter price"
                    value={this.state.average_price}
                    onChange={this.onChange}/>
                </div>
                <div className="form-group">
                  <label style={{float:"center"}} htmlFor="item_description">Description</label>
                  <input
                    type="text"
                    className="form-control"
                    name="item_description"
                    placeholder="Describe the item"
                    value={this.state.item_description}
                    onChange={this.onChange}/>
                </div>
                <div className="form-group">
                  <label style={{float:"center"}} htmlFor="item_history">History</label>
                  <input
                    type="text"
                    className="form-control"
                    name="item_history"
                    placeholder="Enter item's history"
                    value={this.state.item_history}
                    onChange={this.onChange}/>
                </div>
                <div className="form-group">
                  <label style={{float:"center"}} htmlFor="image_url">Picture</label>
                  <input
                    type="text"
                    className="form-control"
                    name="image_url"
                    placeholder="Insert url"
                    value={this.state.image_url}
                    onChange={this.onChange}/>
                </div>
                <div className="form-group">
                  <label style={{float:"center"}} htmlFor="category">Category</label>
                  <input
                    type="text"
                    className="form-control"
                    name="category"
                    placeholder="Item Category"
                    value={this.state.category}
                    onChange={this.onChange}/>
                </div>
                <button
                  type="submit"
                  className="btn btn-lg btn-primary btn-block">
                  Create!
                </button>
                </div>
              </form>
              </th></tr>
            </table>
          </div>
        );
      }
}

export default CreateThread;