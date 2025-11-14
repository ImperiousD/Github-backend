""" Comentario
de varias 
lineas 
pal 
profe """

## One line

#List - Listas Nos sirven para guardar una coleccion de datos
"""lista = [1, 2, 3, 4, 5]
names = ["delvis", "Ivan", "Sofia","Andreina"]
print("Variables de listas:")
print(type(lista))
print(type(names))
print(names)

#tuple - Tuplas Nos sirven para guardar una coleccion de datos
tupla = (1, 2, 3, 4, {"delvis", "Ivan", "Sofia","Andreina"}, [1, 2, 3, 4, 5]) # Las tuplas son inmutables
print("Variables de tuplas:")
print(type(tupla))

#dict - Diccionarios Nos sirven para guardar una coleccion de datos
diccionario = {"name": "delvis", "age": 20, "city": "Css"}
print("Variables de diccionarios:")
print(type(diccionario))"""

"Ejercicio 1:"

edad = 20
tiene_boleto = True

puede_entrar = (edad >= 18) and (tiene_boleto == True)
print(puede_entrar)

"Ejercicio 2:"

promedio = 8.5
distancia_km = 60

califica_beca = (promedio >= 9) or (distancia_km >= 50)
print(califica_beca)

"Ejercicio 3:"

rol = "editor"
esta_activo = True

tiene_acceso_admin = (rol == "admin") or (rol == "editor") and (esta_activo == True)  
print(tiene_acceso_admin)

"Ejercicio 4:"

temp = 35

es_temperatura_peligrosa = not (temp >= 20 and temp <= 30)
print(es_temperatura_peligrosa)



## convertir varias lineas en comentario shift + alt + a