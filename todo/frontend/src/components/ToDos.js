import React from 'react'


const TodoItem = ({item}) => {
    return (
        <tr>
            <td>
                {item.author.username}
            </td>
            <td>
                {item.text}
            </td>
            <td>
                {item.created_at}
            </td>
            <td>
                {item.updated_at}
            </td>
            <td>
                {item.project}
            </td>
        </tr>
    )
}


const TodoList = ({items}) => {
   return (
       <table>
           <th>
               Username
           </th>
           <th>
               Text
           </th>
           <th>
               Created at
           </th>
           <th>
               Updated at
           </th>
           <th>
               Project
           </th>
           {items.map((item) => <TodoItem item={item} />)}
       </table>
   )
}


export default TodoList
