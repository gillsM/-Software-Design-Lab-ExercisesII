import socket

# Create a server socket

serverSocket = socket.socket()

print("Server socket created")

ip = "127.0.0.1"

port = 35491

serverSocket.bind((ip, port))

print("Server socket bound with with ip {} port {}".format(ip, port))

serverSocket.listen()

# Server incoming connections "one by one"

count = 0

while (True):

    (clientConnection, clientAddress) = serverSocket.accept()

    count = count + 1

    print("Accepted {} connections so far".format(count))

    # read from client connection

    while (True):

        data = clientConnection.recv(1024)

        print(data)

        if (data != b''):
            msg1 = "Hi Client! Read everything you sent"

            msg1Bytes = str.encode(msg1)

            msg2 = "Now I will close your connection"

            msg2Bytes = str.encode(msg2)

            clientConnection.send(msg1Bytes)

            clientConnection.send(msg2Bytes)

            print("Connection closed")

            break
