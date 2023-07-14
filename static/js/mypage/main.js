
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
            console.log(response);
            console.log(response.json());
            console.log(JSON.stringify(response));
            console.log(JSON.stringify(response.json()));
        }); 
    }

}

window.onload = ()=>{

    new Main();
}