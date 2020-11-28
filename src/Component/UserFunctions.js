import axios from 'axios'

export const register = newUser => {
  return axios
    .post('http://127.0.0.1:5000/users/register', { 
      username: newUser.username,
      first_name: newUser.first_name,
      last_name: newUser.last_name,
      email: newUser.email,
      password: newUser.password,
      role:'user'
    })
    .then(response => {
      console.log('Registered')
    })
}
export const login = user => {
  return axios
  .post('users/login', {
      email: user.email,
      password: user.password
    })
    .then(response => {
      localStorage.setItem('usertoken', response.data)
      return response.data
    })
    .catch(err => {
      console.log(err)
    })
}

export const getProfile = user => {
  return axios
    .get('users/profile', {
      //headers: { Authorization: ` ${this.getToken()}` }
    })
    .then(response => {
      console.log(response)
      return response.data
    })
    .catch(err => {
      console.log(err)
    })
}
