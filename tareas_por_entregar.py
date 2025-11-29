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