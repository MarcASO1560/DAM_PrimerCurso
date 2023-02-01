import java.util.*;
import java.io.*;
public class Ejercicio3 {
    public static void ej3() throws IOException, InterruptedException {
        boolean hahaha = true;
        Scanner x = new Scanner(System.in);
        ProcessBuilder pb = new ProcessBuilder();
        pb.command("clear").inheritIO().start().waitFor();
        while (hahaha){
            System.out.println("Actividad 3:");
            System.out.println("Esta actividad pide una palabra que el programa devolverá");
            System.out.println("añadiendo la misma palabra pero invertida y pegada a la derecha");
            System.out.println("de la primera palabra escrita.");
            System.out.println("Quieres iniciar la actividad? [s/n]: ");
            String adv = x.next();
            if (adv.equals("s") || adv.equals("S")){
                while (hahaha){
                    pb.command("clear").inheritIO().start().waitFor();
                    System.out.print("Escribe una palabra: ");
                    String palabra = x.next();
                    String result = convert(palabra);
                    System.out.println(result);
                    System.out.println("Quieres jugar de nuevo? [s/n]");
                    String adv2 = x.nextLine();
                    if (adv2.equals("s") || adv2.equals("S")){
                        pb.command("clear").inheritIO().start().waitFor();
                    } else if (adv2.equals("n") || adv2.equals("N")){
                        hahaha = false;
                    }
                }
            } else if (adv.equals("n") || adv.equals("N")){
                break;
            }
        }
    }
    public static String convert(String palabra){
        String[] Palabra = palabra.split("");
        ArrayList<String> y = new ArrayList<String>();
        for (int i=Palabra.length-2; i >= 0; i--){
            y.add(Palabra[i]);
        }
        return String.join("",Palabra) + String.join("", y);
    }
}
