import Servicios from '@/components/Servicios'
import { shallowMount } from '@vue/test-utils'

describe ( 'Servicios Component', () => {
    test ( 'Debe hacer match con el snapshot', () => {
        const componente = shallowMount ( Servicios )
        expect ( componente.html() ).toMatchSnapshot()
    })

    test ( 'Deben haber cuatro servicios en la aplicación', () => {
        const componente = shallowMount ( Servicios )
        //console.log("Total de servicios: ", componente.findAll('li').length)
        expect ( componente.findAll('li').length ).toBe(4)
    })

    test ( 'El precio del tercer servicio debe ser 250', () => {
        const componente = shallowMount ( Servicios )
        const arrayItems = componente.findAll('span')
        console.log("Tipo elemento 3: ", typeof(arrayItems[2].text()))
        console.log("Elemento 3: ", arrayItems[2].text())
        expect ( arrayItems[2].text() ).toBe("250")
    })
})