<template>
<div>
    <img :src="imagen" alt="fondo">

    <div class="indecision-container">
        <input v-model="pregunta" type="text" placeholder="Hazme una pregunta">
        <p>Recuerda terminar con un signo de interrogacion (?)</p>
        <div>
            <h2> Hola mundo </h2>
            <h1> {{respuesta}} </h1>
            <h1> cosa 1 </h1>
        </div>
    </div>
</div>

</template>
<script>
export default {
    name: 'Indecision',
    data(){
        return{
            pregunta: 'Soy precioso?',
            respuesta: null,
            imagen: null
        }
    },
    methods: {
        async obtenerRespuesta(){
            this.respuesta = 'Pensando...'
            const {answer, image} = await fetch("https://yesno.wtf/api")
            .then(respuesta => respuesta.json() )
            this.respuesta = answer
            this.imagen = image
        }
    },
    watch: {
        pregunta(value, oldValue){
            if (value.includes('?')) 
            return this.obtenerRespuesta()
        }
    }

}
</script>

<style lang="sass">
    *
        margin: 0
        padding: 0
        box-sizing: border-box
        transition: .5s
    
    img
        height: 100vh
        max-width: 100%
        max-height: 100%
        position: fixed
        width: 100vw

    .indecision-container
        position: relative
        z-index: 99
        display: flex
        justify-content: center
        align-items: center
        flex-direction: column
        background: rgba(0, 0, 0, .3)
        height: 100vh

    input
        border: none
        padding: 1rem
        width: 50%
        border-radius: 15px
        font-size: 20px
        color: #565656
        outline: none
    
    p
        margin: 2%
        color: red
        font-size: 25px
        font-weight: bold
            
</style>