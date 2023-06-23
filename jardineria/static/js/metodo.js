//función que valida un formulario a través de JqueryValidate
$(function(){
    $("#mi-formulario").validate({
        rules:{
            nom:{
                required:true
            },
            ape:{
                required:true
            },
            fono:{
                required:true,
                number:true
            },
            correo:{
                required:true,
                email:true
            },
            fecha:{
                required:true
            },
            pass:{
                required:true
            },
            pass2:{
                required:true,
                equalTo:pass
            }

        },//rules
        messages:{
            nom:{
                required: 'Ingrese nombre',
                minlength: 'Caracteres insuficientes (6)'
            },
            ape:{
                required: 'Ingrese apellido',
                minlength: 'Caracteres insuficientes (10)'
            },
            fono:{
                required: 'Ingrese teléfono',
                minlength: 'Cantidad de digitos insuficientes (9)'
            },
            correo:{
                required: 'Ingrese correo de usuario',
                email: 'Formato de correo inválido'
            },
            fecha:{
                required: 'Seleccione una fecha válida',
                min: 'Fecha no corresponde'
            },
            pass:{
                required: 'Ingrese contraseña',
                minlength: 'Caracteres insuficientes (8)'
            },
            pass2:{
                required: 'Ingrese una contraseña',
                minlength: 'Caracteres insuficientes (8)',
                equalTo: 'Contraseñas no coinciden'
            },
        },//messages
    })//validate

})//function