#!/usr/bin/python3
"""
Simple HTTP Server
Jesus M. Gonzalez-Barahona and Gregorio Robles
{jgb, grex} @ gsyc.es
TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
"""
import socket
import random
# Create a TCP objet socket and bind it to a port
# We bind to 'localhost', therefore only accepts connections from the
# same machine
# Port should be 80, but since it needs root privileges,
# let's use one above 1024
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(('localhost', 1234))
# Queue a maximum of 5 TCP connection requests
mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
# (in an infinite loop)
boolean = True

try:
    
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('Request received:')
        peticion = recvSocket.recv(2048).decode("utf-8", "strict")
        print(peticion)
        numero = peticion.split()[1][1:]
        if numero == "favicon.ico":
            recvSocket.send(bytes("HTTP/1.1 404 Not Found\r\n\r\n" +
                            "<html><body><h1>Not Found</h1></body></html>" +
                            "\r\n", "utf-8"))
            recvSocket.close()
            continue
        try:
            if boolean is True:
                sumando = int(numero)
                boolean = False
                recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                                "<html><body><h1>El primer numero es: </h1>" +
                                str(sumando) + "<p>Introduce otro numero </p></body></html>" +
                                "\r\n", "utf-8"))
                recvSocket.close()
            else:
                suma = sumando + int(numero)
                boolean = True
                recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                                "<html><body>El resultado de la suma es " +
                                str(sumando) + "+" + numero + "=" + str(suma) +
                                "</body></html>" + "\r\n", "utf-8"))
                recvSocket.close()
        except ValueError:
            boolean = True
            recvSocket.send(bytes("HTTP/1.1 404 Not Found\r\n\r\n" +
                            "<html><body><h1>Error, introduce un numero. </h1>" +
                            "</body></html>" + "\r\n", "utf-8"))
            recvSocket.close()
except KeyboardInterrupt:
    print("Closing binded socket")
mySocket.close()
