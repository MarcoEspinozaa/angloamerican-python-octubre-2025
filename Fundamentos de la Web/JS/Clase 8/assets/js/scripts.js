const palabra1 = "marco";
const palabra2 = 'mundo';
const oracion = `hola ${palabra1}`;
typeof oracion;

console.log(oracion);
console.log(typeof oracion)

const numero1 = 34;
const numero2 = 34.2;

console.log(typeof numero1);
console.log(typeof numero2);

const booleano1 = true;
const booleano2 = false;

/* operadores */

let a = 13;
let b = 6;

let suma = a + b;
let multiplicacion = a * b;
let division = a / b;
let resta = a - b;
let potencia = a ** b;

let modulo = a % b;

/* 13 % 6 */

console.log(modulo);

/* operadores de comparacion */
console.log(2 == '2');
console.log(2 === '2'); /* comparación estricta */

3 > 2; /* true */
3 < 2; /* false */
3 >= 2; /* true */
3 <= 2; /* false */

let numero_primo = 19; /* snakecase */
let numeroPrimo = 19; /* camelCase */
let Numero = 19; /* no recomendado */
/* no ocupar tíldes ni ñ */

/* flujo de control - Condicionales */
const edad = 22;

if (edad < 18) {
    console.log("es menor a 18");
} else if (edad == 18)  {
    console.log("es igual a 18")
} else {
    console.log("es mayor a 18")
}

if ((edad % 2) == 0) { /* edad modulo 2 es cero? */
    console.log("el numero es par");
} else {
    console.log("el numero es impar")
}


/* flujo control switch-case */
const rol = 'auxiliar de aseo';

switch (rol) {
    case 'estudiante':
        console.log("la persona es un estudiante");
        break;
    case 'director':
        console.log("la persona es un director");
        break;
    case 'inspector':
        console.log("la persona es un inspector");
        break;
    case 'docente':
        console.log("la persona es un docente");
        break;
    default:
        console.log("la persona no tiene cargo");
        break;
}

/* arrays o listas */
const lista = [1,2,3,4,5,6];
lista[4] /* retorna 5, posición 4 */

/* objetos */
const persona = {nombre: 'marco', edad: 34};
persona['edad'] /* retorna la edad */

let i = 0
while(i<2) {
    /*console.log(i);*/
    i++;
}

/* for (inicio; condición; paso) {.....}*/
for (let i=0; i < 3; i++) {
    /*console.log(i)*/
}

for (let i=0; i < 10; i +=2) {
    /*console.log(i)*/
}

for (let i=4; i>0; i--) {
    /*console.log(i)*/
}

for (let i=6; i < 10; i++) {
    /*console.log(i)*/
}

/* el for permite continue y break */
for (let i=0; i<6; i++) {
    if (i == 2) {
        continue; /* se salta el 2 */
    }

    if(i == 4) {
        break; /* se termina el ciclo cuando i es 4 */
    }

    /*console.log(i)*/
}

const numeros = [10,20,30];

for (const numero of numeros) {
    console.log(numero)
}


/* Selectores */
// getElementById: busca por el ID y devuelve el elemento

const $titulo = document.getElementById('titulo');

/* querySelector: busca por selector CSS (clase, id, tag) retorna siempre el primer elemento que encuentre */

const boton = document.getElementById('btnSaludo');

/* Registramos un "escuchador" (listener) en un botón. 'click' es el tipo de evento; la función flecha es el callback */

//console.log(boton);

boton.addEventListener('click', () => {
    // funcion se va a ejecutar cuando el navegador detecte un click en el botón ($boton)
    const mensaje = "haciendo click en el botón saludar";

    console.log(mensaje);
});

/* input */
/* se escucha el evento input en el campo texto. */

const nombre = document.getElementById('txtNombre');
const salida = document.getElementById('salida');

/* el navegador pasa un objeto 'e' (evento) al callback */

console.log(salida)
nombre.addEventListener('input', (e) => {

    salida.textContent = `Escribiendo contenido directamente: ${e.target.value}`;
});







