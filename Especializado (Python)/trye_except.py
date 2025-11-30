# Normalmente si tenemos un error en el codigo Python (porque otros lenguajes normalmente no lo hacen) nos sugerirá la linea y el tipo de error, esto en un servidor no es plausible porque perderiamos tiempo y emosion, reputacion y dinero

#try-except nos permite manejar los errores de nuestro codigo de una forma muy parecida al IF, de manera que si presenta algun error nuestra aplicacion no colapse por eso si no que intente dar una sugerencia de como arreglralo y continue con la ejecucion del programa

""" 
try:
    # Código que puede generar una excepción
    resultado = 10 / 0
except ZeroDivisionError:
    # Código para manejar la excepción
    print("No se puede dividir por cero")
"""

def divider(a, b):
    try:
      #En este bloque intentamos ejecutar el código que puede generar una excepción
        return print("El resultado es:", a / b)  # Dividimos a / b
    except ZeroDivisionError: #Estas son una especie de funciones especificas hechas para cada caso en especifico, asi como el typeError
        return print("No se puede dividir por cero")
    except TypeError:
        return print("Los operandos deben ser números")
    finally: #El bloque finally se ejecuta siempre, haya o no una excepcion
        print("La funcion termino")

divider(5, 5)  # Esto generará una excepción de división por cero
divider(5, 'a')  # Esto generará una excepción de tipo

print("El programa continúa ejecutándose después del error.")

#Otro ejemplo

def convert_to_int(value):
    try:
        convert = int(value)
    except ValueError:
        print(f"No se puede convertir '{value}' a entero.")
    else: #Para poder usar el else en estos casos hay que convertir el valor ingresado a una variable como hicimos en la linea 34
        print(f"La conversión de '{convert}' fue exitosa.")
        return convert #Esto lo pusimos aqui como ejemplo de buena practica por si despues de ingresarlo se necesita para otra cosa
        # Otra buena practica es colocar despues de un else un return "None" para que no se devuelva un dato innecesario
    finally:
        print("Intento de conversión finalizado.")
    
print(convert_to_int("123"))  # Debería imprimir 123
print(convert_to_int("ab4y55c"))  # Debería manejar el error y devolver None

#Error de indice

try: 
  listItem = [1, 2, 3]
  element = listItem[1]  # Intentamos acceder a un índice que no existe
except IndexError:
  print("Índice fuera de rango.")
else:
  print("Elemento en el índice elegido es:", element)
finally:
  print("El bloque finally se ejecuta siempre.")
  
#Ejercicio práctico

#Crea una función que tome una lista de números y devuelva la suma de todos los números en la lista.
#La función debe manejar posibles excepciones, como si la lista contiene elementos que no son números

num_list = (12,45,78,5213,36.58,98,65.59)

def adding_num(list):
        adition = sum(list)
        print(f"La suma total es: {adition}")
        return list != int or float
    try:
        
    except TypeError:
        print("Uno o mas valores de la lista no son elementos sumables")
    finally:
        print("El programa finalizó")


adding_num(num_list)

numbers = [1,2,3,4,5,6,7,8,9,10]
def is_even(number):
    return number % 2 == 0 #Esto para filter retornara True solo para los numeros pares
even_numbers = filter(is_even, numbers)
print(f"Números pares: {list(even_numbers)}")