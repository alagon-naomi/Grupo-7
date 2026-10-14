#agregar promedio
numeros = [10, 8, 9, 7, 7, 15, 4]
promedio = sum(numeros) / len(numeros)
print("El promedio es:", promedio)

#agregar mediana
import statistics

mediana = statistics.median(numeros)
print("La mediana es:", mediana)  # Resultado: 8.5

#agregar moda
moda = statistics.mode(numeros)
print("La moda es:", moda)

#agregar varianza
import statistics

datos = [2, 4, 6, 8, 10]
varianza_muestral = statistics.variance(datos)    # Divide entre n-1
varianza_poblacional = statistics.pvariance(datos) # Divide entre n

print("Muestral:", varianza_muestral)
print("Poblacional:", varianza_poblacional)
