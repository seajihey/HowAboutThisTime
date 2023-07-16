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


// timetable
getdata();

function getdata() {
  fetch('URL')
    .then((response) => {
      return response.json(); 
    })
    .then(json => {
      console.log(json); 
      let a = json.name;

      let timetable = {
        "mon": {
          "1": ["user1", "user2", "user3"],
          "2": ["user4"],
          "3": [],
          "4": [],
          "5": [],
          "6": [],
          "7": [],
          "8": [],
          "9": [],
          "10": [],
          "11": [],
          "12": [],
          "13": [],
        },
        "tue": {
          "1": ["user1", "user2", "user3"],
          "2": ["user4"],
          "3": [],
          "4": [],
          "5": [],
          "6": [],
          "7": [],
          "8": [],
          "9": [],
          "10": [],
          "11": [],
          "12": [],
          "13": [],
        },
        "wed": {
          "1": ["user1", "user2", "user3"],
          "2": ["user4"],
          "3": [],
          "4": [],
          "5": [],
          "6": [],
          "7": [],
          "8": [],
          "9": [],
          "10": [],
          "11": [],
          "12": [],
          "13": [],
        },
        "thu": {
          "1": ["user1", "user2", "user3"],
          "2": ["user4"],
          "3": [],
          "4": [],
          "5": [],
          "6": [],
          "7": [],
          "8": [],
          "9": [],
          "10": [],
          "11": [],
          "12": [],
          "13": [],
        },
        "fri": {
          "1": ["user1", "user2", "user3"],
          "2": ["user4"],
          "3": [],
          "4": [],
          "5": [],
          "6": [],
          "7": [],
          "8": [],
          "9": [],
          "10": [],
          "11": [],
          "12": [],
          "13": [],
        },
        "sat": {
          "1": ["user1", "user2", "user3"],
          "2": ["user4"],
          "3": [],
          "4": [],
          "5": [],
          "6": [],
          "7": [],
          "8": [],
          "9": [],
          "10": [],
          "11": [],
          "12": [],
          "13": [],
        },
        "sun": {
          "1": ["user1", "user2", "user3"],
          "2": ["user4"],
          "3": [],
          "4": [],
          "5": [],
          "6": [],
          "7": [],
          "8": [],
          "9": [],
          "10": [],
          "11": [],
          "12": [],
          "13": [],
        },
        
      };

      for (let day in timetable) {
        for (let time in timetable[day]) {
          let count = timetable[day][time].length;
          
          if (count >= 3) {
            elements.forEach(element => {
              element.style.backgroundColor = '#164DCA';
            });
          } else if (count >= 2) {
            elements.forEach(element => {
              element.style.backgroundColor = '#BDC5FF';
            });
          } else if (count >= 1) {
            elements.forEach(element => {
              element.style.backgroundColor = '#F0EDFF';
            });
          }
        }
      }

      console.log(a); 
    });
}


const tableElement = document.querySelector('.table');
tableElement.style.overflowX = 'hidden';
tableElement.style.overflowY = 'auto';




