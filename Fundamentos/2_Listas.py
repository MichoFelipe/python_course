
# Muchas variables
jugador_1 = "Juan"
jugador_2 = "Luis"
jugador_3 = "Jorge"
jugador_4 = "Paco"

# Usando listas solo creamos una variable
lista_jugadores = ["Juan", "Luis", "Jorge", "Paco"]

# Obtener acceso usando índices
print(lista_jugadores[1])
print(lista_jugadores[2])

# Indice fuera de rango
# print(lista_jugadores[4])

notas_alumnos = [17,15,12,5]
print(notas_alumnos)

# Borrar dato de lista usando índice
del(notas_alumnos[3])

# Agregar una nueva nota
notas_alumnos.append(15)
print(notas_alumnos)

# Funciones con listas
print("Suma: ",sum(notas_alumnos))
print("Tamaño: ",len(notas_alumnos))

# Multiplicar valores de la lista usando índices
print("Notas con peso: Practicas: ", 0.10 * notas_alumnos[0])
print("Notas con peso: Parcial: ", 0.30 * notas_alumnos[1])
print("Notas con peso: Exposición: ", 0.20 * notas_alumnos[2])
print("Notas con peso: Final: ", 0.40 * notas_alumnos[3])

## DICTIONARIES

my_data = {"nombre":"Juan", "distrito":"Pueblo Libre"}
print("nombre: ", my_data["nombre"])
print("distrito: ", my_data["distrito"])
 
print("keys: ", my_data.keys())

# Agregar nuevo elemrnto a Dictionary
my_data["apellido"] = "Perez"
print("apellido: ", my_data["apellido"])
print("keys: ", my_data.keys())

# Cast dictionary a list
my_keys = list(my_data.keys())
print("my_keys: ", my_keys)
print("my_keys: ", my_keys[0])


