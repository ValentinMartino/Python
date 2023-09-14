este_curso = 1.5
otros_rapido = 2.5
otros_lento = 7
otros_promedio = 4
este_curso_crudo  = 3.5
otros_promedio_crudo= 5

#apartado A
#se calcula la diferencia para el curso mas rapido
porcentaje_total = (otros_rapido * 100.0) / este_curso
dif_porcentaje = porcentaje_total - 100.0
print(f"El curso mas rapido de los otros es: +{dif_porcentaje}% mas lento")

#se calcula la diferencia para el curso mas lento
porcentaje_total = (otros_lento * 100.0) / este_curso
dif_porcentaje = porcentaje_total - 100.0
print(f"El curso mas lento de los otros es: +{dif_porcentaje}% mas lento")

#se calcula la diferencia para el promedio de los cursos
porcentaje_total = (otros_promedio * 100.0) / este_curso
dif_porcentaje = porcentaje_total - 100.0
print(f"El promedio de los otros es: +{dif_porcentaje}% mas lento")

#-------------------------------------------------------------------------------------------------------------------------------------
#apartado B
prom_tiempo_vacio = 100 - (este_curso/este_curso_crudo)*100
print(f"la cantidad de material eliminado en este curso en la edicion es de: +{prom_tiempo_vacio}%")

prom_tiempo_vacio = 100 - (otros_promedio/otros_promedio_crudo)*100
print(f"la cantidad de material eliminado en los otros cursos en la edicion es de: +{prom_tiempo_vacio}%")

#------------------------------------------------------------------------------------------------------------------------------------
#apartado C
horas_otros_cursos = (otros_promedio * 10.0) / este_curso
print(f"10 horas en este curso equivalen en promedio a: +{horas_otros_cursos} en otros cursos")





