#include <iostream>
using namespace std;

int main() {
    // declaracion e inicializacion de la matriz 3x3
    int matriz[3][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };

    // mostrar la matriz en forma de tabla
    cout << "Matriz en forma de tabla:" << endl;
    for (int x = 0; x < 3; x++) {            // filas
        for (int y = 0; y < 3; y++) {        // columnas
            cout << matriz[x][y] << " ";
        }
        cout << endl;
    }

    // recorrer por columnas
    cout << "\nRecorrido por columnas:" << endl;
    for (int x = 0; x < 3; x++) {            // columnas
        for (int y = 0; y < 3; y++) {        // filas
            cout << matriz[y][x] << " ";
        }
        cout << endl;
    }

    // suma todos los elementos
    int suma = 0;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            suma += matriz[i][j];
        }
    }
    cout << "\nSuma de todos los elementos: " << suma << endl;

    // intercambia la primera fila por la última
    for (int j = 0; j < 3; j++) {
        int temp = matriz[0][j];
        matriz[0][j] = matriz[2][j];
        matriz[2][j] = temp;
    }

    // mostrar la matriz despues del intercambio
    cout << "\nMatriz despues de intercambiar primera y ultima fila:" << endl;
    for (int x = 0; x < 3; x++) {
        for (int y = 0; y < 3; y++) {
            cout << matriz[x][y] << " ";
        }
        cout << endl;
    }

    return 0;
}
