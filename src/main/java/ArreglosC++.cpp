#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {
    int numeros[10];

    // inicializa la semilla del generador de numeros aleatorios, se usa time para que siempre sea diferente la semilla dependiendo la hora del sistema
    srand(time(0));

    // genera un numero random entre 1 y 100
    for (int i = 0; i < 10; i++) {
        numeros[i] = rand() % 100 + 1;
    }

    // transforma todos los numeros impares en 0 y multiplica el valor por su indice
    for (int i = 0; i < 10; i++) {
        if (numeros[i] % 2 != 0) {
            numeros[i] = 0;
        }
        numeros[i] = numeros[i] * i;
    }

    // recorrido clasico
    cout << "Recorrido clasico:" << endl;
    for (int i = 0; i < 10; i++) {
        cout << "Posicion " << i << ": " << numeros[i] << endl;
    }

    // recorrido range-based for loop solo si el compilador soporta C++11 o mas
    cout << "\nRecorrido for-each:" << endl;
    for (int n : numeros) {
        cout << n << endl;
    }

    // busqueda lineal
    int valorBuscado = 50;
    bool encontrado = false;
    for (int i = 0; i < 10; i++) {
        if (numeros[i] == valorBuscado) {
            cout << "\nValor encontrado en la posicion " << i << endl;
            encontrado = true;
            break;
        }
    }

    if (!encontrado) {
        cout << "\nValor no encontrado en el arreglo" << endl;
    }

    return 0;
}
