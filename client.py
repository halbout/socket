import socket

try:
    BYE = "bye"
    ARRET = "arret"
    message = ""
    data = ""
    client_socket = socket.socket()
    client_socket.connect(('127.0.0.1', 10000))

    while message != BYE and data != BYE and message != ARRET and data != ARRET:
        message = input("")
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print(data)

    client_socket.close()

except KeyboardInterrupt:
    print("La connexion au serveur a été interrompue")

except ConnectionResetError:
    print("La connexion au serveur a été interrompue")