<template>
  <nav>
      <div class="menu w-full mx-auto px-6 py-4 flex flex-col md:flex-row justify-between items-center fixed bg-white">
          <a href="" class="font-bold  text-2xl m-5 md:m-0 lg:text-4xl">
            <img class="w-10" src="https://th.bing.com/th/id/R.19a092d976276c5c41e075e62a576bb4?rik=ALeRlaAEvfqfyg&riu=http%3a%2f%2fclipart-library.com%2fimages_k%2fmotorcycle-racing-silhouette%2fmotorcycle-racing-silhouette-11.png&ehk=Xh5WOti6se9J484Tw0586K0xLsRHDk81naFTlvbkSKA%3d&risl=&pid=ImgRaw&r=0"

           alt="">
        </a>
          <ul class="inline-flex">
              <li><a class="px-4 font-bold" href="#about">¿Quienes Somos?</a></li>
              <li><a class="px-4 hover:text-gray-500" href="#productos">Productos</a></li>
              <li><a class="px-4 hover:text-gray-800" href="#cita">Cita Previa</a></li>
          </ul>
      </div>
  </nav>
</template>

<script>
export default {
    name:'Menu'
}
</script>

<style>
.menu{
    background: linear-gradient(180deg,white 0%,#9facea 100%);
    box-shadow: 0 1px 10px black;
}
</style>