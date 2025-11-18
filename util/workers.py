from data.state import naomi
import threading

def create_workers(target):
    for _ in range(naomi.THREADS):
        t = threading.Thread(target=target)
        t.daemon = True
        t.start()

def create_jobs():
    for x in naomi.JOB_NUMBER:
        naomi.queue.put(x)

    naomi.queue.join()