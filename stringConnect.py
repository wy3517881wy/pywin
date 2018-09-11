import re
import urllib
import urllib.request
from collections import deque

url = "https://auth.alipay.com/login/index.htm"

queue = deque()
visited = set()
total_count = 1
queue.append(url)

while queue:
    url = queue.popleft()
    visited |= {url}
    print("正在抓取第 " + str(total_count) + " 个, " + url)
    total_count += 1
    urllop = urllib.request.urlopen(url, timeout=1)
    

    if "htm" not in urllop.getheader('Content-Type'):
        print(urllop + " 不是html页面，忽略！")
        continue
    try:
        data = urllop.read().decode("utf-8")
    except Exception as e:
        print(e)
        continue
    count_per_page = 0

    linkre = re.compile('href="(.+?)"')
    for x in linkre.findall(data):
        if 'https://a.alipayobjects.com/' in x and x not in visited:
            count_per_page += 1
            # queue.append(x)  # 注意调试的时候注释本行,以免对服务器造成压力
            print("加入待爬页面：" + x)
    print("本页面共加入待爬页面:" + str(count_per_page))




