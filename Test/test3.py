from urllib import request
from urllib import parse


# res = request.urlretrieve("http://www.baidu.com",'baidu.html')
# urlcode 函数用法
# url = 'https://www.baidu.com/s'
# params = {'wd':'赵家庆'}
# qs = parse.urlencode(params)
# print(qs)
# url1 = url + "?&" +qs
# print(url1)
# res = request.urlopen(url1)
# print(res.read())

# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}
# url = 'http://www.baidu.com'
# res = request.Request(url, headers=headers,)
# res1 = request.urlopen(res)
# print(res1.read())

# using proxy
url = 'http://httpbin.org/ip'
response = request.urlopen(url)
print(response.read())

proxy = {'http': 'http://127.0.0.1:10809',
         'https':'https://127.0.0.1:10809'}
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}
# 1. 构建代理handler
handler = request.ProxyHandler(proxy)
#  2. 使用上面handler创建opener
opener = request.build_opener(handler)
request.install_opener(opener)
# 3. 发送前准备
res = request.Request(url,headers=header)
Res = request.urlopen(res)
print(Res.read())




