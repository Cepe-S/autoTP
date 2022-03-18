El ejecutable genera un archivo llamado main.c en la misma carpeta el cual poseera una estructura similar a la siguiente:

#include <\stdio.h>
#include <\stdlib.h>

void clrscr() {
    system("@cls||clear");
}


int Ejercicio1() {
    //consigna de If statements .1
}
int Ejercicio2() {
    //consigna de If statements .2
}
int Ejercicio3() {
    //consigna de If statements .3
}
int Ejercicio4() {
    //consigna de For loops .1
}
int Ejercicio5() {
    //consigna de For loops .2
}
int Ejercicio6() {
    //consigna de For loops .3
}
int Ejercicio7() {
    //consigna de Do loops .1
}
int Ejercicio8() {
    //consigna de Do loops .2
}
int Ejercicio9() {
    //consigna de Do loops .3
}
int Ejercicio10() {
    //consigna de Do loops .4
}


int main() {
    int s = 0;
    int a;
    while(1 > 0) {
        clrscr();        
printf("Trabajo Pr�ctico 1\n\n\n--------------If statements--------------\n\n1. Ejercicio 1\n2. Ejercicio 2\n3. Ejercicio 3\n\n--------------For loops--------------\n\n4. Ejercicio 1\n5. Ejercicio 2\n6. Ejercicio 3\n\n--------------Do loops--------------\n\n7. Ejercicio 1\n8. Ejercicio 2\n9. Ejercicio 3\n10. Ejercicio 4\n");
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