import React from 'react'
import './App.css'
import {HashRouter, Route, Link, Switch} from 'react-router-dom'
import UserList from './components/User.js'
import TodoList from './components/ToDos.js'
import ProjectList from './components/Projects.js'
import axios from 'axios'


class App extends React.Component {

   constructor(props) {
       super(props)
       this.state = {
           'users': [],
           'todos': [],
           'projects': []
       }
   }

   componentDidMount() {
       axios.get('http://127.0.0.1:8000/api/users/')
           .then(response => {
               const users = response.data
                   this.setState(
                   {
                       'users': users
                   }
               )
           }).catch(error => console.log(error))
       axios.get('http://127.0.0.1:8000/api/todos/')
           .then(response => {
               const todos = response.data
                   this.setState(
                   {
                       'todos': todos
                   }
               )
           }).catch(error => console.log(error))
       axios.get('http://127.0.0.1:8000/api/projects/')
           .then(response => {
               const projects = response.data
                   this.setState(
                   {
                       'projects': projects
                   }
               )
           }).catch(error => console.log(error))
   }


   render () {
       return (
           <div className="App">
               <HashRouter>
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
                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path='/' component={() => <UserList items={this.state.users} />} />
                        <Route exact path='/todos' component={() => <TodoList items={this.state.todos} />} />
                        <Route exact path='/projects' component={() => <ProjectList items={this.state.projects} />} />
                        <Route component={NotFound404} />
                    </Switch>
               </HashRouter>
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

