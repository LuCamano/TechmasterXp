
(() => {
    'use strict'

    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    const forms = document.querySelectorAll('.needs-validation')

    // Loop over them and prevent submission
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
                if (!form.checkValidity()) {
                    event.preventDefault()
                    event.stopPropagation()
                }
                form.classList.add('was-validated')
            }, false)
    })
    })()

$('#password1').after("<div class='invalid-feedback' id='clave1inv'>Debe ingresar una contraseña</div>");
$('#password2').after("<div class='invalid-feedback' id='clave2inv'>Las contraseñas no coinciden</div>");
$('#rut').after("<div class='invalid-feedback' id='rutinv'>RUT inválido</div>");
$('#correo').after("<div class='invalid-feedback' id='emailinv'>Debe ingresar un correo electrónico</div>");
$('#nombre').after("<div class='invalid-feedback' id='nombreinv'>Debe ingresar un nombre</div>");
$('#apellido').after("<div class='invalid-feedback' id='apellidoinv'>Debe ingresar un apellido</div>");
$('#telefono').after("<div class='invalid-feedback' id='telefonoinv'>Debe ingresar un teléfono</div>");
$('#direccion').after("<div class='invalid-feedback' id='direccioninv'>Debe ingresar una dirección</div>");

function validar_clave(){
    const clave1 = $("#password1")[0];
    const mayus = /[A-Z]/.test(clave1.value);
    const minus = /[a-z]/.test(clave1.value);
    const num = /[0-9]/.test(clave1.value);
    const special = /[^A-Za-z0-9]/.test(clave1.value);
    const length = clave1.value.length >= 8;
    if (!mayus) {
        clave1.setCustomValidity('Debe ingresar al menos una mayúscula');
        $("#clave1inv").text("Debe ingresar al menos una mayúscula");
    } else if (!minus) {
        clave1.setCustomValidity('Debe ingresar al menos una minúscula');
        $("#clave1inv").text("Debe ingresar al menos una minúscula");
    } else if (!num) {
        clave1.setCustomValidity('Debe ingresar al menos un número');
        $("#clave1inv").text("Debe ingresar al menos un número");
    } else if (!special) {
        clave1.setCustomValidity('Debe ingresar al menos un caracter especial');
        $("#clave1inv").text("Debe ingresar al menos un caracter especial");
    } else if (!length) {
        clave1.setCustomValidity('La contraseña debe tener al menos 8 caracteres');
        $("#clave1inv").text("La contraseña debe tener al menos 8 caracteres");
    }

    if (mayus && minus && num && special && length) {
        clave1.setCustomValidity('');
    }
};

function validar_passwords(){
    const clave1 = $("#password1")[0];
    const clave2 = $("#password2")[0];

    if(clave1.value != clave2.value){
        clave2.setCustomValidity('Las contraseñas no coinciden');
        console.log("Las contraseñas no coinciden");
    } else {
        clave2.setCustomValidity('');
        console.log("Las contraseñas coinciden");
    }
};

$("#password1").on( "input", function () {
    validar_clave();
    validar_passwords();
});

$("#password2").on( "input", validar_passwords);

$('#rut').on( "input", function () {
    let rut = $("#rut")[0];
    checkRut(rut);
});


function checkRut(rut) {
    // Despejar Puntos
    let valor = rut.value.replace(".", "");
    // Despejar Guión
    valor = valor.replace("-", "");
    
    valor = valor.replace(/[^0-9kK]/, '');

    // Aislar Cuerpo y Dígito Verificador
    cuerpo = valor.slice(0, -1);
    dv = valor.slice(-1).toUpperCase();
  
    // Formatear RUN

    rut.value = cuerpo + dv;
  
    // Si no cumple con el mínimo ej. (n.nnn.nnn)
    if (cuerpo.length < 7) {
      rut.setCustomValidity("RUT Incompleto");
      return false;
    } else if (cuerpo.length > 8) {
      rut.setCustomValidity("RUT Inválido");
      return false;
    }
  
    // Calcular Dígito Verificador
    suma = 0;
    multiplo = 2;
  
    // Para cada dígito del Cuerpo
    for (i = 1; i <= cuerpo.length; i++) {
      // Obtener su Producto con el Múltiplo Correspondiente
      index = multiplo * valor.charAt(cuerpo.length - i);
  
      // Sumar al Contador General
      suma = suma + index;
  
      // Consolidar Múltiplo dentro del rango [2,7]
      if (multiplo < 7) {
        multiplo = multiplo + 1;
      } else {
        multiplo = 2;
      }
    }
  
    // Calcular Dígito Verificador en base al Módulo 11
    dvEsperado = 11 - (suma % 11);
  
    // Casos Especiales (0 y K)
    dv = dv == "K" ? 10 : dv;
    dv = dv == 0 ? 11 : dv;
  
    // Validar que el Cuerpo coincide con su Dígito Verificador
    if (dvEsperado != dv) {
      rut.setCustomValidity("RUT Inválido");
      return false;
    }
  
    // Si todo sale bien, eliminar errores (decretar que es válido)
    rut.setCustomValidity("");
};

