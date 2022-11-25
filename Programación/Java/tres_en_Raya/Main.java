import java.util.Scanner;

public class Utils {

    //CONSTRUCTOR
    public Utils(){
    }

    //METODES I FUNCIONS
    public void generaTauler(int[][] tauler){
        for (int i=0; i<3; i++){
            for (int j=0; j<3; j++){
                tauler[i][j] = 0;
            }
        }
    }
    //MOSTRA TAULER
    public void mostraTauler(int[][] tauler){
        for (int i=0; i<3; i++){
            for (int j=0; j<3; j++){
                System.out.print(tauler[i][j] + " ");
            }
            System.out.println("");
        }
    }
    //SET POSICIO: introdueix un 1 a la taula
    public void setPosicio(String posicio, int[][] tauler, int player){
        if (tauler[(int)(posicio.charAt(0))-48][(int)(posicio.charAt(1))-48] == 0) {
            tauler[(int) (posicio.charAt(0)) - 48][(int) (posicio.charAt(1)) - 48] = player + 1;
        }else{
            System.out.println("Casella incorrecta. Has perdut el torn.");
        }
    }

    //COMPROVA GUANYADOR
    public boolean comprovaGuanyador(int[][] tauler){
        boolean acaba = false;

        //mira FILES
        for (int fila=0; fila < 3; fila++){
            if ((tauler[fila][0] == tauler[fila][1]) && (tauler[fila][1] == tauler[fila][2]) && (tauler[fila][0] != 0)){ acaba = true; }
        }
        //mira COLUMNES
        for (int columna=0; columna < 3; columna++){
            if ((tauler[0][columna] == tauler[1][columna]) && (tauler[1][columna] == tauler[2][columna]) && (tauler[0][columna] != 0)){ acaba = true; }
        }
        //mira DIAGONAL \ 00 11 22
        if ((tauler[0][0] == tauler[1][1]) && (tauler[1][1] == tauler[2][2])  && (tauler[1][1] != 0)){ acaba = true; }

        //mira DIAGONAL /  20 11 02
        if ((tauler[2][0] == tauler[1][1]) && (tauler[1][1] == tauler[0][2]) && (tauler[1][1] != 0)){ acaba = true; }

        System.out.println("Acaba = " + acaba);

        return acaba;
    }


}
public class Main {
    public static void main(String[] args){
        System.out.println("*** Benvinguts al 3 en Raya ***");

        Scanner sc = new Scanner(System.in);
        boolean acaba = false;
        int tauler[][] = new int[3][3];
        Utils ut = new Utils();
        String jugador[] = {"Jaume", "Tolo"};
        String posicio = "";
        int player = 0;

        ut.generaTauler(tauler);
        ut.mostraTauler(tauler);

        System.out.println("Els jugadors son: "+jugador[player]+", "+jugador[player+1]);
        player = (int)(Math.random()*2);

        while (!acaba) {

            if (player == 0){player = 1;}else{player = 0;}
            System.out.println("Hola "+ jugador[player] + ", tria una opció:");
            posicio = sc.next();
            ut.setPosicio(posicio, tauler, player);
            ut.mostraTauler(tauler);
            acaba = ut.comprovaGuanyador(tauler);
            if (acaba) { System.out.println("El jugador "+ jugador[player] + " ha guanyat");
            }
        }
    }
}