export class Table{
    constructor(){
        this.mytable =document.querySelector('.mytable');
        this.makeTable();
    }

    getData(){

    }
    
    makeTable(){
        this.mytable.appendChild(this.createDay());
        this.mytable.appendChild(this.createDay("월"));
        this.mytable.appendChild(this.createDay("화"));
        this.mytable.appendChild(this.createDay("수"));
        this.mytable.appendChild(this.createDay("목"));
        this.mytable.appendChild(this.createDay("금"));
        this.mytable.appendChild(this.createDay("토"));
        this.mytable.appendChild(this.createDay("일"));
        
        for(let i = 0; i < 16*7; i++){
            if(i % 7 == 0){
                this.mytable.appendChild(this.createTime((i/7)+9));
            }
            const newblock = this.createBlock(i);
            this.mytable.appendChild(newblock);
        }
    }

    createDay(str=""){
        const newDay = document.createElement('div');
        newDay.textContent = `${str}`;
        newDay.classList.add('table_day');
        if(str == "토"){
            newDay.style.color = "blue";
        }
        else if(str == "일"){
            newDay.style.color = "red";
        }

        return newDay;
    }

    createTime(num){
        const newTime = document.createElement("div");
        newTime.textContent = `${num}`;
        newTime.classList.add('table_time');

        return newTime;
    }

    createBlock(color = "white", id){
        const newBlock = document.createElement('div');
        newBlock.classList.add("table_block");
        newBlock.setAttribute("id", id);
        newBlock.textContent = `${id}`;
        newBlock.style.backgroundColor = `${color}`;

        return newBlock;
    }

}