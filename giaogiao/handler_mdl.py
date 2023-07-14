from . import bdcollecter, zdcollecter, pcollecter


def handle(moudle, url, ip, port, thread_num):
    if moudle == 'nbip':
        bdcollecter.name_ip(ip)
    elif moudle == 'fofa':
        bdcollecter.fofa_666(url)
    elif moudle == 'icmp':
        zdcollecter.ip_scan(ip, thread_num, moudle)
        print('icmp扫描完成')
    elif moudle == 'tcp':
        zdcollecter.ip_scan(ip, thread_num, moudle)
        print('tcp扫描完成')
    elif moudle == 'udp':
        zdcollecter.ip_scan(ip, thread_num, moudle)
        print('udp扫描完成')
    elif moudle == 'pscan':
        pcollecter.port_scan(ip, port, thread_num)
        print('端口扫描完成')
