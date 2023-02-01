import java.io.*;
import java.util.*;
public class Ejercicio1 {
    public static void ej1() throws IOException, InterruptedException{
        boolean condition = true;
        new ProcessBuilder("clear").inheritIO().start().waitFor();
        while (condition==true){
            System.out.println("Actividad 1:");
            System.out.println("Este ejercicio es un juego de adivinar una palabra secreta,");
            System.out.println("al escribir esta, tienes 3 intentos para adivinarla, si no");
            System.out.println("lo consigues, pierdes.");
            System.out.println("Quieres empezar el juego? [s/n]");
            Scanner x = new Scanner(System.in);
            String palabra = x.nextLine();
            int cc = 3;
            if ( palabra.equals("S") || palabra.equals("s")){
                while (condition==true){
                    System.out.println("Empieza el juego:");
                    System.out.println("Escribe una palabra secreta:");
                    String secreto = x.nextLine();
                    while (condition==true){
                        new ProcessBuilder("clear").inheritIO().start().waitFor();
                        if (cc > 1) {
                            System.out.println("Adivina la palabra, tienes " + cc + " intentos: ");
                        } else {
                            System.out.println("Adivina la palabra, tienes " + cc + " intento: ");
                        }
                        String intento = x.nextLine();
                        if (intento.equals(secreto)){
                            new ProcessBuilder("clear").inheritIO().start().waitFor();
                            System.out.println("Has ganado el juego!!!");
                            System.out.println("Quieres volver a jugar? [s/n]");
                            String adv2 = x.nextLine();
                            if (adv2.equals("s") || adv2.equals("S")){
                                new ProcessBuilder("clear").inheritIO().start().waitFor();
                            } else if (adv2.equals("n") || adv2.equals("N")){
                                condition = false;
                            }
                        } else {
                            cc--;
                        } if (cc == 0){
                            new ProcessBuilder("clear").inheritIO().start().waitFor();
                            System.out.println("Has perdido el juego... La palabra secreta era: " + secreto);
                            System.out.println("Quieres volver a jugar? [s/n]");
                            String adv2 = x.nextLine();
                            if (adv2.equals("s") || adv2.equals("S")){
                                new ProcessBuilder("clear").inheritIO().start().waitFor();
                            } else if (adv2.equals("n") || adv2.equals("N")){
                                condition = false;
                            }
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