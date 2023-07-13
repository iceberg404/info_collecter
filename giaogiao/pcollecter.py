import queue, threading, socket, sys


class PortScanner(threading.Thread):
    def __init__(self, portqueue, ip, timeout=3):
        threading.Thread.__init__(self)
        self._portqueue = portqueue
        self._ip = ip
        self._timeout = timeout

    def run(self):
        while True:
            if self._portqueue.empty():
                break
            port = self._portqueue.get(timeout=0.5)
            try:
                s = socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(self._timeout)
                result_code = s.connect_ex((self._ip, port))
                # sys.stdout.write("[%d]Scan\n" % port)
                # 若端口开放则会返回0
                if result_code == 0:
                    sys.stdout.write("[%d] OPEN\n" % port)
            except Exception as e:
                print(e)
            finally:
                s.close()


def port_scan(ip, port, thread_num):
    # 端口列表
    portList = []
    portList.append(port)
    threads = []
    portqueue = queue.Queue()
    for port in portList:
        portqueue.put(port)
    for t in range(thread_num):
        threads.append(PortScanner(portqueue, ip, timeout=3))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
