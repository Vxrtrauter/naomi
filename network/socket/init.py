import socket
from data.state import naomi

def create_socket():

    naomi.host = "0.0.0.0"
    naomi.port = 9999

    try:
        naomi.s = socket.socket()
    except socket.error as e:
        print(f"[!] Socket Exception: {str(e)}")

def bind_socket():
    print(f"[i] Binding to {naomi.host}:{naomi.port}")

    try:
        naomi.s.bind((naomi.host,naomi.port))
        print("[+] Binding Successful!")
        naomi.s.listen(5)

    except socket.error as e:
        print(f"[!] Socket Exception: {str(e)}")
        print("[i] Retrying...")
        bind_socket()
