//Import the library for text in terminal.
#include <stdio.h>
/*The main line is used to call a function and the int part refeers to
 the integer numbers, like float(for floating point numbers) and 
 char(for single characters, such as 'a' or 'B').*/
int main() {
    //printf means: print a function.
    printf("Hello World!\n");// And the \n character means that there will be a newline.
    printf("I am not a god.\n\n");// You can put any \n as you want.
    printf("First line.\nSecond line.\nThird line.\n\n");//Also you can put text between the \n character.
    //Apart from the \n character, you can put an horizontal tab with a \t.
    printf("\tHello there.\t\t\t\tI'm far away.\n\n");
    //Also there are the \" to add a doble quote or the \\ to add a backslash.
    
    /*Oh, and this is a multi
    line comment.*/
    //Variables.
    printf("Actividad 1: Hacer print de una variable.\n\n");
    int x = 1;
    float y = 1.5;
    char z = 'a';
    printf("%d\n", x);
    printf("%f\n", y);
    printf("%c\n\n", z);
    printf("Actividad 2: Hacer un cálculo entre 2 variables.\n\n");
    int x1 = 2;
    int y1 = 2;
    //Suma.

    printf("La suma entre %d",x1);
    printf(" y %d",y1);
    printf(" es: ");
    printf("%d\n",x1+y1);
    //Resta.

    printf("La resta entre %d",x1);
    printf(" y %d",y1);
    printf(" es: ");
    printf("%d\n",x1-y1);
    //Multiplicación.

    printf("La multiplicación entre %d",x1);
    printf(" y %d",y1);
    printf(" es: ");
    printf("%d\n",x1*y1);
    //División.

    printf("La división entre %d",x1);
    printf(" y %d",y1);
    printf(" es: ");
    printf("%d\n\n",x1/y1);

    //Conditionals (If...Else).
    printf("Actividad 3: Usa el condicional If.\n\n");
    int x2;
    printf("Introduce un valor, si este es mayor que 100, entonces\n te diré que es mayor. Si no lo es, entonces te diré\nque es menor: ");
    scanf("%d", &x2);
    if (x2>100) {
        printf("\nEs mayor que 100.\n\n");
    } else {
        printf("\nEs menor que 100.\n\n");
    }
    //The return 0 is used to finish the function of main.
    return 0;
}