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

