<template>
  <div>
      <h1>¿Quién es este Pokemon?</h1>      
      <PokemonPicture :pokemonId="60" :showPokemon="true" />
      <PokemonOptions/>
  </div>
</template>

<script>
import PokemonOptions from '@/components/PokemonOptions'
import PokemonPicture from '@/components/PokemonPicture'
import getPokemonOptions from '@/helpers/getPokemonOptions';


export default {
  components: {PokemonOptions, PokemonPicture, getPokemonOptions}

}
</script>

<style>

</style>