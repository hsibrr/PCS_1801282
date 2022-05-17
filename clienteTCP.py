import argparse
import socket
from cryptography.fernet import Fernet

description ="""modo de uso
    client.py -msj "Mensaje a enviar"""
parser = argparse.ArgumentParser (description='Port scanning',
                                epilog=description,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument ("-msj", metavar='MSJ', dest="msj",
                    help="mensaje a enviar",required=True)
params = parser.parse_args ()

#se comienza a cifrar
clave = Fernet.generate_key ()
cipher_suite = Fernet (clave)

#se almacena la clave
file = open ('clave.key', 'wb')
file.write (clave)
file.close ()
mensaje = params.msj
mensajeBytes = mensaje.encode ()

#se cifra el mensaje
msj_cifrado = cipher_suite.encrypt (mensajeBytes)
print ("Mensaje enviado:\n",mensaje)
#Preparamos los datos de la conexión
TCP_IP = 'l27.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 2048

#se establece la conexión
s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
s.connect ( (TCP_IP, TCP_PORT))
s.send (msj_cifrado)
respuesta = s.recv (BUFFER_SIZE).decode ()
s.close ()
print ("Respuesta recibida:", respuesta)