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

