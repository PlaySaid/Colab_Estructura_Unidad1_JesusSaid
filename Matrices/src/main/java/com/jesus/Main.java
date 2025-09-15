package com.jesus;

public class Main {
    public static void main(String[] args) {
        System.out.print(
                "\n " +
                "------------------------------------------- \n" +
                "- 2. Matrices ( Arrays Bidimencionales ). - \n" +
                "------------------------------------------- \n" +
                "1. Declaración e inicialización. \n" +
                "Acá se dá una matriz de 3x3 en Java: \n \n");

        Matriz0 matriz0 = new Matriz0();
        matriz0.imprimirMatriz0();

        System.out.print("\n Y resuelto se da una matriz 3x3 con numeros agregados del 1 al 9: \n");

        Matriz1_9 matriz1_9 = new Matriz1_9();
        matriz1_9.imprimirMatriz1_9();

        System.out.print("\n" +
                "------------- \n" +
                "2. Recorrido. \n" +
                "La matriz en forma de tabla: \n");

        matriz1_9.tabla();

        System.out.println("\n" +
                "--------------- \n" +
                "3. Operaciones. \n");

        int total = matriz1_9.sumaElementos();

        System.out.println("La suma de todos los elementos de la matriz: " + total + "\n \n" +
                "Y el intercambio de las filas 1 y 2. \n" +
                "1ro, la matriz original, para tener una vista previa antes del cambio: \n");

        matriz1_9.imprimirMatriz1_9();

        System.out.println("\n" +
                "Y la matriz cambiando las filas: \n");

        matriz1_9.intercambiarFilas(0,2);
        matriz1_9.imprimirMatriz1_9();

        System.out.println("\n");
    }
}