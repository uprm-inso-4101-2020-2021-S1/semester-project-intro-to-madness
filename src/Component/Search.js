import React, {useState, useEffect} from 'react';
import {Link} from 'react-router-dom'
import './Search.css';
import Example from '../Images/Example.PNG';

function Search() {

    // This gets all the threads from the storage.
    const [threads, setThreads] = useState([{}]);
    useEffect(()=> {
        fetch('/threads').then(
        response => response.json()
        ).then(data => setThreads(data.Thread))
    }, []);

    const updateThreads = (category) => {
        fetch('/threads/' + category).then(
            response => response.json()
            ).then(data => setThreads(data.Thread))
    }

    const [items, setItems] = useState([{}]);
    useEffect(()=> {
        fetch('/items').then(
          response => response.json()
        ).then(data => setItems(data.Item))
      }, []);

    const getItem = (threads) =>{
        var result = "NA";
        for(var item of items){
            if(item.ID == threads.item_id){
                result = item
            }
        }
        return(result)
    }

    const sorts = ["Purus Institute", "Ac Ipsum Associates", "Faucibus Company", "Phasellus LLP", "Aenean Corp."];
    const [sorting, setSorting] = useState(sorts[0]);

    return (
        <div className="Search">
            <h1><span>Sorting by: <i>{sorting}</i></span></h1>

            {/* This part sets the buttons that change the sorting method. */}
            <table style={{marginLeft:"200px"}}><tr>
                {sorts.map((sort) => (
                    <th><button onClick={() => setSorting(sort) & updateThreads(sort)} className="Sorting">{sort}</button></th>
                ))}
            </tr></table>

                    {/* The search results. */}
            <div className='threads-div'>

            {threads.map((thread) => (

                <table className='threads-table'><tr>
                <th><Link to={{
                    pathname: "/item",
                    search: getItem(thread).item_name,
                    state:{
                    item: getItem(thread).item_name,
                    image: getItem(thread).image_url,
                    price: getItem(thread).average_price,
                    description: getItem(thread).item_description,
                    history: getItem(thread).item_history
                }
                }}><img src={Example} className="threadImage" alt="Filler"/></Link></th>
                <th><h2><b>{getItem(thread).item_name}</b></h2>
                {/* <h2>By: <i>{users[1].username}</i></h2> */}
                <h2>On: <i>{thread.Date}</i></h2></th>
                </tr></table>
            ))}
            </div>
            
        </div>
    )
}

export default Search;