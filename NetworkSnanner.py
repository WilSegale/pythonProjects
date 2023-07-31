from threading import *
from DontEdit import *
from queue import *
import argparse
import socket



 


#NUMBER OF THREADS
N_THREADS = 20000

#THREAD QUEUE
q = Queue()
print_lock = Lock()

def port_scan(port):
    #Scan a port on the global var 'host'
    try:
        s = socket.socket()
        s.connect((host,port))
    except:
        with print_lock:
            print(f"{host:15}:{port:5} is {RED} {DIM} CLOSED {RESET}",end='\r')
    else:
        with print_lock:
            print(f"{NORMAL} {host:15}:{port:5} is {BRIGHT} {GREEN} OPEN {RESET}")
    finally:
        s.close()

def scan_thread():
    global q
    while True:
        #get teh port number for the queue
        worker = q.get()
        # scan the port number
        port_scan(worker)
        #tells the queue that the scanning for the port is done
        q.task_done()

def main(host,ports):
    global q
    for t in range(N_THREADS):
        # for each thread, start it
        t = Thread(target=scan_thread)
        #when demon is set to true the thread will end
        t.daemon = True
        #start the demon
        t.start()
    
    for worker in ports:
        # for each port put the port into the queue
        # to start the scan
        q.put(worker)
    
    #wait for the threads to finish
    q.join()

if __name__ == "__main__":
    #parse some paramerters passed
    parsr = argparse.ArgumentParser(description="Port Scanner")
    parsr.add_argument("host", help="Host to scan")
    parsr.add_argument("--ports","-p", dest="port_range", default="0-65535", help="Port range to scan")
    args = parsr.parse_args()
    host, port_range = args.host, args.port_range

    start_port, end_port = port_range.split("-")
    start_port, end_port = int(start_port), int(end_port)

    ports = [ p for p in range(start_port, end_port)]

    main(host, ports)