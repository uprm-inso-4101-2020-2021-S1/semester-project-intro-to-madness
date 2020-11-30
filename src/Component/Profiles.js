import React, {useState, useEffect} from 'react';
import './Profiles.css';

function Profiles() {

  // This calls on the backend to find the user information.
  const [user, setUser] = useState([{}]);
  var user_threads = 0;

  useEffect(()=> {
    fetch('/users').then(
      response => response.json()
    ).then(data => setUser(data.User[data.User.length-1]))
  }, []);

  // This finds the user information
  const filler = "No activity.";
  var activity = [filler, filler, filler, filler];

  const [threads, setThreads] = useState([{}]);

  useEffect(()=> {
    fetch('/threads').then(
      response => response.json()
    ).then(data => setThreads(data.Thread))
  }, []);

  for (var i = 0; i < threads.length; i++) {
    var thrd = threads[i];
    if (thrd.user_id === user.ID) {
      user_threads++;
      activity.push(thrd.Date);
    }
  }

  return (
    <div className="UserProfile">

    {/* Everything that's not the Top or Side Bar */}
      <div id='Body'>
        <h1><span>{user.username} | {user.role}</span></h1> <br></br>
        
        {/* Square with user's info */}
        <table style={{backgroundColor: "blanchedalmond", borderStyle: "solid", marginLeft:"200px"}}>
          <tr>
            {/* This is the first column*/}
            <th><table><tr>
              <th><div className='infoSquare'><h2>Name: <i>{user.first_name + ' ' + user.last_name}</i></h2></div></th>
              <th><div className='infoSquare'><h2>Threads posted: <i>{user_threads}</i></h2></div></th>
            </tr></table></th></tr>
            
            <th>
            {/* This is the "User Activity", aka the right side of the table */}
            <div className='infoSquare' style={{height:"260px", width:"1225px"}}>
              <h2>User Activity</h2>
              <table style={{marginLeft:"8px"}}>
              <tr><th><div className='actSquare'><h2>{activity[activity.length-1]}</h2></div></th>
              <th><div className='actSquare'><h2>{activity[activity.length-2]}</h2></div></th></tr>
              <tr><th><div className='actSquare'><h2>{activity[activity.length-3]}</h2></div></th>
              <th><div className='actSquare'><h2>{activity[activity.length-4]}</h2></div></th></tr>
              </table>
            </div>
          </th>
        </table>
        {/* End of squares */}
      </div>
    </div>
  );
}

export default Profiles;

  