# Bloque aislado de codigo reutilizable que realiza una tarea especifica
# Primero se define con def, se declara el nobre y la accion abajo
""" def say_hello():
    print("Hello!")
    
# LLamar una funcion
say_hello()

# Entrada de valores y parametros

# Variable global puede ser accedida desde cualquier parte del codigo
variable = 10

def sayHelloAndShowVariable():
    print ("Hola muchachos")
    print (variable)
    # variable local no puede ser accedida desde cualquier parte del codigo
    variableDos = 20"""
    

""" def sum(num1, num2):
    print("El resultado de la suma es: ", num1 + num2) """
    
"""def say HelloUser(name):
    print(f"Hola {name}) """
    
    
# Ejercicio> Crear una funcion que salude a una persona por su nombre y apellido y mostrar el resultado por consola

""" def greet(name, lastname):
    print(f"Hola {name} {lastname}")

greet("Delvis", "Sanabria")

# En el caso de que uno de los parametros sea opcional

def saludo(name, Lastname, country = "Venezuela"): 
    print(f"Hola {name} {Lastname}, soy de {country}")

saludo("Delvis, Sivira")
saludo("Andreina", "Sanabria", "Colombia") """

#Las funciones son bloques de codigo reutilizables, que nos permiten realizar tareas especificas


#Definir una funcion
""" def sayHello():
  print("Hola Mundo")
   """
#llamar a una funcion
#sayHello()

#Scope

#Variable global puede ser accedida desde cualquier parte del codigo
#variable = 10

""" def sayHelloAndShowVariable():
  print("Hola muchachos")
  print(variable)
  #varible local no puede ser accedida desde cualquier parte del codigo
  variableDos = 20
  print("estoy pintnando la variableDos desde dentro de la funcion", variableDos)
  
sayHelloAndShowVariable()

#print("estoy pintnando la variableDos desde fuera de la funcion", variableDos)

def sum(num1, num2):
  print("El resultado de la suma es: ", num1 + num2)
  
sum(2,3)
sum(4,5)
sum(6,7)

#Podemos crear funciones que reciban parametros(variables) para ser usados dentro de la funcion para realizar alguna tarea estos parametros son leidos por posicion de izquierda a derecha

#la estructura de una funcion con parametros es la siguiente : def nombreFuncion(parametro1, parametro2):
def sayHelloUser(name):
  print(f"Hola {name}")
  
sayHelloUser("Delvis")
sayHelloUser("Andreina")
sayHelloUser("Eduardo") """

#crear una funcion saludo que salude a una persona por su nombre y apellido y mostrar el resultado por consola

#podemos definir parametros con valores por defecto para que en caso de no recibir un valor se use el valor por defecto
"""def saludo(name, lastname = "", country = "Venezuela"):
  print(f"Hola {name} {lastname}, soy de {country}")
  
saludo("Delvis", "Sivira")
saludo("Andreina", "Sanabria", "Colombia")
saludo("Eduardo", "Sanabria")"""

""" def sumTwoNumbers(num1, num2):
  result = num1 + num2
  #Solo hay un return y solo se puede delvover un valor
  return result  

sumResult = sumTwoNumbers(2, 3)
print(sumResult)
 """

# Ejercicio
# Define una función "calculator", que reciba dos numeros, y el tipo de operacion y segun el tipo de operacion la realice y retorne el resultado. luego muestra el resultado por consola 

""" num1 = 25
num2 = 55
simbolo = "div"

def calculator(num1, simbolo, num2):
  if simbolo == "suma":
    result = num1 + num2
  elif simbolo == "resta":
    result = num1 - num2
  elif simbolo == "mult":
    result = num1 * num2
  elif simbolo == "div":
    result = num1 / num2
  elif simbolo == "prod":
    result = num1 % num2
  return result

print(calculator(num1, simbolo, num2)) """

# Estructura: variable = lambda parametros : operacion
# #Crear una funcion lambda que salude

""" saludo = lambda nombre: print("Hola", nombre)
saludo("Eduardo") """

#Tipos de funciones

#Funcion lambda

#son funciones anonimas que nos permiten crear funciones en una sola linea

#estructura: variable = lambda parametros : operacion

""" sum = lambda num1, num2: print("El resultado de la suma es: ", num1 + num2)

sum(1,2)
  
#Ejercicio 1 (si estas viendo la grabacion has esto y envialo 🥰)
#Crear una funcion lambda que salude 

name = lambda name: print(f"Hola {name} como estas?")

#Funciones Callbacks 
#Son funciones que se pasan como parametro a otras funciones

#Ejemplo"""

""" def process(list, callback): 
  process recibira una lista de elementos y una funcion (callback)
      para cada uno de los elementos dentro de la lista, aplicara esa funcion que le pasamos
      y asi delvolvera una nueva lista con los elementos transformados

  return [callback(item) for item in list]
  este return nos devuelve una nueva lista que aplica un for a la lista original y transforma cada elemento con la funcion que le pasamos 

numbers = [1,2,3,4,5,6,7,8,9,10]
result = process(numbers, lambda item: item * 2)
print(result)  """

# Funciones generales: Son funciones que vienen por defecto en python para evitar la recursividad

#Ejercicio 2
#Crear una función que reciba una lista de números y una función callback
#y devuelva una nueva lista con los números transformados divididos entre 2 y luego mostrar los primos y no primos según la función callback
""" list = [1,2,3,4,5,6,7,8,9,10]

def lista(list, callback):
  result = [callback(item) for item in list, lambda / item]
  print(list(result))
  
  lista(list, lambda item: item / 2)
 """
print("Hola mundo"