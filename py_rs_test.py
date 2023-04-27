import subprocess
from functools import partial
 
subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")

import re
import execjs
import requests

url = "http://mpa.hubei.gov.cn/zfxxgk/fdzdgknr/cpzh/"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Host": "mpa.hubei.gov.cn",
    "Pragma": "no-cache",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62"
}



resp1 = requests.get(url, headers=headers)
content = re.findall(r"content=\"(.*?)\"", resp1.text)[1]
cookie1 = resp1.headers["Set-Cookie"].split(";")[0]
nsd = int(re.findall(r"nsd=(.*?);", resp1.text)[0])
cd = re.findall(r"cd=\"(.*?)\"", resp1.text)[0]
# print(content, nsd, cd)

with open("./a_6.js", "r", encoding="utf-8") as f:
    jsdata = f.read()
ctx = execjs.compile(jsdata)
ret = ctx.call("main", content, nsd, cd, cookie1).split(";")[0]
# print(ret)
cookie_enable = "enable_ZkLlO5PNXDiy=true"
req_cookie = ";".join([cookie_enable, cookie1, ret])
# print(req_cookie)
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Cookie": req_cookie,
    "Host": "mpa.hubei.gov.cn",
    "Pragma": "no-cache",
    "Referer": "http://mpa.hubei.gov.cn/zfxxgk/fdzdgknr/cpzh/index.shtml",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62"
}

resp2 = requests.get(url, headers=headers)

print(resp2)
print(resp2.headers)
print(resp2.text)
