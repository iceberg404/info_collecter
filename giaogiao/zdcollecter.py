import queue
import time
from random import randint
from scapy.layers.inet import IP, ICMP, TCP, UDP
from scapy.sendrecv import sr1
import threading


class scaner(threading.Thread):
    def __init__(self, ipqueue, moudle, timeout):
        threading.Thread.__init__(self)
        self._ipqueue = ipqueue
        self._timeout = timeout
        self._moudle = moudle

    def run(self):
        while True:
            if self._ipqueue.empty():
                break
            ip = self._ipqueue.get()
            if self._moudle == 'icmp':
                try:
                    ip_id = randint(1, 65535)
                    icmp_id = randint(1, 65535)
                    icmp_seq = randint(1, 65535)
                    packet = IP(dst=ip, ttl=64, id=ip_id) / ICMP(id=icmp_id, seq=icmp_seq) / b'rootkit'
                    result = sr1(packet, timeout=1, verbose=False)
                    if result:
                        for rcv in result:
                            scan_ip = rcv[IP].src
                            print(scan_ip + '--->' '[up]')
                    else:
                        print(ip + '--->' '[down]')
                except Exception as e:
                    print(e)
            if self._moudle == 'tcp':
                try:
                    dport = randint(1, 65535)  # 随机目的端口
                    packet = IP(dst=ip) / TCP(flags="A", dport=dport)  # 构造标志位为ACK的数据包
                    response = sr1(packet, timeout=1.0, verbose=0)
                    if response:
                        if int(response[TCP].flags) == 4:  # 判断响应包中是否存在RST标志位
                            time.sleep(0.5)
                            print(ip + '--->' '[up]')
                        else:
                            print(ip + '--->' '[down]')
                    else:
                        print(ip + '--->' '[down]')
                except:
                    pass
            if self._moudle == 'udp':
                try:
                    dport = randint(1, 65535)
                    packet = IP(dst=ip) / UDP(dport=80)
                    response = sr1(packet, timeout=1.0, verbose=0)
                    if response:
                        if int(response[IP].proto) == 1:
                            time.sleep(0.5)
                            print(ip + '--->' '[up]')
                        else:
                            print(ip + '--->' '[down]')
                    else:
                        print(ip + '--->' '[down]')
                except:
                    pass


def ip_scan(ip, thread_num, moudle):
    ipList = []
    if '/' in ip:
        for i in range(int(ip.split('/')[0].split('.')[3]), int(ip.split('/')[1]) + 1):
            ipList.append(ip.split('.')[0] + '.' + ip.split('.')[1] + '.' + ip.split('.')[2] + '.' + str(i))
    else:
        ipList.append(ip)
    ipqueue = queue.Queue()
    threads = []
    for ip in ipList:
        ipqueue.put(ip)
    for t in range(thread_num):
        threads.append(scaner(ipqueue, moudle, timeout=1))
    for thread in threads:
        thread.start()
        thread.join()