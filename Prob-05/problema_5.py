import time
import os

def problema_5():
    # Variables de escala modificables
    PIXELES_POR_KM = 1  # Ajusta cuántos píxeles representan 1 km
    SEGUNDOS_POR_HORA = 60  # Ajusta cuántos segundos representan 1 hora

    while True:
        try:
            velocidad_tren = float(input("Ingrese la velocidad del tren en km/h: "))
            desaceleracion_tren = float(input("Ingrese la desaceleración del tren en m/s² (valor negativo): "))
            aceleracion_tren = float(input("Ingrese la aceleración del tren en m/s²: "))
            tiempo_parada_tren_minutos = float(input("Ingrese el tiempo de parada del tren en minutos: "))

            if desaceleracion_tren >= 0:
                print("Error: La desaceleración debe ser un valor negativo.")
                continue
            if tiempo_parada_tren_minutos < 0:
                print("Error: El tiempo de parada no puede ser negativo.")
                continue

            break
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")

    # Conversión de unidades y cálculo de tiempos
    vf1, vi2 = 0, 0  # Velocidades finales e iniciales en m/s
    vi1 = velocidad_tren * (1000 / 3600)  # Conversión de km/h a m/s
    vf2 = vi1  # Mismo valor porque el tren vuelve a la misma velocidad

    tiempo_perdido_01 = abs((vf1 - vi1) / desaceleracion_tren)
    tiempo_perdido_02 = abs((vf2 - vi2) / aceleracion_tren)
    tiempo_perdido_total = tiempo_perdido_01 + (tiempo_parada_tren_minutos * 60) + tiempo_perdido_02

    print(f"\nEl tiempo perdido por la parada del tren es de {tiempo_perdido_total:.2f} segundos")

problema_5()
