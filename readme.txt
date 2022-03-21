El ejecutable genera un archivo llamado main.c, con los datos ingresados de manera manual o automática del trabajo práctico, el cual poseerá una estructura similar a la siguiente:

#include <stdio.h>
#include <stdlib.h>

void clrscr() {
    system("@cls||clear");
}


//---------Problemas Secuenciales---------

//1. Suponga que un individuo desea invertir su capital en un banco y desea saber cuánto dinero ganará después de un mes si el banco paga a razón de 2% mensual.
int Ejercicio1() {
    
}

//2. Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuánto deberá pagar finalmente por su compra.
int Ejercicio2() {
    
}

//3. Un maestro desea saber qué porcentaje de hombres y que porcentaje de mujeres hay en un grupo de estudiantes.
int Ejercicio3() {
    
}

//---------Problemas Condicionales Selectivos Simples---------

//1. Determinar si un alumno aprueba a reprueba un curso, sabiendo que aprobara si su promedio de tres calificaciones es mayor o igual a 7; reprueba en caso contrario.
int Ejercicio4() {
    
}

//2. En un almacén se hace un 20% de descuento a los clientes cuya compra supere los $5000 ¿Cuál será la cantidad que pagara una persona por su compra?
int Ejercicio5() {
    
}

//3. Un obrero necesita calcular su salario semanal, el cual se obtiene de la sig. manera: Si trabaja 40 horas o menos se le paga $300 por hora Si trabaja más de 40 horas se le paga $300 por cada una de las primeras 40 horas y $400 por cada hora extra.
int Ejercicio6() {
    
}

//4. Desarrolle un algoritmo que lea dos números y los imprima en forma ascendente
int Ejercicio7() {
    
}

//5. Hacer un algoritmo que calcule el total a pagar por la compra de camisas. Si se compran tres camisas o más se aplica un descuento del 20% sobre el total de la compra y si son menos de tres camisas un descuento del 10%
int Ejercicio8() {
    
}

//---------Problemas Condicionales Selectivos Compuestos (si anidados o en cascada)---------

//1. Leer 2 números; si son iguales que los multiplique, si el primero es mayor que el segundo que los reste y si no que los sume.
int Ejercicio9() {
    
}

//2. Leer tres números diferentes e imprimir el número mayor de los tres.
int Ejercicio10() {
    
}

//---------Problemas con repeticiones---------

//1. Calcular el promedio de un alumno que tiene 7 calificaciones en la materia de Programación 1
int Ejercicio11() {
    
}

//2. Leer 10 números y obtener su cubo y su cuarta.
int Ejercicio12() {
    
}

//3. Leer 10 números e imprimir solamente los números positivos
int Ejercicio13() {
    
}

//4. Leer 15 números negativos y convertirlos en positivos e imprimir dichos números.
int Ejercicio14() {
    
}

//5. Suponga que se tiene un conjunto de calificaciones de un grupo de 40 alumnos. Realizar un algoritmo para calcular la calificación promedio y la calificación más baja de todo el grupo.
int Ejercicio15() {
    
}

//6. Calcular e imprimir la tabla de multiplicar de un número cualquiera. Imprimir el multiplicando, el multiplicador y el producto.
int Ejercicio16() {
    
}



int main() {
    int s = 0;
    int a;
    while(1 > 0) {
        clrscr();        
        printf("\n--------------Problemas Secuenciales--------------\n\n[1] Ejercicio 1\n[2] Ejercicio 2\n[3] Ejercicio 3\n\n--------------Problemas Condicionales Selectivos Simples--------------\n\n[4] Ejercicio 1\n[5] Ejercicio 2\n[6] Ejercicio 3\n[7] Ejercicio 4\n[8] Ejercicio 5\n\n--------------Problemas Condicionales Selectivos Compuestos (si anidados o en cascada)--------------\n\n[9] Ejercicio 1\n[10] Ejercicio 2\n\n--------------Problemas con repeticiones--------------\n\n[11] Ejercicio 1\n[12] Ejercicio 2\n[13] Ejercicio 3\n[14] Ejercicio 4\n[15] Ejercicio 5\n[16] Ejercicio 6\n");
        printf("\nSeleccione un ejercicio: ");
        scanf("%d", &s);
        switch (s) {
            case 1:
                Ejercicio1();
                break;
            case 2:
                Ejercicio2();
                break;
            case 3:
                Ejercicio3();
                break;
            case 4:
                Ejercicio4();
                break;
            case 5:
                Ejercicio5();
                break;
            case 6:
                Ejercicio6();
                break;
            case 7:
                Ejercicio7();
                break;
            case 8:
                Ejercicio8();
                break;
            case 9:
                Ejercicio9();
                break;
            case 10:
                Ejercicio10();
                break;
            case 11:
                Ejercicio11();
                break;
            case 12:
                Ejercicio12();
                break;
            case 13:
                Ejercicio13();
                break;
            case 14:
                Ejercicio14();
                break;
            case 15:
                Ejercicio15();
                break;
            case 16:
                Ejercicio16();
                break;
            default:
                printf("ejercicio fuera de rango");
                break;
        }
        printf("\n----------\n\n");
        printf("Introduzca 1 para continuar o 0 para cerrar: ");
        scanf("%d", &a);
        if (a == 0) {
            break;
        }
        printf("\n----------\n\n");
    }
    return 0;
}

Esto genera un menú donde se puede seleccionar que ejercicio ejecutar de manera cómoda y tambien permite al alumno no tener que encerrar funciones en comentarios, facilitando así la realización, la cual sería en una función por cada ejercicio, y también facilita la revisión de las mismas.

El menú se vería de la siguiente manera y se ejecutaría en bucle hasta que se solicite que se cierre:

Trabajo Practico 1


--------------Problemas Secuenciales--------------

[1] Ejercicio 1
[2] Ejercicio 2
[3] Ejercicio 3

--------------Problemas Condicionales Selectivos Simples--------------

[4] Ejercicio 1
[5] Ejercicio 2
[6] Ejercicio 3
[7] Ejercicio 4
[8] Ejercicio 5

--------------Problemas Condicionales Selectivos Compuestos (si anidados o en cascada)--------------

[9] Ejercicio 1
[10] Ejercicio 2

--------------Problemas con repeticiones--------------

[11] Ejercicio 1
[12] Ejercicio 2
[13] Ejercicio 3
[14] Ejercicio 4
[15] Ejercicio 5
[16] Ejercicio 6

Seleccione un ejercicio:
