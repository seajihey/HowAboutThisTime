import { Sidebar } from './sidebar.js';
import { Table } from './table.js';

class Main{
    constructor(){
        const sidebar = new Sidebar();
        const table = new Table();
    }
}

window.onload = ()=>{

    new Main();
}