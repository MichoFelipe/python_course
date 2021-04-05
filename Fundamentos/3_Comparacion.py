# Comparacion Simple
edad = 11
if edad == 18 :
    print("Aure ya es adulto")

# Comparacion con dos variables
edad = 9
altura = 1.35
if edad > 10 and altura > 1.3:
    print("Ingresa al juego")

# Comparacion Multiple
noche = input("Ya es de noche? si/no: ")
if noche == 'si':
    print("Cambiar movil a modo nocturno")

tienes_movil = input("Tienes móvil? si/no: ")
if tienes_movil == 'si':
    print("Bajate esta nueva app ahora mismo!")
else:
    print("Tenemos una promoción de un nuevo móvil para tí.")


tipo_movil = input("Que tipo de móvil deseas? (Samsung/Iphone/Otro): ")
if tipo_movil == 'Samsung':
    print("Tenemos el nuevo Samsung Galaxy 2021 con 64gb de memoria")
elif tipo_movil == 'Iphone':
    print("Acabamos de recibir el Iphone 12 hace una semana!")
else:
    print("Tenemos para tí en modelo Huawei, LG y Xiaomi!")


edad = int(input("Ingrese tu edad: "))
altura = float(input("Ingrese tu altura: "))
if( (edad > 8) and (altura>1.10) ):
    print("Puede acceder al juego")