package com.jesus;

public class Matriz1_9 {
    int[][] matriz = {
            {1,2,3},
            {4,5,6},
            {7,8,9}
    };

    public void imprimirMatriz1_9() {
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                System.out.print(matriz[i][j] + " ");

            }
            System.out.println();

        }
    }

    public void tabla() {
        System.out.println("+---+---+---+");
        for (int i = 0; i < matriz.length; i++) {
            System.out.print("|");
            for (int j = 0; j < matriz[i].length; j++) {
                System.out.printf(" %d |", matriz[i][j]);
            }
            System.out.println();
            System.out.println("+---+---+---+");
        }
    }


    public int sumaElementos() {
        int suma = 0;

        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                suma += matriz[i][j];
            }
        }
        return suma;
    }

    public void intercambiarFilas(int fila1, int fila2) {
        int[] temp = matriz[fila1];
        matriz[fila1] = matriz[fila2];
        matriz[fila2] = temp;
    }
}
