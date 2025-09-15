import random
import array

# - 1. Declaración y creación. -

# En Python, se puede escribir una lista con datos anteriormente puestas de esta manera:
Lista_escrita = [1,2,3,4,5,6,7,8,9,10]

# Se puede utilizar el comando "array" para hacer el enlistado multiples datos relacionados a una unica variable.
# Usualmente usado en otros lenguajes, como Java, pero donde tambien se le puede usar en Python con una extención.
Lista_array = array.array( 'i', [random.randint(1,10) for _ in range(10)])

# Mientras que, en Python, se llega a hacer con "list", pudiendo utilizar la misma estructura anteriormente mostrada, sin necesidad del poner "array".
Lista_list = [random.randint(1,10) for _ in range(10)]

# Vamos a seguir haciendo ejercicios con este tipo de listados, así que se crearan mas listados con distinto nombre para la practica.
Lista_0 = Lista_list.copy()
Lista_x = Lista_list.copy()


# ----------
# - 2. Recorrido e impresión. -

# 1ro, se deja un espacio vacio, donde se "guardaran" el resultado de la lista aleatoria "Lista list".
# Por esto mismo, se le llamará a este guardado: "resultados".
resultados = []
resultadosX = []

# Con el 'for' de bucle clasico.
# Se llegar a elegir la lista, agregar el guardado "resultados" para ver la posición de la lista señalada.
for n in range(len(Lista_list)):
    resultados.append(f'Posición {n}: {Lista_list[n]}')


# ----------
# - 3. Modificación. -

# Cambiar los números con resultados impares en 0.
for n in range(len(Lista_0)):
    if Lista_0[n] %2 !=0:
        Lista_0[n] = 0

# Multiplicar los indises o posiciones con el resultado del listado.
Lista_xResultados = [n * valor for n, valor in enumerate(Lista_x)]

for n in range(len(Lista_xResultados)):
    resultadosX.append(f'Posición {n}: {Lista_xResultados[n]}')


# ----------
# - 4. Busqueda. -

# Implementar busqueda lineal para encontrar un valor en el arreglo.
# Se agrega un if, else, y el valor al cual se quiere buscar.

valor = 8

def if_valor_Lista_list(valor, Lista_list):
    if valor in Lista_list:
        return f'El valor {valor} si está en la lista, en la posición {Lista_list.index(valor)}'
    else:
        return f'El valor {valor} NO está en la lista'

resultado_if = if_valor_Lista_list(valor, Lista_list)


# -- Impresión/Impresión. --
print(
    '-------------------------- \n'
    '- 1. Arreglos ( Arrays ) - \n'
    '-------------------------- \n'
    '1. Declaración y Creación. \n \n',
    'Así se muestra la "Lista escrita", con listado ya seleccionado en Python: \n',
    Lista_escrita, '\n \n',
    'Así se muestra la "Lista array", con aleatorio en Python: \n',
    Lista_array, '\n \n',
    'Así se muestra la "Lista list", con "list" ( o por predeterminado ) aleatorio en Python: \n',
    Lista_list, '\n \n'
    '----------\n'
    '2. Recorrido e Impresión. \n \n',
    'Así se muestra la "Lista list", con "for". \n',
    'Se puede representar de forma horizontal: \n',
    ' / '.join(resultados), '\n \n',
    'O tambien, representarse de forma vertical ( con "\\n" ): \n',
    '\n'.join(resultados), '\n \n'
    '----------\n'
    '3. Modificación. \n \n',
    'Cambiar todos los valores por 0: \n',
    Lista_0, '\n \n',
    'Multiplicar todos los valores por su indice. \n',
    'Primero el referente: \n',
    Lista_x, '\n \n'
             'Y luego el modificado: \n',
    '\n'.join(resultadosX), '\n \n'
    '---------- \n'
    '4. Busqueda. \n \n',
    'Implementar busqueda lineal para encontrar un valor en el arreglo. \n',
    'En este ejemplo, usaremos el numero 8 para buscarlo en la lista \n',
    Lista_list, '\n',
    resultado_if
)