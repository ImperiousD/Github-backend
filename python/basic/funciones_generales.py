#map(funcion, iterable), La funcion map aplica una funcion especifica a cada elemento de un iterable (como una list o tupla) y devuelve un objeto map (que es un iterable). Podemos convertir este objeto en una lista o tupla si es necesario

#myList = [1,2,3,4]

"""  def multiplyBy3(number):
    return number * 3

result = map(multiplyBy3,myList)
# Tambien se podria deifinir en una sola linea con un lambda
result2 = map(lambda number: number * 3, myList)
print({result2}) 

print(f"El resultado es: {list(result)}")  """

#Basicamente es la formula para un for que aplicara lo que querramos, al final devuelve un objeto que es cuando devuelve una codificacion extraña, para estos casos hay que convertirlo en una lista como aparece en este ultima linea


# reduce(funcion,iterable) La funcion "reduce" aplica una funcion de manera acumulativa a los elementos de un iterable, reduciendolo a un solo valor. Esta funcion se encuentra en el modulo "functools", por lo que debemos importarla antes de usarla

from functools import reduce

"""myList =[1,2,3,4,5]

def sumTwoNumbers(accumulator,number):
    return accumulator + number

TotalSum = reduce(sumTwoNumbers, myList)
print(f"{TotalSum}") """
# Como se llego a ese resultado?
# Paso 1: accumulator = 1, number = 2 => retorna 3
# Paso 2: accumulator = 3, number = 3 => retorna 6
# Paso 3: accumulator = 6, number = 4 => retorna 10
# Paso 4: accumulator = 10, number = 5 => retorna 15
# Resultado final: 15

# Tambien se puede hacer con un lambda
""" TotalSum2 = reduce(lambda accumulator, number: accumulator + number, myList)
print(f"{TotalSum2}")

mysTring = ["Hola, ", "como ", "estas?"]
mstring_result = reduce(sumTwoNumbers, mysTring)
print(f"'{mstring_result}'")#Las comillas singulares pueden hacer un quote sobre el stirng, las dobles no sirven

# Utilizando una funcion lambda
mysTring = ["Hola, ", "como ", "estas?"]
mstring_result = reduce(lambda accumulator, string: accumulator + string, mysTring)
print(f"'{mstring_result}'") """


# Ejercicio 1
# Dada una lista de numeros, utiliza la funcion reduce para calcular el producto de todos los numeros en la lista. Muestra el resultado por consola

number_list = [12,15,23,16,85]

exe1_result = reduce(lambda accumulator, numbers: accumulator % numbers, number_list)
print(f"El producto de los numeros ingresados es: {exe1_result}")


#Ejercicio 2
# Dada una lista de palabras, utiliza la funcion reduce para concatenar todas las palabras en una sola cadena de texto, separadas por espacios. Muestra el resultado por consola

s_list = ["Éste ","es ","el ","resultado ","final","!"]

s_list_result = reduce(lambda accumulator, string: accumulator + string, s_list)
print(f"{s_list_result}")

# Funciones para transformar datos

#int()
#float()
#str()
#bool()
#list() convierte un iterable en una lista
#tuple()convierte un iterable en una tupla
#dict() Diccionario


#int()

print(int("283"))

#float

print(float("3.14"))
print(float(10))

#list()
print(list((1,2,3)))
print(list("Hola"))

#dict()

print(dict([("nombre", "Juan"),("edad",30)]))

#Tambien lo podemos hacer con variables:

name = "Eduardo"
age = 32

print(dict([(name,age)]))

# Funciones para encontrar elementos en una coleccion

#max() Devuelve el elemento con el valor mayor

print(f"El mayor de ambosa valores es: {max(224,449,568,974)}")

#min()
print(f"El mayor de ambosa valores es: {min(224,449,568,974)}")

# Funciones para realizar operaciones matematicas

#sum() Suma todos los elementos de un iterable

print(f"La suma de los valores es: {sum([10,20,30,40,50])}")

#round() Redondea un numero al entero mas cercano o a un numero especifico de decimales

