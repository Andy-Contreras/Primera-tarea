(async () => {
    const {value: pais} = await Swal. fire({
        title:"Bienvenido¡",
        text: "Selecciona tu pais de residencia",
        icon:'success',
        allowOutsideClick: false,
        input:'select',
        inputPlaceholder:"Pais",
        inputValue:'',
        inputOptions:{
            México: 'México',
            España: 'España',
            Alemania:'Alemania',
            Argentina:'Argentina',
            Australia:'Australia',
            Chile:'Chile',
            China:'China',
            Colombia:'Colombia',
            Cuba:'Cuba',
            Ecuador:'Ecuador',
            Mónaco:'Mónaco',
            Panamá:'Panamá',
            Perú:'Perú',
            Portugal:'Portugal',
            EstadosUnidos:'Estados Unidos',
        }
    });
    if (pais){
        Swal.fire({
            title:'Espero que te guste mi página web',
            allowOutsideClick: false,

        })
    }
})()
