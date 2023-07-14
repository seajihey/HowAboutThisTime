
import { Sidebar } from './sidebar.js';
import { Table } from './table.js';

class Main{
    constructor(){
        const sidebar = new Sidebar();
        const table = new Table();
        this.getdata();
    }

    getdata(){
        fetch('http://127.0.0.1:8000/api/user/lmj__010129/')
        .then((response) =>{
            return response.json();
        }).then( json => {
            console.log(json);
            let a = json.name;

            let timetable = {"mon" :{
                "1" : ["tjsgh531"],
                "2" : ["tjsgh531"]
            }};

            console.log(timetable["mon"]["1"].length);

            console.log(a);
        }); 
    }

}

window.onload = ()=>{

    new Main();
}