# Funciones de tiempo

# Son funciones que nos permiten trabajar con fechas y horas en python

import time as tm

#.localtime() Devuelve la hora local como una tupla de tiempo

actualTm = tm.localtime() #Devuelve la hora local como una tupla de tiempo
print(f"Hora local: {actualTm}")

#Ahora de lo anterior sacaremos lo que nos interesa

year = actualTm.tm_year
month = actualTm.tm_mon
day = actualTm.tm_mday
print(f"Año: {year}, Mes: {month}, Dia: {day}")

#struct_time es una tupla con 9 elementos que representan una fecha y hora, vamos a construir una fecha especifica

specific_date = tm.struct_time((2023,12,25,10,30,0,0,0,0)) #Año, mes, dia, hora, minuto, segundo, dia de la semana(0-6), dia del año(1-366), horario de verano(-1,0,1)
print(f"Fecha especifica: {specific_date}")

"""
    +------------------------------------------------------------+
    |           Propiedades de la estructura de tiempo           |
    +------------+-----------------------------------------------+
    | Propiedad  | Descripción                                   |
    +------------+-----------------------------------------------+
    | tm_year    | Año (por ejemplo, 2024).                      |
    | tm_mon     | Mes del año (1-12).                           |
    | tm_mday    | Día del mes (1-31).                           |
    | tm_hour    | Hora (0-23).                                  |
    | tm_min     | Minuto (0-59).                                |
    | tm_sec     | Segundo (0-61, permite 60 y 61 para segundos  |
    |            | intercalares).                                |
    | tm_wday    | Día de la semana (0-6, donde 0 es lunes).     |
    | tm_yday    | Día del año (1-366, donde 1 es 1 de enero).   |
    | tm_isdst   | Horario de verano (1 si está en efecto, 0 si  |
    |            | no, -1 si no se sabe).                        |
    +------------+-----------------------------------------------+
"""

#Formatear fechas y horas .striftime()
formatted_time = tm.strftime("%Y-%m-%d %H:%M:%S", actualTm)#Formato: Año-Mes-Día Hora:Minuto:Segundo (Se ve raro pero es asi)
print("Fecha y hora formateada:", formatted_time)

