import threading

contador = 1
cond = threading.Condition()

def preparacion():
    global contador
    for i in range(1, 6):
        with cond:
            cond.wait_for(lambda: contador == 1)
            print(f"Preparación {i} completada")
            contador = 2
            cond.notify_all()

def procesamiento():
    global contador
    for i in range(1, 6):
        with cond:
            cond.wait_for(lambda: contador == 2)
            print(f"Procesamiento {i} completado")
            contador = 3
            cond.notify_all()

def empaque():
    global contador
    for i in range(1, 6):
        with cond:
            cond.wait_for(lambda: contador == 3)
            print(f"Empaque {i} completado")
            contador = 1
            cond.notify_all()


hilo1 = threading.Thread(target=preparacion)
hilo2 = threading.Thread(target=procesamiento)
hilo3 = threading.Thread(target=empaque)


hilo1.start()
hilo2.start()
hilo3.start()

hilo1.join()
hilo2.join()
hilo3.join()
