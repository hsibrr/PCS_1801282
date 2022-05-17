import argparse
import socket
from cryptography.fernet import Fernet

#se preparan los datos de la conexion
TCP_IP = 'l27.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 2048

#se establece conexion
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
(conn,addr) = s.accept()
print ("Direccion de conexion: ", addr)
while True:
    msj_cifrado = conn.recv(BUFFER_SIZE)
    conn.send(b"Enterado, bye")
    break
conn.close()

#se genera el objeto para cifrar
file = open('clave.key', 'rb') #se abre en bytes rb
clave = file.read() #la llave sera en bytes
file.close()
cipher_suite = Fernet (clave)

mensajeBytes = cipher_suite.decrypt(msj_cifrado,None)
mensaje = mensajeBytes.decode()
print("Mensaje recibido:\n", mensaje)

