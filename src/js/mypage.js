// side bar click event
const side_items = document.querySelectorAll('.side_items');
let side_item_active = document.querySelector('.side_item_active');

// content
const contents = document.querySelectorAll('.content');

let active_content = "group_list";

side_items.forEach(ele => {
    ele.addEventListener('click', (e)=>{
        //side_bar css 변경 코드
        if(!e.target.classList.contains('side_item_active')){
            side_item_active.classList.remove('side_item_active');
            e.target.classList.add('side_item_active');
            side_item_active = e.target;

            active_content=e.target.dataset.content;
    
            // content unactive 설정
            contents.forEach(element => {
                
                if(element.classList.contains(`${active_content}`)){                    
                    console.log(`활성화 : ${element}`);
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



