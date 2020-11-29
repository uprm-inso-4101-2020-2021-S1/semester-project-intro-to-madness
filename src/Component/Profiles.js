import React from 'react';
import './Profiles.css';
import axios from 'axios';

const api = axios.create({
  baseURL: `http://127.0.0.1:5000/users`
})
class Profiles extends React.Component {

  state = {
    users: []
  }
  constructor() {
    super()
    api.get('/').then(res => {
      this.setState({users: res.data})
    })
    // this.state = {
    //   username: User.username,
    //   first_name: User.first_name,
    //   last_name: User.last_name,
    //   email: User.email,
    //   role: User.role,
    //   user_threads: 0,
    //   errors: {}
    // }
  }

  // This calls on the backend to find the user information.

  // This finds the user information
  // const filler = "No activity.";
  // var activity = [filler, filler, filler, filler];

  // const [threads, setThreads] = useState([{}]);

  // useEffect(()=> {
  //   fetch('/threads').then(
  //     response => response.json()
  //   ).then(data => setThreads(data.Thread))
  // }, []);

  // for (var i = 0; i < threads.length; i++) {
  //   var thrd = threads[i];
  //   if (thrd.user_id === user.ID) {
  //     user_threads++;
  //     activity.push(thrd.Date);
  //   }
  // }

  render () {
    return (
      <div className="UserProfile">

      {/* Everything that's not the Top or Side Bar */}
        <div id='Body'>
          <h1><span>{this.state.users.username} | {this.state.role}</span></h1> <br></br>
          {this.state.users.map((user) => (
            <h2>user.username</h2>
          ))}
          {/* Square with user's info */}
          <table style={{backgroundColor: "blanchedalmond", borderStyle: "solid", marginLeft:"200px"}}>
            <tr>
              {/* This is the first column*/}
              <th><table><tr>
                <th><div className='infoSquare'><h2>Name: <i>{this.state.first_name + ' ' + this.state.last_name}</i></h2></div></th>
                <th><div className='infoSquare'><h2>Threads posted: <i>Like 1</i></h2></div></th>
              </tr></table></th></tr>
              
              <th>
              {/* This is the "User Activity", aka the right side of the table */}
              <div className='infoSquare' style={{height:"260px", width:"1225px"}}>
                <h2>User Activity</h2>
                <table style={{marginLeft:"8px"}}>
                <tr><th><div className='actSquare'><h2>Filler Activity</h2></div></th>
                <th><div className='actSquare'><h2>Filler Activity</h2></div></th></tr>
                <tr><th><div className='actSquare'><h2>Filler Activity</h2></div></th>
                <th><div className='actSquare'><h2>Filler Activity</h2></div></th></tr>
                </table>
              </div>
            </th>
          </table>
          {/* End of squares */}
        </div>
      </div>
    );
  }
}

export default Profiles;