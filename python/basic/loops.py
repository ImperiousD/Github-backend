#Los loops son estructuras de control que nos permiten repetir un bloque de codigo
#un numero determinado de veces o mientras se cumpla una condicion

#While  (Mientras se cumpla)
""" count = 0

while count < 3:
  print(f"me ejecuto, estoy en la vuelta {count}")
  count += 1
  
print("Sali del bucle")


choise = int(input("Para iniciar escribe 1:"))
Asi se puede convertir aqlgo en otro tipo de valor . Los inputs siempre se escriben en string
#Ejemplo de bucle calculador de suma

choise = int(input("Para iniciar escribe 1:"))

while choise == 1:
  num1 = int(input("Ingresa el primer numero a sumar: "))
  num2 = int(input("Ingresa el segundo numero a sumar: "))
  total = num1 + num2
  print(f"El resultado de tu suma fue {total}")
  choise = int(input("Para reinicar escribe el numero 1: "))
  
print("Fin del programa") """










##                                      FOR

#For (para cada elemento) nos creara un bucle que se repetira segun la cantidad de elementos

""" fruits = ["apple", "orange", "banana"]
print(fruits)

#for (elemento in lista): (lo que quiero hacer a cada elemento en cada vuelta (iteracion))
for fruit in fruits:
  print(fruit)

#Pintar una cantidad especifica de numeros segun un rango (una extesion de numeros de A a Z)

for number in range(0,11):
  print(f"El numero es: {number}")

myList = ["Eduardo", "Jesus", "Hugo", "Delvis"]

#Break (break) nos sirve para romper un bucle
for name in myList:
  if name == "Jesus":
    break #rompe el bucle
  print(f"El nombre es: {name}")
 
#Continue (continue) nos sirve para saltar a la siguiente iteracion 
for name in myList:
  if name == "Jesus":
    continue #se salta a la siguiente iteracion
  print(f"El nombre es: {name}") """






#usando ambos

""" fruits = ["apple", "orange", "banana", "kiwi","coco"]

for fruit in fruits:
  if fruit == "banana":
    continue
  elif fruit == "kiwi":
    print("Estoy en la fruta prohibida")
    break
  print(fruit)

Ejercicio de la forma en que lo hizo el professor
n = int(input("Escribe un numero positivo:"))

for number in range(1, n + 1):
  if (10 < number < 20) or (number % 3 == 0) or (number == 25 or number ==30):
    print(f"El numero {number} cumple con aluna de las condiciones") """


# Ejercicio 2:
#Enunciado: 
# Crea un programa que simule la validación de una contraseña:
# 1. Define una contraseña secreta (ej: `"python123"`).
# 2. Pide al usuario que ingrese una contraseña.
# 3. Usa un bucle `while` para:
#    - Permitir hasta 3 intentos.
#    - Si la contraseña es correcta, muestra "¡Acceso concedido!" y termina.
#    - Si es incorrecta, muestra "Contraseña incorrecta. Intentos restantes: X".
#    - Si se agotan los intentos, muestra "¡Cuenta bloqueada!".


#Ejercicio 3
# Enunciado:  
# Pide al usuario 5 números enteros. Usando un bucle `for` y `match-case`:
# 1. Clasifica cada número en:
#    -"Pequeño" si es menor que 10.
#    -"Mediano" si está entre 10 y 50.
#    -"Grande" si es mayor que 50.
#    -"Cero" si es 0.
# 2. Al final, muestra cuántos números hubo en cada categoría.


""" El ejercicio que habia hecho yo

n = int(input("Para iniciar escribe un numero entero: "))

for i in range(1, n + 1):
    if ((n % 3) == 0):
        print(f"{i} es divisible entre 3 ")
    elif (n > 10) and (n <20):
        print(f"{i} es mayor que 10 y menor que 20 ")
    elif (n == 25) or (n == 50):
        print(f"{i} es igual a 25 o 50 ") """


## Ejercicio 2

""" password = "python123"
count = 4

while count > 0:
    count -= 1
    user_password = input("Introduzca su contraseña: ")
    if user_password == password:
        print("Acceso concedido!")
        break
    elif count == 0:
        print("!Cuenta bloqueada!")
        break
    elif user_password != password:
        print(f"Contraseña incorrecta. Intentos restantes {count}") """
        
## Ejercicio 3

# Pide al usuario 5 números enteros y los clasifica usando match-case
contador_pequeno = 0
contador_mediano = 0
contador_grande = 0
contador_cero = 0

for _ in range(5):
  entrada = input("Escribe un numero entero: ")
  try:
    numero = int(entrada)
  except ValueError:
    print("Entrada no valida. Se tomara como 0.")
    numero = 0

  match numero:
    case 0:
      contador_cero += 1
    case n if n < 10:
      contador_pequeno += 1
    case n if 10 <= n <= 50:
      contador_mediano += 1
    case n if n > 50:
      contador_grande += 1

print(f"Intentos con valor 0: {contador_cero}")
print(f"Numeros pequeños totales: {contador_pequeno}")
print(f"Numeros medianos totales: {contador_mediano}")
print(f"Numeros grandes totales: {contador_grande}")

