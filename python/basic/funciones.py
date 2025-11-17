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
    variableDos = 20
    

def sum(num1, num2):
    print("El resultado de la suma es: ", num1 + num2)
    
def say HelloUser(name):
    print(f"Hola {name}) """
    
    
# Ejercicio> Crear una funcion que salude a una persona por su nombre y apellido y mostrar el resultado por consola

def greet(name, lastname):
    print(f"Hola {name} {lastname}")

greet("Delvis", "Sanabria")

# En el caso de que uno de los parametros sea opcional

def saludo(name, Lastname, country = "Venezuela"): 
    print(f"Hola {name} {Lastname}, soy de {country}")

saludo("Delvis, Sivira")
saludo("Andreina", "Sanabria", "Colombia")
      