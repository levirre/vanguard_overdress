//deck_hash.js

//const deck = require('./D-SD01.json');
const fs = require('fs');
data = fs.readFileSync('./D-BT01.json');
let deck = JSON.parse(data);
console.log(deck);
//console.log(deck);
card = deck.cards[0].id


var vm = new Vue({
  el: '#counter',
  data: {
    StyleObj:{
      color: 'red'
    }
  }
});
//Vue.createApp(Counter).mount('#counter')
