<template>
  <div>
    <Menu/>
    <About/>
    <Productos/>
    <Cita/>
  </div>
</template>

<script>
import Menu from './components/Menu'
import About from './components/About'
import Productos from './components/Productos'
import Cita from './components/Cita'

export default {
  name: 'App',
  components: {
    Menu,
    About,
    Productos,
    Cita
  }
}
</script>

<style>
*{
  scroll-behavior: smooth;
}
</style>