import React from 'react';
import './Login.css';

  // Unfinished functions that make the buttons open up another page
  function Login() {


  // This would call on the backend to find the user information
//   const [login, setUser] = React.useState({
//       firstname: 'Carl',
//       lastname: 'Winslow',
//       username: 'UrcleWhisperer',
//     email: 'Familymatters@gmail.com',
//     password: 'UrcleNeverLeaves',
//     cpassword: 'UrcleNeverLeaves'
//   });

  

  return (
    <div className="Login">
<h1 style={{float:"center",marginLeft:"200px"}}>Login & Registration</h1>
    {/* Everything that's not the Top or Side Bar */}
      <div id='Body'>
        
        {/* Square with user's info */}
        <table style={{float:"left",backgroundColor: "blanchedalmond", borderStyle: "solid", marginLeft:"250px"}}>
          <tr><th>
            {/* This is the first column TODO: you know*/}
            <div className='CredentialSquare'><h2 style={{float:"left"}}>UserName: </h2><input type="text" placeholder=""style={{marginTop:"25px"}}/></div>
            <div className='CredentialSquare'><h2 style={{float:"left"}}>Password: </h2><input type="text" placeholder=""style={{marginTop:"25px"}}/></div>
          
            </th>
            </tr>
            </table>
            <table style={{float:"right",backgroundColor: "blanchedalmond", borderStyle: "solid", marginRight:"150px"}}>
          <tr><th>
          <div className='CredentialSquare'><h2 style={{float:"left"}}>Name: </h2><input type="text" placeholder=""style={{marginTop:"25px"}}/></div>
          <div className='CredentialSquare'><h2 style={{float:"left"}}>UserName: </h2><input type="text" placeholder=""style={{marginTop:"25px"}}/></div>
          <div className='CredentialSquare'><h2 style={{float:"left"}}>Email: </h2><input type="text" placeholder=""style={{marginTop:"25px"}}/></div>
          <div className='CredentialSquare'><h2 style={{float:"left"}}>Password: </h2><input type="text" placeholder=""style={{marginTop:"25px"}}/></div>
          <div className='CredentialSquare'><h2 style={{float:"left"}}>Confirm: </h2><input type="text" placeholder=""style={{marginTop:"25px"}}/></div>
            </th>
            </tr>
            </table>
            </div>
            </div>
  
  )
}

export default Login;

