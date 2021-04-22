
<h3>Rendering in Vue</h3>

#

```html
<div id="counter">
    <div v-bind:style="{color: hasColor}"> test {{ card }}</div> 
</div>

<script>
    
    const RootComponent = { 
        data(){
            return{
                hasColor: "red",
                card: 10, 
            }
        }
    };
    const app = Vue.createApp(RootComponent)
    const vm = app.mount('#counter');
    console.log(Counter.data());
</script>
``` 
<p>create a const Javascript Object called called Counter with a data() function to be used by Vue. pass it to Vue.createApp() and mount it to the id tag set in html #counter</p>
<p>v-bind: can bind to any html attribute, style,src, title</p>

<h3>Components in Vue</h3>

#
https://v3.vuejs.org/guide/instance.html#creating-an-application-instance

````js
const RootComponent = {
  /* A JS object containing 
  options, data() function, for use by createApp  */
}
const app = Vue.createApp(RootComponent)
const vm = app.mount('#app')
````
mount is a Proxy handler for mutable data that will update the real html tag
<img src="https://i.imgur.com/vPGwOum.png">
