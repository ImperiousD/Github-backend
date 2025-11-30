#Ejercicio práctico

#Crea una función que tome una lista de números y devuelva la suma de todos los números en la lista.
#La función debe manejar posibles excepciones, como si la lista contiene elementos que no son números


num_list = [12,45,78,5213,36.58,98,65.59,"Hola"]

def adding_numbers(list):
    

filtered_number = filter(adding_numbers,list)
print(filtered_number)

# estructura de un lambda: # lambda parametros: expresion

adding_numbers(num_list)


#-------------------------------------------------
exe1_result = reduce(lambda accumulator, numbers: accumulator % numbers, num_list)

#lambda

""" s_list = ["Éste ","es ","el ","resultado ","final","!"]

s_list_result = reduce(lambda accumulator, string: accumulator + string, s_list)
print(f"{s_list_result}")


#filter

numbers = [1,2,3,4,5,6,7,8,9,10]
def is_even(number):
    return number % 2 == 0 #Esto para filter retornara True solo para los numeros pares
even_numbers = filter(is_even, numbers)
print(f"Números pares: {list(even_numbers)}") """


from functools import reduce

