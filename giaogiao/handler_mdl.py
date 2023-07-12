from . import bdcollecter, zdcollecter, pcollecter


def handle(moudle, url, ip, port, thread_num):
    if moudle == 'nbip':
        bdcollecter.name_ip(ip)
    elif moudle == 'fofa':
        bdcollecter.fofa_666(url)
    elif moudle == 'icmp':
        if '/' in ip:
            for i in range(int(ip.split('/')[0].split('.')[3]), int(ip.split('/')[1]) + 1):
                zdcollecter.icmp_scan(ip.split('.')[0] + '.' + ip.split('.')[1] + '.' + ip.split('.')[2] + '.' + str(i))
        else:
            zdcollecter.icmp_scan(ip)
        print('icmp扫描完成')
    elif moudle == 'tcp':
        if '/' in ip:
            for i in range(int(ip.split('/')[0].split('.')[3]), int(ip.split('/')[1]) + 1):
                zdcollecter.tcp_scan(ip.split('.')[0] + '.' + ip.split('.')[1] + '.' + ip.split('.')[2] + '.' + str(i))
        else:
            zdcollecter.tcp_scan(ip)
        print('tcp扫描完成')
    elif moudle == 'udp':
        if '/' in ip:
            for i in range(int(ip.split('/')[0].split('.')[3]), int(ip.split('/')[1]) + 1):
                zdcollecter.udp_scan(ip.split('.')[0] + '.' + ip.split('.')[1] + '.' + ip.split('.')[2] + '.' + str(i))
        else:
            zdcollecter.udp_scan(ip)
        print('udp扫描完成')
    elif moudle == 'pscan':
        if '-' in port:
            for i in range(int(port.split('-')[0]), int(port.split('-')[1]) + 1):
                pcollecter.port_scan(ip, port, thread_num)
        print('端口扫描完成')
