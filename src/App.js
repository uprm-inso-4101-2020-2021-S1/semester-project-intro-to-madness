import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
 
import Item from './Component/Item.js';
import Profiles from './Component/Profiles.js';
import Error from './Component/Error.js';
import Nav from './Component/Nav.js';
import Home from './Component/Home.js';
import About from './Component/About.js';
import Search from './Component/Search.js';
import Login from './Component/Login.js';
import Register from './Component/Register.js';
import Create from './Component/CreateThread.js';

function App() {
    return (      
      <Router>
        <div className="App">
          <Nav />
            <Switch>
              <Route path="/" component={Home} exact />
              <Route path="/item" component={Item} />
              <Route path="/profile" component={Profiles}/>
              <Route path="/about" component={About}/>
              <Route path="/search" component={Search}/>
              <Route path="/login" component={Login}/>
              <Route path="/register" component={Register}/>
              <Route path="/create" component={Create}/>
              
              <Route component={Error}/>
           </Switch>
        </div> 
      </Router>
    );
}

export default App;