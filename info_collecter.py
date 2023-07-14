import argparse, logging
from giaogiao import handler_mdl


def banner():
    ban_ner = '''
        db    db d8b   db .d888b. d8888b. d888888b 
        `8b  d8' 888o  88 88   8D 88  `8D `~~88~~' 
         `8bd8'  88V8  88 `VoooY' 88oobY'    88    
           88    88 V8o88 .d~~~b. 88`8b      88    
           88    88  V888 88   8D 88 `88.    88    
           YP    VP   V8P `Y888P' 88   YD    YP    
    '''
    print(ban_ner)


def start():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--moudle', dest='moudle', type=str, help='模块选择')
    parser.add_argument('-u', '--url', dest='url', type=str, help='域名')
    parser.add_argument('-i', '--ip', dest='ip', type=str, help='ip或者ip范围')
    parser.add_argument('-p', '--port', dest='port', type=str, help='端口范围')
    parser.add_argument('-t', '--thread', dest='thread', type=int, default=3, help='线程数默认3')
    moudle = parser.parse_args().moudle
    url = parser.parse_args().url
    ip = parser.parse_args().ip
    port = parser.parse_args().port
    thread_num = parser.parse_args().thread
    # print(moudle)
    handler_mdl.handle(moudle, url, ip, port, thread_num)


if __name__ == '__main__':
    try:
        banner()
        logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
        start()
    except KeyboardInterrupt:
        print('good game=_=')
