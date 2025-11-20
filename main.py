from network.socket.init import create_socket, bind_socket
from network.socket.connections import accept_connections
from shell.shell import shell
from util.workers import create_jobs, create_workers
from data.state import naomi

def work():
    while True:
        x = naomi.queue.get()
        if x == 1:
            create_socket()
            bind_socket()
            accept_connections()
        if x == 2:
            shell()
        naomi.queue.task_done()

if __name__ == "__main__":
    create_workers(work)
    create_jobs()
