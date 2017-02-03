#encoding=utf-8
import re
import urllib
import urllib2

url = 'https://www.taobao.com/markets/nvzhuang/taobaonvzhuang'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
headers = {'User-Agent':user_agent}
try:
    request = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(request)
    content = response.read()

    #print content
    reg = r'<a href="(.+?)"><img src="\/\/(.+?[\.png|\.jpg|\.gif])"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, content)
    x = 0
    for imgurl in imglist:
        imgadd = 'http:' + imgurl[0] + imgurl[1]
        print imgadd
        urllib.urlretrieve(imgadd, '%s.png' % x)
        x += 1
except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason
