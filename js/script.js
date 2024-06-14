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
$('#tarjeta').after("<div class='invalid-feedback' id='err_nro_tarjeta'>Número de tarjeta inválido</div>");


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
    let input = $("#cantidad-producto")[0];
    let valor = parseInt(input.value);
    let nuevovalor = Math.min(valor + 1, 10);
    input.value = nuevovalor;
};

function disminuirCantidadProducto(){
    let input = $("#cantidad-producto")[0];
    let valor = parseInt(input.value);
    let nuevovalor = Math.max(valor - 1, 1);
    input.value = nuevovalor;
};

$("#boton-incrementar").on('click', aumentarCantidadProducto);
$("#boton-decrementar").on('click', disminuirCantidadProducto);


function validar_telefono(){
    const telefono = $("#telefono")[0];
    const telefonoinv = $("#telefonoinv");
    let txt = telefono.value;

    txt = txt.replace(/[^0-9]/, '');
    telefono.value = txt;

    if (txt.length < 9) {
        telefono.setCustomValidity('Debe ingresar al menos 9 caracteres');
        telefonoinv.text("Debe ingresar al menos 9 caracteres");
        return false;
    } else if (!(/^\d+$/.test(txt))) {
        telefono.setCustomValidity('Debe ingresar solo números');
        telefonoinv.text("Debe ingresar solo números");
        return false;
    }
    telefono.setCustomValidity('');
}

$("#telefono").on("input", validar_telefono);



function fValidarTarjeta(){
    codigo = $("#tarjeta").val().replace('-', '');
    input = $("#tarjeta")[0];
    error = $("#err_nro_tarjeta");
    VISA = /^4[0-9]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}$/;
    MASTERCARD = /^5[1-5][0-9]{2}-?[0-9]{4}-?[0-9]{4}-?[0-9]   {4}$/;
    AMEX = /^3[47][0-9-]{16}$/;
    CABAL = /^(6042|6043|6044|6045|6046|5896){4}[0-9]{12}$/;
    NARANJA =   /^(589562|402917|402918|527571|527572|0377798|0377799)[0-9]*$/;

    $("#err_nro_tarjeta").html("");
    if(luhn(codigo)){
        if(VISA.test(codigo)){
            input.setCustomValidity('');
        } else if(MASTERCARD.test(codigo)){
            input.setCustomValidity('');
        } else if(AMEX.test(codigo)){
            input.setCustomValidity('');
        } else if(CABAL.test(codigo)){
            input.setCustomValidity('');
        } else if(NARANJA.test(codigo)){
            input.setCustomValidity('');
        } else {
            input.setCustomValidity('Número de tarjeta inválido');
            error.text("Número de tarjeta inválido");
        }
    } else {
        input.setCustomValidity('Número de tarjeta inválido');
        error.text("Número de tarjeta inválido");
    }
}
function luhn(value) {
    // Accept only digits, dashes or spaces
    if (/[^0-9-\s]+/.test(value)) return false;
    // The Luhn Algorithm. It's so pretty.
    let nCheck = 0, bEven = false;
    value = value.replace(/\D/g, "");
    for (var n = value.length - 1; n >= 0; n--) {
        var cDigit = value.charAt(n),
        nDigit = parseInt(cDigit, 10);
        if (bEven && (nDigit *= 2) > 9) nDigit -= 9; nCheck +=  nDigit; bEven = !bEven;
    }
    return (nCheck % 10) == 0;
}

$("#tarjeta").on("input", fValidarTarjeta);


$("#boton-pagar").on("click", function () {
    document.getElementById("metodo-pago").dispatchEvent(new Event('submit'));
    document.getElementById("datos-facturacion").dispatchEvent(new Event('submit'));
});

$("#cvv").on("input", function () {
    input = this;
    valor = input.value;
    valor = valor.replace(/[^0-9]/, '');
    input.value = valor;
    if (valor.length < 3) {
        input.setCustomValidity('Debe ingresar al menos 3 caracteres');
    } else {
        input.setCustomValidity('');
    }
});

