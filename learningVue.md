
<h3>Rendering in Vue</h3>

#

```html
<div id="counter">
    <div v-bind:style="{color: hasColor}"> test {{ card }}</div> 
</div>

<script>
    
    const Counter = { 
        data(){
            return{
                hasColor: "red",
                card: 10, 
            }
        }
    };
    Vue.createApp(Counter).mount('#counter');
</script>
``` 
<p>create a const Javascript Object called called Counter with a data() function to be used by Vue. pass it to Vue.createApp() and mount it to the id tag set in html #counter</p>


