import time
from random import randint
from scapy.layers.inet import IP, ICMP, TCP, UDP
from scapy.sendrecv import sr1


def icmp_scan(ip):
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


def tcp_scan(ip):
    try:
        dport = randint(1, 65535)  # 随机目的端口
        packet = IP(dst=ip) / TCP(flags="A", dport=dport)  # 构造标志位为ACK的数据包
        response = sr1(packet, timeout=1.0, verbose=0)
        if response:
            if int(response[TCP].flags) == 4:  # 判断响应包中是否存在RST标志位
                time.sleep(0.5)
                print(ip + ' ' + "is up")
            else:
                print(ip + ' ' + "is down")
        else:
            print(ip + ' ' + "is down")
    except:
        pass


def udp_scan(ip):
    try:
        dport = randint(1, 65535)
        packet = IP(dst=ip) / UDP(dport=80)
        response = sr1(packet, timeout=1.0, verbose=0)
        if response:
            if int(response[IP].proto) == 1:
                time.sleep(0.5)
                print(ip + ' ' + "is up")
            else:
                print(ip + ' ' + "is down")
        else:
            print(ip + ' ' + "is down")
    except:
        pass
