# Bucle FOR usando list
notas_alumnos = [17,15,12,5]
print("nota 1: ", notas_alumnos[0])
print("nota 2: ", notas_alumnos[1])

for nota in notas_alumnos:
    print("nota: ", nota)

# Bucle FOR con Dictionaries
usuario_1 = {"user":"admin","id":1}
usuario_2 = {"user":"invitado","id":2}
usuarios = [usuario_1, usuario_2]
for usuario in usuarios:
    print("Usuario: ", usuario["user"] + " "+str(usuario["id"]))

search_usuario = 2
for usuario in usuarios:
    if usuario["id"] == search_usuario:
        print("Usuario Encontrado: ", usuario["user"])


# Bucle FOR usando RANGE
for usuario in range(1,5):
    print("Usuario ", usuario)


# Bucle WHILE
contador = 1
while contador < 5: # Condicion que sea menor a 11 es True
    print("Ejercicio ", contador)
    #if contador == 3:
    #    break
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
for seccion in range (1,3):
    for alumno in range (1,2):
        print("Alumno: ", alumno)
    print("Seccion: ", seccion)