function validar_email(){
    const email = $("#correo")[0];
    const email_regex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    if (!email_regex.test(email.value)) {
        email.setCustomValidity('Email inválido');
        $("#emailinv").text("Email inválido");
    } else {
        email.setCustomValidity('');
    }
    if (email.value == "") {
        $("#emailinv").text("Debe ingresar un correo electrónico");
    }
};

function validarTexto(texto, msgerror, textoError){
    txt = texto.value;
    if (txt.length < 3) {
        texto.setCustomValidity('Debe ingresar al menos 3 caracteres');
        msgerror.text("Debe ingresar al menos 3 caracteres");
    } else {
        texto.setCustomValidity('');
    }
    if (txt == "") {
        msgerror.text(textoError);
    };
};

$('#correo').on('input', validar_email);

$('#nombre').on('input', function () {
    const nombre = $("#nombre")[0];
    const nombreinv = $("#nombreinv");
    const txtError = "Debe ingresar un nombre";
    validarTexto(nombre, nombreinv, txtError);
});

$('#apellido').on('input', function () {
    const apellido = $("#apellido")[0];
    const apellidoinv = $("#apellidoinv");
    const txtError = "Debe ingresar un apellido";
    validarTexto(apellido, apellidoinv, txtError);
});

function validar_direccion(){
    const direccion = $("#direccion")[0];
    const direccioninv = $("#direccioninv");
    let txt = direccion.value;
    if (txt.length < 10) {
        direccion.setCustomValidity('Debe ingresar al menos 10 caracteres');
        direccioninv.text("Debe ingresar al menos 10 caracteres");
        return false;
    } else if (txt.split(" ").length < 2) {
        direccion.setCustomValidity('Debe ingresar una dirección válida');
        direccioninv.text("Debe ingresar una dirección válida");
        return false;
    } else if (!(/\d/.test(txt))) {
        direccion.setCustomValidity('Debe ingresar un número en la dirección');
        direccioninv.text("Debe ingresar un número en la dirección");
        return false;
    } else if (!(/[a-zA-Z]/.test(txt))) {
        direccion.setCustomValidity('Debe ingresar una dirección válida');
        direccioninv.text("Debe ingresar una dirección válida");
        return false;
    }
    direccion.setCustomValidity('');
}

$('#direccion').on('input', validar_direccion);
$('#direccion').on('click', validar_direccion);

$('#rutPerfil').attr('disabled', true);

function aumentarCantidadCarrito(id){
    let identificador = id.slice(-1);
    let input = $("#cant-elem-carrito-"+identificador)[0];
    let valor = parseInt(input.value);
    let nuevovalor = Math.min(valor + 1, 10);
    input.value = nuevovalor;
};

function disminuirCantidadCarrito(id){
    let identificador = id.slice(-1);
    let input = $("#cant-elem-carrito-"+identificador)[0];
    let valor = parseInt(input.value);
    let nuevovalor = Math.max(valor - 1, 1);
    input.value = nuevovalor;
};

$(".incrementar-carrito").on('click', function () {
    let id = this.id;
    aumentarCantidadCarrito(id);
});

$(".decrementar-carrito").on('click', function () {
    let id = this.id;
    disminuirCantidadCarrito(id);
});

function aumentarCantidadProducto(){
    let input = $("#cantidad")[0];
    let valor = parseInt(input.value);
    let nuevovalor = Math.min(valor + 1, 10);
    input.value = nuevovalor;
};

function disminuirCantidadProducto(){
    let input = $("#cantidad")[0];
    let valor = parseInt(input.value);
    let nuevovalor = Math.max(valor - 1, 1);
    input.value = nuevovalor;
};