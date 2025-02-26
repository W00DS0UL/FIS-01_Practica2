def problema_1():
    velocidad_impulso_nervioso = 100  # m/s
    
    while True:
        try:
            altura_persona = float(input('Ingrese su altura en metros: '))
            if altura_persona <= 0:
                print("Error: La altura debe ser un número positivo.")
                continue
            break
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")
    
    tiempo_impulso_nervioso = altura_persona / velocidad_impulso_nervioso
    print(f'El tiempo que tarda en llegar al cerebro es de {tiempo_impulso_nervioso:.6f} segundos')

problema_1()
