let inputs = document.querySelectorAll(".boton")
        let arrayinputs=Array.from(inputs)
        let valorpatron=document.getElementById("valorpatron")

        const btncmp=document.getElementById("botoncomprobar")
        btncmp.addEventListener('click',()=>{
            let patron=[];
            arrayinputs.forEach(elemento=>{
                if (elemento.checked){
                patron.push(1) 
                }else{
                    patron.push(0)
                }
            })
            valorpatron.value=patron
            console.log(valorpatron.value)
        })