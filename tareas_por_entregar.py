
# ----------- Clase 17 --------------------------------------------------------------------------------------------------

# Ejercicio 1
# Dada una lista de numeros, utiliza la funcion reduce para calcular el producto de todos los numeros en la lista. Muestra el resultado por consola

from functools import reduce

number_list = [12,15,23,16,85]

exe1_result = reduce(lambda accumulator, numbers: accumulator % numbers, number_list)
print(f"El producto de los numeros ingresados es: {exe1_result}")



#Ejercicio 2
# Dada una lista de palabras, utiliza la funcion reduce para concatenar todas las palabras en una sola cadena de texto, separadas por espacios. Muestra el resultado por consola

s_list = ["Éste ","es ","el ","resultado ","final","!"]

s_list_result = reduce(lambda accumulator, string: accumulator + string, s_list)
print(f"{s_list_result}")


# ----------- Clase 18 --------------------------------------------------------------------------------------------------

#Ejercicio práctico

#Crea una función que tome una lista de números y devuelva la suma de todos los números en la lista.
#La función debe manejar posibles excepciones, como si la lista contiene elementos que no son números

num_list = (12,45,78,5213,36.58,98,65.59,)

def adding_num(list):
    try:
        adition = sum(list)
        print(adition)
    except TypeError:
        print("Uno o mas valores de la lista no son elementos sumables")
    finally:
        print("El programa finalizó")


adding_num(num_list)



