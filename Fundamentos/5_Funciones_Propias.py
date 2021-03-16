def mostrar_segundos_por_dia():
    horas = 24
    minutos = horas * 60
    segundos = minutos * 60
    print(segundos)

mostrar_segundos_por_dia()

def mostrar_segundos_por_dia(dias):
    horas = dias*24
    minutos = horas * 60
    segundos = minutos * 60
    print(segundos)

mostrar_segundos_por_dia(7)
mostrar_segundos_por_dia(20)
mostrar_segundos_por_dia(360)

def convertir_dias_a_segundos(dias):
    horas = dias*24
    minutos = horas * 60
    segundos = minutos * 60
    return segundos

total_segundos = convertir_dias_a_segundos(7)
total_mili_segundos = total_segundos * 1000
print(total_mili_segundos)

