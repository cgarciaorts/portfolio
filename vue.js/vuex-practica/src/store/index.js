import {createStore} from "vuex"


export default createStore({
    state:{
        count:1,
        nombre:"nico"
    },

    mutations:{
        sumar(state){

            state.count +=1
            state.nombre = "misco"

        }        
    }
})