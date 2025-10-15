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
const rol = 'inspector';

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
const persona = {
    nombre: 'marco', 
    edad: 34,
    direccion: 'wdfasdf',
};
persona['edad'] /* retorna la edad */

let i = 0
while(i<6) {
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

const titulo = document.getElementById('titulo');
const clases = document.getElementsByClassName('parrafo');
const ejemplo = document.getElementsByTagName('h1')

/*console.log(titulo)
console.log(clases)
console.log(ejemplo)*/

/* querySelector: busca por selector CSS, retorna siempre el primer elemento que encuentre. En palabras simples buscar el elemento tal cual lo hacen en CSS por ejemplo:  */

const ejemplo2 = document.querySelector('#salida');
const titulo2 = document.getElementById('titulo');

/*console.log(ejemplo2)*/


const boton = document.getElementById('btnSaludo');

/* Registramos un "escuchador" (listener) en un botón. 'click' es el tipo de evento; la función flecha es el callback */

//console.log(boton);

boton.addEventListener('click', () => {
    console.log("haciendo click en el botón saludar");
    alert("haciendo click al botón saludar.")
});

/* input */
/* se escucha el evento input en el campo texto. */

const contador = document.querySelector('#contador');

const contador2 = document.getElementById('contador');

console.log("contador con querySelector: ", contador)
console.log("contador con getElementById: " , contador2)

/* ===================== */
let cuenta = 0
const parrafo_contador = document.getElementById('cuenta');

console.log("parrafo contador: " , parrafo_contador)

contador.addEventListener('click', () => {
    cuenta ++;
    parrafo_contador.textContent = "Clicks: " + cuenta;
});
/* ====================== */

const nombre = document.getElementById('txtNombre');
const salida = document.getElementById('salida');

/* el navegador pasa un objeto 'e' (evento) al callback */

/*console.log(salida)*/
nombre.addEventListener('input', (e) => {
    console.log(e.target);

    salida.innerText = "Escribiendo contenido directamente: " + e.target.value;

    console.log("Escribiendo contenido directamente: " + e.target.value + " y mostrando en consola")
});


/* ============== */
const boton_color = document.getElementById('boton_color');
const parrafo_color = document.getElementById('parrafo_color');

console.log(boton_color);
console.log(parrafo_color)

boton_color.addEventListener('click', () => {
    parrafo_color.style.color = 'red';
    boton_color.style.display = 'none';
});
/* =============== */

const mouse_color = document.getElementById('mouse_color');

mouse_color.addEventListener('mouseenter', () => {
    console.log("detectando el evento")
    mouse_color.style.backgroundColor = 'blue';
});

mouse_color.addEventListener('mouseleave', () => {
    mouse_color.style.backgroundColor = '';
});




