import urllib.request
import urllib.parse
import json

f = open('test.txt', 'r')
f_read = f.read()
print(f_read)

#这个是百度语音识别api的地址
url = 'http://vop.baidu.com/server_api?lan=zh&cuid=34:e6:ad:da:81:f3&token=24.cac99078743ed68797e52a2c8b6a1d80.2592000.1524456073.282335-10677609'

#准备一下头
headers = {
        'Host': 'vop.baidu.com',
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
        'Contenttype': 'application/json',
        }

#还有我们准备用Post传的值，这里值用字典的形式
values = {
    'format':'amr',
    'rate':8000,
    'channel':1,
    'cuid':'34:e6:ad:da:81:f3',
    'token':'24.cac99078743ed68797e52a2c8b6a1d80.2592000.1524456073.282335-10677609',
    'lan':'zh',
    'len':5734,
    'speech':f_read,
    }

#将字典格式化成能用的形式
data = urllib.parse.urlencode(values).encode('utf-8')

#创建一个request,放入我们的地址、数据、头
request = urllib.request.Request(url, data, headers)

#访问
html = urllib.request.urlopen(request).read().decode('utf-8')

#利用json解析包解析返回的json数据 拿到翻译结果
print(json.loads(html))
