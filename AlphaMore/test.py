import mxnet as mx

a = mx.nd.ones((2, 3))

b = a * 2 + 1
print(b.asnumpy())

import urllib3
import json

urllib3.disable_warnings()

http = urllib3.PoolManager()

send_headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Connection':'keep-alive',
    'Host':'xueqiu.com',
    'Cookie':'',
}
r = http.request('GET', 'https://xueqiu.com', headers = send_headers)
print("----------  end  -------------")
print(r.status)
print(r.data)

r = http.request('GET', 'https://xueqiu.com/stock/cata/stocklist.json?page=1&size=1&order=desc&orderby=percent&type=11', headers = send_headers)

print(json.loads(r.data.decode('utf-8')))

print("----------  end  -------------")
