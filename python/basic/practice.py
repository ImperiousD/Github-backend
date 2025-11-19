#Ejercicio 1 

# Dado una lista de numeros, utiliza la funcion reduce para encontrar el producto de todos los numeros en la lista. Muestra el resultado por consola.

from functools import reduce

myList = [1,2,3,4,5]

def product(accumulator, number):
  return accumulator % number

finalResult = reduce(product, myList)
print(f"El producto de todos los numeros en la lista es: {finalResult}") 


#Ejercicio 2

# Dada una lista de palabras, utiliza la funcion reduce para concatenar todas las palabras en una sola cadena separada por espacios. Muestra el resultado por consola.

myWords = ["Esta", "es", "una", "lista", "de", "palabras"]
def concatenate(accumulator, word):
  return accumulator + " " + word
finalString = reduce(concatenate, myWords)