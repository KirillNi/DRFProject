import React from 'react'


const UserItem = ({item}) => {
   return (
       <tr>
           <td>{item.username}</td>
           <td>{item.first_name}</td>
           <td>{item.last_name}</td>
           <td>{item.email}</td>
           <td>{item.birthday_year}</td>
       </tr>
   )
}


const UserList = ({items}) => {
    return (
        <table>
            <tr>
                <th>Username</th>
                <th>First name</th>
                <th>Last Name</th>
                <th>Email</th>
                <th>Birthday year</th>
            </tr>
            {items.map((item) => <UserItem item={item} />)}
        </table>
    )
}


export default UserList

