<template>
  <section id="padre">
      <img id="animacion" src="https://media.baamboozle.com/uploads/images/41563/1600663080_846368" alt="">
      <section id="caja-servicios">
          <h1>Servicios</h1>
            <ul id="lista">
                <li v-for="servicio in servicios" :key="servicio" :class="{ activo : servicio.activo }" @click="activar_desactivar(servicio)">{{servicio.nombre}} <span>{{servicio.precio}}</span>€</li>
            </ul>
            <div id="total">
                <h3>Total <span>{{calcularTotal()}}</span></h3>
            </div>
            
      </section>
  </section>
</template>

<script>
export default {
    name: 'Servicios',
    data(){
        return{
            servicios: [
                {
                    nombre: 'Desarrollo Web',
                    precio: 300,
                    activo: false
                },
                {
                    nombre: 'Diseño Web',
                    precio: 400,
                    activo: false
                },
                {
                    nombre: 'Integración',
                    precio: 250,
                    activo: false
                },
                {
                    nombre: 'Clases particulares',
                    precio: 220,
                    activo: false
                }
            ]
        }
    },
    methods:{
        activar_desactivar(servicio){
            servicio.activo = !servicio.activo
        },
        calcularTotal(){
            let total = 0
            for ( let i = 0;  i < this.servicios.length; i++ ){
                if ( this.servicios[i].activo === true ){
                    total += this.servicios[i].precio
                }
            }
            return total
        }
    }
}
</script>

<style lang="sass">
    @mixin flexbox
        display: flex
        justify-content: center
        align-items: center
    *
        margin: 0
        padding: 0
        box-sizing: border-box
        font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif
        color: white
    
    #padre
        background: url('http://www.tubodegahermosillo.com/images/gallery/desktop.jpg')
        background-repeat: no-repeat
        background-size: cover
        height: 100vh
        @include flexbox
        flex-direction: column
        h1
            font-size: 5rem
    
    #caja-servicios
        padding: 1rem
        width: 70%
        @include flexbox
        flex-direction: column
        background: #2b21717a
        border-radius: 15px
    #lista
        list-style: none
        font-size: 2rem
        padding: 1rem
        width: 50%
        @include flexbox
        flex-direction: column
        background: #ffffff21
        box-shadow: 1px 1px 5px black
        border-radius: 15px
        li
            margin: 1rem
            padding: .5rem 1rem
            width: 70%
            float: left
            background: #7331569c
            border-radius: 15px
            cursor: pointer
            span
                float: right
    .activo
        background: #00800096 !important
    
    #total
        width: 50%
        border-radius: 15px
        padding: 1rem
        font-size: 1.3rem

        h3
            float: left
            width: 100%
            span
                float: right
    #animacion
        width: 14%
        position: absolute
        top: 11%
        left: 15%
</style>