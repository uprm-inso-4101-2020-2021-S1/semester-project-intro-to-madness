import axios from 'axios';

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
  .post('http://127.0.0.1:5000/users/login', {
      username: user.username,
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
    .get('http://127.0.0.1:5000/users/profile', {
      // headers: { Authorization: ` ${this.getToken()}` }
    })
    .then(response => {
      console.log(response)
      return response.data
    })
    .catch(err => {
      console.log(err)
    })
}

export const createThread = newItem => {
    return axios
      .post('http://127.0.0.1:5000/items/create', {
      item_description: newItem.item_description,
      average_price: newItem.average_price,
      item_name: newItem.item_name,    
      item_history: newItem.average_price,
      image_url: newItem.image_url,
      user_ID: 1
      })
      .then(response => {
        console.log('Created.')
      })
  }