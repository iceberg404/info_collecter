from bs4 import BeautifulSoup
import base64, json, requests, re

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
    'Accept-Encoding': 'gzip, deflate, br',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cookie': ''
}


def name_ip(ip):
    realurl = 'https://site.ip138.com/' + ip
    r = requests.get(url=realurl, headers=headers)
    pattern = re.compile('<li><span class="date">.*?<li>', re.S)
    result = re.findall(pattern, r.text)
    unique_urls = set()  # 创建一个空的集合用于存储去重后的结果
    for line in result:
        soup = BeautifulSoup(line, 'lxml')
        url = soup.a.attrs['href']
        unique_urls.add(url.strip('/'))
    # 打印去重后的结果
    for url in unique_urls:
        print(url)
    if len(unique_urls) > 20:
        print('解析数量超过20个，可能是cdn服务器')
    else:
        print('可能是真的服务器')


def fofa_666(url):
    url1 = "https://fofa.info/api/v1/search/all?email=@qq.com&key=&fields=domain,host,port,protocol&size=10000&qbase64="
    query = base64.b64encode(url.encode('utf-8'))
    realurl = url1 + str(query.decode('utf-8'))
    print(realurl)
    r = requests.get(headers=headers, url=realurl)
    result_array = json.loads(r.content)
    # print(result_array)
    url_list = [item[1] for item in result_array['results']]
    unique_urls = set()  # 创建一个空的集合用于存储去重后的结果
    for line in url_list:
        if line.startswith("https://"):
            line = line[len("https://"):]  # 去掉起始部分
        elif line.startswith("http://"):
            line = line[len("http://"):]  # 去掉起始部分
            # 判断与已有的网址的相似度，如果相似度小于阈值，则添加到集合中
        unique_urls.add(line.strip())
        for i in unique_urls:
            if url in i:
                with open('fofa.txt', 'a') as f:
                    f.write(i + '\n')
    print('已经写入当前文件夹的fofa.txt中')
