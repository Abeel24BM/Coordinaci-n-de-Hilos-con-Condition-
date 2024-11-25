import threading

contador = 1
iteraciones = 5
condicion = threading.Condition()

# Función para la tarea de preparación
def preparacion():
    global contador
    for i in range(1, iteraciones + 1):
        with condicion:
            condicion.wait_for(lambda: contador == 1)
            print(f"Preparación {i} completada")
            contador = 2
            condicion.notify_all()

# Función para la tarea de procesamiento
def procesamiento():
    global contador
    for i in range(1, iteraciones + 1):
        with condicion:
            condicion.wait_for(lambda: contador == 2)
            print(f"Procesamiento {i} completado")
            contador = 3
            condicion.notify_all()

# Función para la tarea de empaque
def empaque():
    global contador
    for i in range(1, iteraciones + 1):
        with condicion:
            condicion.wait_for(lambda: contador == 3)
            print(f"Empaque {i} completado")
            contador = 1
            condicion.notify_all()


hilo_preparacion = threading.Thread(target=preparacion)
hilo_procesamiento = threading.Thread(target=procesamiento)
hilo_empaque = threading.Thread(target=empaque)

hilo_preparacion.start()
hilo_procesamiento.start()
hilo_empaque.start()

hilo_preparacion.join()
hilo_procesamiento.join()
hilo_empaque.join()

print("Secuencia de producción completada.")
