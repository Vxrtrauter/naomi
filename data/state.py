from dataclasses import dataclass, field
from queue import Queue
import socket

THREADS = 2
JOB_NUMBER = [1, 2]

@dataclass
class Naomi:

    THREADS: int = 2
    JOB_NUMBER: list[int] = field(default_factory=lambda: [1, 2])

    s: socket.socket = field(default_factory=socket.socket)
    queue: Queue = field(default_factory=Queue)

    host: str = ""
    port: int = 0
    connections: list = field(default_factory=list)
    addresses: list = field(default_factory=list)

naomi = Naomi()