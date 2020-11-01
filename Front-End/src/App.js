import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
 
import Item from './Component/Item.js';
import Profiles from './Component/Profiles.js';
import Error from './Component/Error.js';
import Nav from './Component/Nav.js';
import Home from './Component/Home.js';
import About from './Component/About.js';
import Search from './Component/Search.js';
 
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
              <Route component={Error}/>
           </Switch>
        </div> 
      </Router>
    );
}

export default App;