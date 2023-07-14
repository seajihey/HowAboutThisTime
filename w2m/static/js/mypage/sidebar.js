export class Sidebar{
    constructor(){
        this.side_items = document.querySelectorAll('.side_items');
        this.side_item_active = document.querySelector('.side_item_active');
        
        this.contents = document.querySelectorAll('.content');
        this.active_content = "group_list";
    
        this.sidebarClickEvent();
    }

    sidebarClickEvent(){
        this.side_items.forEach(ele => {
            ele.addEventListener('click', (e)=>{
                //side_bar css 변경 코드
                if(!e.target.classList.contains('side_item_active')){
                    this.side_item_active.classList.remove('side_item_active');
                    e.target.classList.add('side_item_active');
                    this.side_item_active = e.target;
        
                    this.active_content = e.target.dataset.content;
        
                    // content unactive 설정
                    this.contents.forEach(element => {
                        if(element.classList.contains(`${this.active_content}`)){                    
                            if(element.classList.contains('unactive')){
                                element.classList.remove('unactive');
                            }
                        }
        
                        else{
                            if(!element.classList.contains('unacitve')){
                                element.classList.add('unactive');
                            }
                        }
                    });
                }
            });
        });        
    }
}