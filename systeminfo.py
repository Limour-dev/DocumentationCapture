import socket
import uuid

hostname = socket.gethostname()

ip = socket.gethostbyname(hostname)

def get_mac_address():
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0,11,2)])

mac = get_mac_address()

def get_systeminfo():
    return f'{mac}|{hostname}@{ip}'
