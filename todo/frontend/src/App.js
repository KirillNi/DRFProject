import React from 'react'
// import './App.css'
import axios from 'axios'
import {BrowserRouter, Route, Link, Routes} from 'react-router-dom'
import UserList from './components/User.js'
import TodoList from './components/ToDos.js'
import ProjectList from './components/Projects.js'
import LoginForm from './components/Auth.js'
import Cookies from 'universal-cookie'



class App extends React.Component {

   constructor(props) {
       super(props)
       this.state = {
           'users': [],
           'todos': [],
           'projects': [],
           'token': ''
       }
   }

   set_token(token) {
       const cookies = new Cookies()
       cookies.set('token', token)
       this.setState({'token': token})
   }

   is_authenticated() {
        return this.state.token !== ''
   }

    logout() {
        this.set_token('')
    }

    get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token})
    }

    get_token(username, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username, password: password})
            .then(response => {
                this.set_token(response.data['token'])
        }).catch(error => alert('Неверный логин или пароль'))
    }



   load_data() {
       axios.get('http://127.0.0.1:8000/api/users/')
           .then(response => {
                this.setState({users: response.data})
            }).catch(error => console.log(error))

       axios.get('http://127.0.0.1:8000/api/todos/')
           .then(response => {
                this.setState({todos: response.data})
            }).catch(error => console.log(error))

       axios.get('http://127.0.0.1:8000/api/projects/')
           .then(response => {
                this.setState({projects: response.data})
            }).catch(error => console.log(error))
   }

   componentDidMount() {
        this.get_token_from_storage()
        this.load_data()
   }

   render () {
       return (
           <div className="App">
               <BrowserRouter>
                    <nav>
                        <ul>
                            <li>
                                <Link to='/'>Users</Link>
                            </li>
                            <li>
                                <Link to='/todos'>ToDos</Link>
                            </li>
                            <li>
                                <Link to='/projects'>Projects</Link>
                            </li>
                            <li>
                                {this.is_authenticated() ? <button onClick={()=>this.logout()}>
                                    Logout</button> : <Link to='/login'>Login</Link>}
                            </li>
                        </ul>
                    </nav>
                    <Routes>
                        <Route exact path='/' element={<UserList items={this.state.users} />} />
                        <Route exact path='/todos' element={<TodoList items={this.state.todos} />} />
                        <Route exact path='/projects' element={<ProjectList items={this.state.projects} />} />
                        <Route exact path='/login' element={<LoginForm
                            get_token={(username, password) => this.get_token(username, password)} />} />
                        <Route component={NotFound404} />
                    </Routes>
               </BrowserRouter>
           </div>
       )
   }
}


const NotFound404 = ({ location }) => {
    return (
        <div>
            <h1>Страница по адресу '{location.pathname}' не найдена</h1>
        </div>
    )
}


export default App;

