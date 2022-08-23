import Indecision from '@/components/Indecision'
import { shallowMount } from '@vue/test-utils'

describe ('Indecision Component', () => {
    test('Debe averiguar que existe un elemento hmtl',() =>{
        const componente = shallowMount(Indecision)
        expect(componente.find('h1').exists()).toBeTruthy()
    })    
    test('Debe averiguar que h2 tiene el valor de hola mundo',() =>{
        const componente = shallowMount(Indecision)
        const valorh2 = componente.find('h2').text()//busca en mi componente indecision si hay un h2
        expect(valorh2).toBe("Hola mundo")//se espera que el valor sea hola mundo, si es asi pasará la prueba
    })
    test('Debe mostrar los h1',() =>{
        const componente = shallowMount(Indecision)
        const h1etiquetas = componente.findAll(h1)
        console.log(h1etiquetas)
        expect(h1etiquetas[1].text()).toBe("cosa 1")
    })    

    // test ('Debe hacer match con el snapshot', () => {
    //     const estructura = shallowMount(Indecision) //aqui hace la captura
    //     expect(estructura.html()).toMatchSnapshot() //aqui compara la captura con la que le pasan
    
    // })
})

// describe ('Indecision Component', () => {
//     test ('Debe tener el valor de la api', () => {
//         const estructura = shallowMount(Indecision) //aqui hace la captura
//         const h2 = estructura.find('h2') //aqui hace la captura
//         expect(h2.text()).toBe('Hola mundo')
//     })
// })