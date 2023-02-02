import java.util.*;
import java.io.*;
public class Ejercicio3 {
    public static void ej3() throws IOException, InterruptedException {
        boolean hahaha = true;
        Scanner x = new Scanner(System.in);
        ProcessBuilder pb = new ProcessBuilder();
        pb.command("clear").inheritIO().start().waitFor();
        System.out.println("Actividad 3:");
        System.out.println("Esta actividad pide una palabra que el programa devolverá");
        System.out.println("añadiendo la misma palabra pero invertida y pegada a la derecha");
        System.out.println("de la primera palabra escrita.");
        while (hahaha == true){
            System.out.println("Quieres iniciar la actividad? [s/n]: ");
            String adv = x.next();
            if (adv.equals("s") || adv.equals("S")){
                while (hahaha == true) {
                    System.out.print("Escribe una palabra: ");
                    String palabra = x.next();
                    String result = convert(palabra);
                    System.out.println(result);
                    break;
                }
            } else if (adv.equals("n") || adv.equals("N")){
                hahaha = false;
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
