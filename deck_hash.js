//deck_hash.js

//const deck = require('./D-SD01.json');
const fs = require('fs');
data = fs.readFileSync('./D-BT01.json');
let deck = JSON.parse(data);
img = 'img/D-BT01/' + deck.cards[0].id + '.png'
//import * as url from img

console.log(img);
const Counter = {
    data(){
        return{
            hasColor: "red",
            counter: 10,
            fontSize: 30,
            card: img
            
            
        }
    }
};
const app = Vue.createApp(Counter)
const vm = app.mount('#counter');


//Vue.createApp(Counter).mount('#counter')
