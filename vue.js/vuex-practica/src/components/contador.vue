<template>
  <div>
     

    
      <h1>{{nombre}}</h1>
     <h1>{{count}}</h1>

     <button v-on:click="sumarnumero()">sumar</button>

  </div>

</template>

<script>

import {mapMutations} from "vuex"
import {mapState} from "vuex"

export default {
  name: 'App',
  components: {

  },

  computed:{
    ...mapMutations(["sumar"]),
    ...mapState(["count","nombre"])

  },


  methods:{

    sumarnumero(){
      this.$store.commit("sumar")
    },

  },
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@1,300;1,400&display=swap');

#app{
    justify-content: center;
    align-items: center;
    text-align: center;
    font-family: 'Open Sans', sans-serif;
}

button{
  width: 20%;
  padding: 8px 30px;
  border: none;
  background-color: aqua;
  cursor: pointer;
  backdrop-filter: 2px;
}

</style>
