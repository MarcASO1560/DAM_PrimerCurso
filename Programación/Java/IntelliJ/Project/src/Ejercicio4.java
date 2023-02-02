import java.util.*;
import java.io.*;
public class Ejercicio4 {
    public static void ej4() throws IOException, InterruptedException{
        boolean condition = true;
        ProcessBuilder pb = new ProcessBuilder();
        Scanner x = new Scanner(System.in);
        pb.command("clear").inheritIO().start().waitFor();
        System.out.println("Actividad 4:");
        System.out.println("Esta actividad trata sobre eliminar los espacios existentes en ");
        System.out.println("una cadena de texto pedida.");
        while (condition == true){
            System.out.print("Quieres iniciar la actividad? [s/n]: ");
            Scanner y = new Scanner(System.in);
            String adv = y.next();
            if (adv.equals("s") || adv.equals("S")){
                while (condition == true) {
                    System.out.println("Escribe una cadena de texto:");
                    Scanner z = new Scanner(System.in);
                    String cadena = z.nextLine();
                    String result = convert(cadena);
                    System.out.println(result);
                    System.out.println("Quieres jugar de nuevo? [s/n]");
                    Scanner w = new Scanner(System.in);
                    String adv2 = w.nextLine();
                    if (adv2.equals("s") || adv2.equals("S")) {
                        pb.command("clear").inheritIO().start().waitFor();
                    } else if (adv2.equals("n") || adv2.equals("N")) {
                        condition = false;
                    }
                }
            }else if (adv.equals("n") || (adv.equals("N"))) {
                condition = false;
            }
        }
    }
    public static String convert(String cadena){
        String[] Cadena = cadena.split("");
        for (int i=0; i < Cadena.length ; i++){
            if (Cadena[i].equals(" ")){
                Cadena[i] = "";
            }
        }
        return String.join("", Cadena);
    }
}