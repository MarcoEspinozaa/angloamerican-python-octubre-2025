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
const rol = 'director';

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
/* objetos */
const persona = {nombre: 'marco', edad: 34};

for (let i=0; i < 3; i++) {
    /*console.log(i)*/
}

let i = 0
while(i<2) {
    console.log(i);
    i++;
}

let condicion = true /* bandera */ 
while(condicion) {
    
}





