
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

#                    !! PENDIENTE!!



#----------- Clase 19 --------------------------------------------------------------------------------------------------

#Ejercicio:

#Crear una clase llamada "Estudiante" que tenga los atributos "nombre", "edad" y "carrera".
#Agregar un metodo llamado "estudiar" que imprima un mensaje indicando que el estudiante esta estudiando su carrera.

class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    def estudiar(self):
        return f"El estudiante {self.nombre}, de edad {self.edad} se encuentra estudiando {self.carrera}"

student = Estudiante("Eduardo Nunes", 27, "Programacion orientada a objetos")
print(student.estudiar()) 


#Ejercicio de herencia y polimorfismo
#Crear una clase llamada "Vehiculo" con los atributos "marca", "modelo" y "anio".
#Agregar un metodo llamado "info" que imprima la informacion del vehiculo.
#Crear dos clases hijas llamadas "Coche" y "Motocicleta" que hereden de la clase "Vehiculo".
#Modificar el metodo "info" en ambas clases hijas para que imprima informacion especifica de cada tipo de vehiculo.


class Vehiculo:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def info(self):
        return f"El vehiculo es de la marca {self.brand}, y es un modelo {self.model} del año {self.year}!!"

class Coche(Vehiculo):
    def info(self):
        return f"El vehiculo es de la marca {self.brand}, y es un modelo {self.model} del año {self.year}!!"
    
class Motocicleta(Vehiculo):
    def info(self):
        return f"El vehiculo es de la marca {self.brand}, y es un modelo {self.model} del año {self.year}!!"
    
coche = Coche("Ford","Laser",90)
coche.info()
moto = Motocicleta("Yamaha","R7",2026)
moto.info()

print(coche.info())
print(moto.info())


#mostrar atributos en forma de diccionario

carDictionary = car.__dict__
print(carDictionary)
        
        
#Extender la funcionalidad de una clase existente sin modificar su codigo fuente
#Utilizando la funcion "super()" podemos llamar a los metodos de la clase padre desde la clase hija

class ElectricCar(Coche):
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year)
        self.battery_capacity = battery_capacity
        
    def info(self):
        super().info()
        print(f"Capacidad de la bateria: {self.battery_capacity} kWh")
    def charge(self):
        print(f"Cargando el coche {self.brand} {self.model}...")
        
electric_car = ElectricCar("Tesla", "Model S", 2022, 100)
electric_car.info()
electric_car.charge()

