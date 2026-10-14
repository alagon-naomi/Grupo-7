notas=[14,16,11,18,13]
promedio=sum(notas)/len(notas)

print("promedio",promedio)
print("nota maxima",max(notas))
print("nota minima",min(notas))
print("Cantidad de notas:", len(notas))
print("Promedio general:", promedio)

# 1. Contar cuántos aprobaron y cuántos jalaron (nota mínima 11)
aprobados = 0
desaprobados = 0

for nota in notas:
    if nota >= 11:
        aprobados = aprobados + 1
    else:
        desaprobados = desaprobados + 1

print("Total de aprobados:", aprobados)
print("Total de desaprobados:", desaprobados)

# 2. Dibujar un gráfico simple con asteriscos (*)
print("\nGrafico de notas:")
for nota in notas:
    print(nota, "*" * nota)