print(round(3.14159)) #Desde el 5 hacia abajo redondea hacia abajo y al contrario si es 5 o mas redondea hacia arriba

# Funciones para elementos

#sorted() Devuelve una lista ordenada de los elementos de un iterable

print(sorted([5,2,9,1,5,6]))

#Tambien lo puede hacer con strings
print(sorted("python")) #Esta vez en orden alfabetico, no segun las posiciones en la tabla ASCII

#En caso de que querramos que lo devuelva al revez usamos #reverse=True

print(sorted([5,2,9,1,5,6], reverse=True))

#len() Devuelve la cantidad de elementos en un iterable
print(len("Hola Mundo")) #Cuenta los caracteres incluyendo espacios
print(len([1,2,3,4,5])) #Cuenta los elementos en la lista

#Funciones para saber el tipo de dato

#type() Devuelve el tipo de dato del elemento proporcionado

print(type(123))
print(type("Hola"))
print(type([1,2,3]))

#Funciones para rango range()
print(list(range(5))) #Genera una secuencia de numeros desde 0 hasta n-1 (en este caso 4)

print(list(range(2,10))) #Genera una secuencia de numeros desde el valor inicial hasta el valor final -1

print(list(range(1,10,2))) #Genera una secuencia de numeros desde el valor inicial hasta el valor final descontando la cantidad que hayamos puesto como tercer valor (en este caso de 2 en 2)

#Funciones para filtrar elementos

#filter(funcion,iterable) filtra los elementos de un iterable basandose en una funcion que devuelve True o False

numbers = [1,2,3,4,5,6,7,8,9,10]
def is_even(number):
    return number % 2 == 0 #Esto para filter retornara True solo para los numeros pares
even_numbers = filter(is_even, numbers)
print(f"Números pares: {list(even_numbers)}")

#Las variables son inmutables, por lo que no se pueden cambiar, pero si podemos crear nuevas variables basadas en las anteriores

# Otras funciones generales

#abs() Devuelve el valor absoluto de un numero (sin signo)

print(abs(-5))#El valor absoluto de un número es su magnitud o distancia desde el cero en la recta numérica, sin importar si es positivo o negativo. Por ejemplo, el valor absoluto de \(5\) es \(5\), y el de \(-5\) también es \(5\). Se representa con dos barras verticales a cada lado del número, como en \(|-4|=4\)

# all() Devuelve True si todos los elementos de un iterable son verdaderos (o si el iterable esta vacio)

print(all([True, True, True])) #Devuelve True
print(all([True, False, True])) #Devuelve False
print(all([True, 1, "Hola"])) #Devuelve True porque todos los elementos son considerados verdaderos
print(all([True,0])) #Devuelve True porque el iterable esta vacio

#any() Devuelve True si al menos un elemento de un iterable es verdadero. Si el iterable esta vacio, devuelve False

print(any([False, False, True])) #Devuelve True
print(any([False, False, False])) #Devuelve False
print(any([0, "", None, 5])) #Devuelve True porque 5 es considerado verdadero
print(any([])) #Devuelve False porque el iterable esta vacio

# eval() Evalua una expresion en forma de cadena y la ejecuta como codigo Python, una expresion matematica o algo que se pueda ejecutar (Es peligroso)

expression = "3 + 5 * 2"
print(f"El resultado de la expresion {expression} es: {eval(expression)}") #Devuelve 13

#exec() Ejecuta bloque decodigo Python dinamicamente a partir de una cadena de texto (Es peligroso) 

code = "x = 10"
exec(code)
print(f"El valor de x despues de ejecutar exec es: {x}") #Devuelve 10 (Porque esta escrito como una variable basicamente)

#enumerate() Agrega un contador a un iterable y devuelve un objeto enumerado. Es util cuando necesitamos tanto el indice como el valor de los elementos en un bucle

fruits = ["manzana", "banana", "cereza"]
for indice, fruit in enumerate(fruits):
    print(f"Índice: {indice}, Fruta: {fruit}")

# Otro ejemplo

fruits = ["manzana", "banana", "cereza"]
enumerated_fruits = enumerate(fruits)
print(list(enumerated_fruits))

