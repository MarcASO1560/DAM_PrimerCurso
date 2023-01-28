import java.io.*;
import java.util.*;
public class Ejercicio1 {
    public static void ej1() throws IOException, InterruptedException{
        boolean condition = true;
        new ProcessBuilder("clear").inheritIO().start().waitFor();
        while (condition==true){
            System.out.println("Quieres empezar el juego? [s/n]");
            Scanner x = new Scanner(System.in);
            String palabra = x.nextLine();
            int cc = 3;
            if ( palabra.equals("S") || palabra.equals("s")){
                while (condition==true){
                    System.out.println("Empieza el juego:");
                    System.out.println("Escribe una palabra secreta:");
                    Scanner y = new Scanner(System.in);
                    String secreto = y.nextLine();
                    while (condition==true){
                        new ProcessBuilder("clear").inheritIO().start().waitFor();
                        if (cc > 1) {
                            System.out.println("Adivina la palabra, tienes " + cc + " intentos: ");
                        } else {
                            System.out.println("Adivina la palabra, tienes " + cc + " intento: ");
                        }
                        Scanner z = new Scanner(System.in);
                        String intento = z.nextLine();
                        if (intento.equals(secreto)){
                            new ProcessBuilder("clear").inheritIO().start().waitFor();
                            System.out.println("Has ganado el juego!!!");
                            break;
                        } else {
                            cc--;
                        } if (cc == 0){
                            new ProcessBuilder("clear").inheritIO().start().waitFor();
                            System.out.println("Has perdido el juego... La palabra secreta era: " + secreto);
                            break;
                        }
                    }
                    break;
                }
            } else if (palabra.equals("N") || palabra.equals("n")){
                System.out.println("Acaba el programa.");
                break;
            } else {
                System.out.println("No se entiende...");
            }
        }

    }

}