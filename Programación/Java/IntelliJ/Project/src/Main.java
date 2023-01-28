import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException, InterruptedException{
        boolean condition = true;
        while (condition == true){
            new ProcessBuilder("clear").inheritIO().start().waitFor();
            System.out.println("=================================");
            System.out.println("|              MENU             |");
            System.out.println("=================================");
            System.out.println("| Opciones:                     |");
            System.out.println("|        1. Actividad 1         |");
            System.out.println("|        2. Actividad 2         |");
            System.out.println("|        a. Actualizar          |");
            System.out.println("|        x. Salir jajajajaja              |");
            System.out.println("=================================");
            System.out.println(" ");
            System.out.println("Escoje una opción: ");
            Scanner x = new Scanner(System.in);
            String num = x.nextLine();
            switch (num){
                case "1":
                    Ejercicio1 obj = new Ejercicio1();
                    obj.ej1();
                    break;
                case "2":
                    Ejercicio2 obj2 = new Ejercicio2();
                    obj2.ej2();
                    break;
                case "a":
                    Runtime.getRuntime().exec("sh script.sh");
                    break;

                case "x":
                    new ProcessBuilder("clear").inheritIO().start().waitFor();
                    while (condition == true){
                        System.out.println("Seguro que quieres salir? [S/N]");
                        Scanner y = new Scanner(System.in);
                        String adv = y.nextLine();
                        if (adv.equals("s") || adv.equals("S")){
                            condition = false;
                        } else if (adv.equals("n") || adv.equals("N")){
                            break;
                        } else{
                            System.out.println("No se ha entendido...");
                        }
                }
        }

         }
    }
}
