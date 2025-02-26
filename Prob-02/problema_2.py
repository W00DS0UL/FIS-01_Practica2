def problema_2():
    velocidad_crecimiento_cabello = 2  # cm/mes

    while True:
        try:
            distancia_inicial_cabello = float(input('Ingrese su largo inicial de cabello en cm: '))
            if distancia_inicial_cabello < 0:
                print("Error: El largo inicial no puede ser negativo.")
                continue
            
            distancia_final_cabello = float(input('Ingrese su largo final de cabello en cm: '))
            if distancia_final_cabello < distancia_inicial_cabello:
                print("Error: El largo final no puede ser menor que el inicial.")
                continue
            break
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")

    tiempo_crecimiento_cabello = (distancia_final_cabello - distancia_inicial_cabello) / velocidad_crecimiento_cabello

    print("\nSeleccione la unidad de tiempo para la conversión:")
    opciones = ["Segundos", "Minutos", "Horas", "Días", "Semanas", "Meses", "Años"]
    conversiones = [30 * 24 * 60 * 60, 30 * 24 * 60, 30 * 24, 30, 4.345, 1, 1/12]

    for i, opcion in enumerate(opciones, 1):
        print(f"{i}. {opcion}")

    while True:
        try:
            opcion = int(input("Ingrese el número de su elección: "))
            if 1 <= opcion <= 7:
                tiempo_convertido = tiempo_crecimiento_cabello * conversiones[opcion - 1]
                unidad = opciones[opcion - 1].lower()
            else:
                raise ValueError
            break
        except ValueError:
            print("Error: Ingrese un número entre 1 y 7.")

    print(f"El tiempo estimado de crecimiento es de {tiempo_convertido:.2f} {unidad}.")

problema_2()
