import React from 'react';
import {Link} from 'react-router-dom'
import './Search.css';
import example from '../Images/Example.PNG';

function Search() {

    const [thread1, setThread1] = React.useState({
        item: "Holographic Charizard",
        image: example,
        OP: "Lordeth Diego",
        collaborator: "TeylorSwish",
        date: "2020/10/30",
        latestPing: "2020/10/31"
    });
    const threads = [thread1, thread1, thread1, thread1];

    const sorts = ["Popular", "Newest", "Alphabetical"];
    const [sorting, setSorting] = React.useState(sorts[0]);
    

    return (
        <div className="Search">
            <h1><span>Sorting by: <i>{sorting}</i></span></h1>

            {/* This part sets the buttons that change the sorting method.
            ... It doesn't actually sort anything yet though. */}
            <table style={{marginLeft:"200px"}}><tr>
                {sorts.map((sort) => (
                    <th><button onClick={() => setSorting(sort)} className="Sorting">{sort}</button></th>
                ))}
            </tr></table>

                    {/* TODO: The search results. AKA everything down from this and
                    fixing the copy/pasted thread1 const */}
            <div className='threads-div'>

            {threads.map((thread) => (

                <table className='threads-table'><tr>
                <th><Link to='/item'><img src={thread.image} className="threadImage"></img></Link></th>
                <th><h2><b>{thread.item}</b></h2>
                <h2>By: <i>{thread.OP}</i></h2>
                <h2>On: <i>{thread.date}</i></h2></th>
                <th><h2>Latest Comment:</h2>
                <h2>{thread.collaborator} on <i>{thread.latestPing}</i></h2></th>    
                </tr></table>
            ))}
            </div>
            
        </div>
    )
}

export default Search;