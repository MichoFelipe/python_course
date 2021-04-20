
## CONCEPTOS BÁSICOS DE STRING
saludo = 'Hola'
print("tamaño del texto: ", len(saludo))
# Obtener caracteres de la palabra 'Hola'
# Palabra:      Hola
# Posiciones:   0123
print("H: ", saludo[0])
print("o: ", saludo[1])
print("a: ", saludo[3])
#print("ERROR: ", saludo[4]) # Indice fuera de rango.

## Concatenar Strings
nombre = "Juan"
apellido = "Perez"
nombre_completo = nombre + "_" + apellido
print(nombre_completo)


## PARTE DE UN STRING
saludo = 'Hola'
#         0123                  # Indices de la palabra Hola
print("ola: ", saludo[1:4])     # Empieza en 1 hasta el 4, pero no incluye el 4
print("Hol: ", saludo[0:3])     # Empieza en 0 hasta el 3, pero no incluye el 3


# OMITIR INDICE EN PARTE DE UN STRING
saludo = 'Hola'
#         0123                  # Indides de la palabra Hola
print("Ho: ", saludo[:2])       # Si omite el primer número, se usa el inicio del String
print("la: ", saludo[2:])       # Si omite el segundo número, se usa el fin del String


# UNIR PARTES DE UN STRING
a = 'Hi!'
b = 'Hello'

## Asigna a 'c' los primermos dos caracteres de 'a' seguido por los 2 últimos caracteres de 'b'.
c = a[:2] + b[len(b) - 2:]
#¿Que valor imprime 'c'?
print("Valor de C: ",c)


## PYTHON STRING LOOPS
saludo = 'Hola'
resultado = ''
# len(variable): Retorna el tamaño de la variable.
print("Tamaño variable Saludo: ", len(saludo))
# range(n): retorna la secuencia de valores-> 0,1,2,3, ... n-1
for i in range(len(saludo)):
    # Hacer algo con saludo[i]
    # Aqui sólo agregaremos cada caracter sobre la variable resultado
    resultado = resultado + saludo[i]


if False:
    print("Resultado usando range-len: ", resultado)

    # Otra forma de iterar/recorrer un String es recorriendo por cada caracter.
    saludo = 'Hola'
    resultado = ''
    for ch in saludo:
        # De esta forma, empezamos por cada caracter a través del String -> H, o, l, a 
        resultado = resultado + ch

    print("Resultado usando caracteres: ", resultado)