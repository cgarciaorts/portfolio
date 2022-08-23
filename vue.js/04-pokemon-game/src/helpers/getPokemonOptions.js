import pokemonApi from "../api/pokemonApi"

const getPokemons = () => {

    const pokemonsArr = Array.from( Array(650) )

    return pokemonsArr.map( ( _ , index ) => index + 1)

}

const getPokemonOptions = () => {

    const mixedPokemons = getPokemons()
                            .sort( () => Math.random() - 0.5 )

    getPokemonNames( mixedPokemons.splice(0,4) )
}

const getPokemonNames = async ( [a,b,c,d] = []) => {

    const resp = await pokemonApi.get(`/1`)

    console.log(resp.data.name, resp.data.id)
    // const promiseArr = [
    //     pokemonApi.get(`/${a}`),
    //     pokemonApi.get(`/${b}`),
    //     pokemonApi.get(`/${c}`),
    //     pokemonApi.get(`/${d}`),
    // ]
    // const respuestas =  await Promise.all(arrPromises)
    // console.log(respuestas)
    // // console.log (a,b,c,d)

}

export default getPokemonOptions