<template>
    <div id="productos" class="productos  min-h-screen mx-auto px-6 p-10">

        <h2 class="text-4xl font-bold text-center text-white mb-8 mt-28">NUESTROS PRODUCTOS</h2>
        <div class="flex items-center flex-wrap mb-6">
            <div class="w-full md:w-1/2">
                <h4 class="text-3x1 text-white font-bold mb-3">Ducati DesertX 2022</h4>
                <p class="text-white mb-8">Lorem, ipsum dolor sit amet consectetur adipisicing elit. Deleniti voluptate eum fuga sed reiciendis, accusamus ea consectetur natus, iste non reprehenderit perspiciatis distinctio? In maiores accusamus nostrum dolor iure animi!</p>
            </div>
            
            <div class="w-full md:w-1/2">
                <img src="http://assets.stickpng.com/images/580b585b2edbce24c47b2d04.png" alt="">
            </div>

            <div class="flex items-center flex-wrap mb-20">
                <div class="w-full md:w-1/2">
                    <img src="http://maskemotos.com/wp-content/uploads/2014/10/XS-125-MOTOCICLETA-NEGRA.png" alt="">
                </div>                
                <div class="w-full md:w-1/2">
                    <h4 class="text-3x1 text-white font-bold mb-3">Tiger 1200 Rally</h4>
                    <p class="text-white mb-8">Lorem ipsum, dolor sit amet consectetur adipisicing elit. Aliquam rem, magnam quasi suscipit enim laborum explicabo nostrum excepturi ut ducimus qui assumenda voluptatem. Quaerat dolores nisi neque aliquid velit. Omnis.</p>
                </div>                    
            </div>

            <div class="flex items-center flex-wrap mb-20">
                <div class="w-full md:w-1/2">
                    <h4 class="text-3x1 text-white font-bold mb-3">Super moto BSA</h4>
                    <p class="text-white mb-8">Lorem ipsum, dolor sit amet consectetur adipisicing elit. Aliquam rem, magnam quasi suscipit enim laborum explicabo nostrum excepturi ut ducimus qui assumenda voluptatem. Quaerat dolores nisi neque aliquid velit. Omnis.</p>
                </div>
                
                <div class="w-full md:w-1/2">
                    <img src="https://heromotored.com/wp-content/uploads/2020/10/moto-negra.png" alt="">
                </div>  

            </div>

        </div>
    </div>
</template>

<script>
export default {
    name: 'Productos'
}
</script>

<style>
    .productos{
        background: linear-gradient(90deg,#607eea 0%,#764ba2 100%);
    }
</style>