package com.jesus;

public class Matriz0 {
    int[][] matriz = new int[3][3];

    public void imprimirMatriz0() {
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                System.out.print(matriz[i][j] + " ");

            }
            System.out.println();
        }
    }
}

