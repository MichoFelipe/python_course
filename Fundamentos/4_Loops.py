# Bucle FOR
for contador in range(1,11):
    print("Tarea ", contador)


# Bucle WHILE
contador = 1
while contador < 11: # Condicion que sea menor a 11 es True
    print("Ejercicio ", contador)
    contador = contador + 1

num_jugadores = 0
respuesta = 'y'
while respuesta == 'y':
    num_jugadores = num_jugadores + 1
    print("Numero total de jugadores es: ", str(num_jugadores))
    respuesta = input("Deseas invitar a otro jugador? y/n: ")
    if respuesta == 'y':
        nombre = input("Ingrese el nombre del jugador?: ")
        print("Bienvenido jugador ", nombre)

print("El numero de jugadores al final es: ", str(num_jugadores))

# Bucle dentro de otro bucle
for seccion in range (1,5):
    for alumno in range (1,9):
        print("Alumno: ", alumno)
    print("Seccion: ", seccion)