$("#fecha-expiracion").on("input", function () {
    let input = this;
    let valor = input.value;
    valor = valor.replace(/[^0-9]/, '');
    valor = valor.replace("`", '');
    input.value = valor;
    let fechaActual = new Date();
    let yearActual = fechaActual.getFullYear() - 2000;
    let mesActual = fechaActual.getMonth() + 1;
    let mes = "";
    let year = "";

    if (valor.length > 2){
        valor = valor.substring(0, 2) + "/" + valor.substring(2);
        input.value = valor;
        mes = valor.split("/")[0];
        year = valor.split("/")[1];
    }

    if (valor.length < 5) {
        input.setCustomValidity('Debe ingresar al menos 4 caracteres');
        return false;
    } else if (year < yearActual) {
        input.setCustomValidity('Año de expiración inválido');
        return false;
    } else if (mes < 1 || mes > 12) {
        input.setCustomValidity('Mes de expiración inválido');
        return false;
    } else if (year == yearActual && mes < mesActual) {
        input.setCustomValidity('Fecha de expiración inválida');
        return false;
    }
    input.setCustomValidity('');
});

// Función para actualizar el resumen de la compra
// const productos = [
//     { nombre: "Producto 1", precio: 10.00, cantidad: 2 },
//     { nombre: "Producto 2", precio: 15.00, cantidad: 1 },
//     { nombre: "Producto 3", precio: 5.00, cantidad: 3 }
// ];
// const cantidadProductos = document.getElementById("cantidad-productos");
// const total = document.getElementById("total");

// function actualizarResumen() {
//     let totalProductos = 0;
//     let totalPrecio = 0.00;

//     productos.forEach(producto => {
//         totalProductos += producto.cantidad;
//         totalPrecio += producto.precio * producto.cantidad;
//     });

//     cantidadProductos.textContent = totalProductos;
//     total.textContent = totalPrecio.toFixed(2);
// }

// actualizarResumen();


// Funcion para generar números de tarjeta de crédito de prueba
// function generateCardNumber(prefix, length) {
//     let cardNumber = prefix;
//     while (cardNumber.length < (length - 1)) {
//         cardNumber += Math.floor(Math.random() * 10);
//     }

//     // Calculate check digit using Luhn algorithm
//     let sum = 0;
//     let shouldDouble = true;
//     for (let i = cardNumber.length - 1; i >= 0; i--) {
//         let digit = parseInt(cardNumber.charAt(i));
//         if (shouldDouble) {
//             digit *= 2;
//             if (digit > 9) {
//                 digit -= 9;
//             }
//         }
//         sum += digit;
//         shouldDouble = !shouldDouble;
//     }
//     let checkDigit = (10 - (sum % 10)) % 10;
//     cardNumber += checkDigit.toString();

//     return cardNumber;
// }

var deleteModal = $('#deleteModal')[0];
    deleteModal.addEventListener('show.bs.modal', function (event) {
        var button = event.relatedTarget;
        var productId = button.getAttribute('data-id');
        var productName = button.getAttribute('data-name');
        
        var modalTitle = deleteModal.querySelector('.modal-title');
        var modalBodySpan = deleteModal.querySelector('.modal-body #productName');
        var deleteForm = deleteModal.querySelector('#deleteForm');
        var tipoObjeto = button.getAttribute('data-tipo');

        if (tipoObjeto == 'Usuario'){
            modalTitle.textContent = 'Eliminar usuario';
            deleteForm.action = '/delete-user/' + productId + '/';
        } else if (tipoObjeto == 'Producto'){
            modalTitle.textContent = 'Eliminar producto';
            deleteForm.action = '/delete-product/' + productId + '/';
        } else if (tipoObjeto == 'Marca'){
            modalTitle.textContent = 'Eliminar marca';
            deleteForm.action = '/delete-brand/' + productId + '/';
        }
        modalBodySpan.textContent = productName;
    });

var productsModal = $('#productsModal')[0];
    productsModal.addEventListener('show.bs.modal', function (event) {
        let boton = event.relatedTarget;
        let productos = JSON.parse(boton.getAttribute('data-products'));

        let modalBody = productsModal.querySelector('.modal-body');
        modalBody.textContent = "";

        productos.forEach(producto => {
            let p = document.createElement('p');
            p.textContent = producto["nombre"] + " x" + producto["cantidad"];
            modalBody.appendChild(p);
        });
    });