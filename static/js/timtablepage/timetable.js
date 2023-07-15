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

//시간표
getdata()
    fetch('')
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

// time
getdata();

function getdata() {
  fetch('')
    .then((response) => {
      return response.json(); 
    })
    .then(json => {
      console.log(json); 
      let a = json.name;

      let timetable = {
        "mon": {
          "1": ["tjsgh531", "user1"] 
        }
      };

      if (timetable["mon"]["1"].length >= 2) {
        let mon1Elements = document.querySelectorAll('.mon_1');
        mon1Elements.forEach(element => {
          element.style.backgroundColor = '#164DCA';
        });
      }

      console.log(a); 
    });
}


