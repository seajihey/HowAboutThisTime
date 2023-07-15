//room part item 새로 만드는 함수
function createRoomPartItem(num){
    const colorlist = ["#9A91EB", "#A8267E", "#FF4B21", "#FFBD37"];

    const item = document.createElement("div");
    item.classList.add("room_part_item");

    const user = document.createElement("div");
    user.classList.add("user");

    const image = new Image();
    image.src="../src/img/user.png";

    const name = document.createElement("div");
    name.classList.add("name");
    name.style.backgroundColor = colorlist[num % 4];

    user.appendChild(image);
    item.appendChild(user);
    item.appendChild(name);

    return item;
}

const room_part_items = document.querySelector('.room_part_items');

for(let i = 0; i < 5; i++){
    const item =  createRoomPartItem(i);
    room_part_items.appendChild(item);
}
