import java.util.*;
import java.io.*;
public class Ejercicio2 {
    public static void ej2() throws IOException, InterruptedException{
        boolean condition = true;
        ProcessBuilder pb = new ProcessBuilder();
        pb.command("clear").inheritIO().start().waitFor();
        while(condition == true){
            System.out.println("Actividad 2:");
            System.out.println("Este ejercicio trata sobre escribir escribir una cadena de");
            System.out.println("texto así como una frase o una oración. Para luego poder volver");
            System.out.println("una palabra que esté dentro de la cadena anteriór y que el");
            System.out.println("programa cambie la palabra de la cadena a mayúscula.");
            System.out.println("Quieres empezar el juego? [s/n]");
            Scanner x = new Scanner(System.in);
            String adv = x.nextLine();
            if (adv.equals("s") || adv.equals("S")){
                while(condition == true){
                    System.out.println("Escribe una cadena de texto:");
                    String cadena = x.nextLine();
                    System.out.println("Escribe una palabra que esté dentro de la cadena: ");
                    String palabra = x.nextLine();
                    String result = convert(cadena,palabra);
                    System.out.println(result);
                    System.out.println("Quieres jugar de nuevo? [s/n]");
                    String adv2 = x.nextLine();
                    if (adv2.equals("s") || adv2.equals("S")){
                        pb.command("clear").inheritIO().start().waitFor();
                    } else if (adv2.equals("n") || adv2.equals("N")){
                        condition = false;
                    }
                }
            } else if (adv.equals("n") || (adv.equals("N"))){
                condition = false;
            }
        }
    }
    public static String convert(String cadena, String palabra){
        String[] Cadena = cadena.split(" ");
        for (int i=0; i < Cadena.length ; i++){
            if (Cadena[i].equals(palabra)){
                Cadena[i] = palabra.toUpperCase();
            }
        }
        return String.join(" ", Cadena);
    }
}