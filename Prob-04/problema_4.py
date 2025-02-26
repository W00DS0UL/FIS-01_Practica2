import math

def problema_4():
    while True:
        try:
            separacion_inicial = float(input("Ingrese la separación inicial en metros: "))
            if separacion_inicial < 0:
                print("Error: La separación inicial no puede ser negativa.")
                continue

            aceleracion_car_01 = float(input("Ingrese la aceleración del carrito 1 en m/s²: "))
            if aceleracion_car_01 < 0:
                print("Error: La aceleración no puede ser negativa.")
                continue

            aceleracion_car_02 = float(input("Ingrese la aceleración del carrito 2 en m/s²: "))
            if aceleracion_car_02 < 0:
                print("Error: La aceleración no puede ser negativa.")
                continue

            break
        except ValueError:
            print("Error: Ingrese valores numéricos válidos.")

    tiempo = 3  # segundos
    distancia_recorrida_car_01 = 0.5 * aceleracion_car_01 * tiempo**2
    distancia_recorrida_car_02 = 0.5 * aceleracion_car_02 * tiempo**2
    separacion_final = abs(separacion_inicial - (distancia_recorrida_car_01 + distancia_recorrida_car_02))
    cruzaron = separacion_final < 0
    a_total = 0.5 * (aceleracion_car_01 + aceleracion_car_02)

    if a_total == 0:
        tiempo_cruce = float('inf')
    else:
        tiempo_cruce = math.sqrt(separacion_inicial / a_total)

    print(f"La distancia de separación luego de {tiempo} segundos es de {separacion_final:.2f} metros")
    if cruzaron:
        print("Nota: Los carritos ya se cruzaron y ahora se están alejando.")
    else:
        print(f"El tiempo en el que los carritos se cruzan es de {tiempo_cruce:.2f} segundos")

problema_4()
