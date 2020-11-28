import React, { Component } from 'react'
import { login } from './UserFunctions'

class Login extends Component {
  constructor() {
    super()
    this.state = {
      eusername: '',
      password: '',
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

    const user = {
      username: this.state.username,
      password: this.state.password
    }

    login(user).then(res => {
      if (!res.error) {
        this.props.history.push(`/http://127.0.0.1:5000/user/profile`)
      }
    })
  }

  render() {
    return (
      <div className="container">
        <div className="row">
          <div className="col-md-6 mt-5 mx-auto">
            <form noValidate onSubmit={this.onSubmit}>
              <h1 style={{float:"center",Right:"350px"}} className="h3 mb-3 font-weight-normal">Log In</h1>
              <div className="form-group">
                <label style={{float:"center",marginLeft:"200px"}} htmlFor="email">Username</label>
                <input
                  type="username"
                  className="form-control"
                  name="username"
                  placeholder="Enter username"
                  value={this.state.username}
                  onChange={this.onChange}
                />
              </div>
              <div className="form-group">
                <label style={{float:"center",marginLeft:"200px"}} htmlFor="password">Password</label>
                <input
                  type="password"
                  className="form-control"
                  name="password"
                  placeholder="Password"
                  value={this.state.password}
                  onChange={this.onChange}
                />
              </div>
              <button style={{marginLeft:"200px"}}
                type="submit"
                className="btn btn-lg btn-primary btn-block"
              >
                Sign in
              </button>
            </form>
          </div>
        </div>
      </div>
    )
  }
}

export default Login



