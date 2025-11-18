from network.socket.init import create_socket, bind_socket
from network.socket.connections import list_connections, accept_connections
from interface.shell import get_target, send_target_commands
from util.workers import create_jobs, create_workers
from data.state import naomi

def start_shell():
    while True:
        cmd = input("shell>")
        if cmd == "":
            cmd = input("shell>")
        if cmd == "list":
            list_connections()
        elif "select" in cmd:
            connection = get_target(cmd)
            if connection != None:
                send_target_commands(connection)
        elif cmd is not "":
            print(f"Invalid Command: {cmd}")

def work():
    while True:
        x = naomi.queue.get()
        if x == 1:
            create_socket()
            bind_socket()
            accept_connections()
        if x == 2:
            start_shell()
        naomi.queue.task_done()

if __name__ == "__main__":
    create_workers(work)
    create_jobs()
