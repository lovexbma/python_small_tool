# -*- coding:utf-8 -*-
import re
import urllib
import urllib2

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent':user_agent}
try:
    request = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(request)
    #print response.read()
    content = response.read().decode('utf-8')
    pattern = re.compile('<div class="author clearfix">.*?title=.*?<h2>(.*?)</h2>.*?' +
                         '<div class="content">.*?<span>(.*?)</span>.*?</div>.*?' +
                         '<div class="stats">.*?' +
                         'class="number">(.*?)</i>', re.S)
    items = re.findall(pattern,content)

    for item in items:
        haveImg = re.search("img",item [2] )
        if not haveImg:
            print item[0],'\n',item[1], '\n', item[2], '\n'

    #'<div class="thumb">.*?src="(.+?[\.jpg|\.png|\.gif])".*?'+
    #reg = r'src="(.+?[\.jpg|\.png|\.gif])"'
    reg = r'<div class="thumb">.*?src="(.+?[\.jpg|\.png|\.gif])".*?</div>'
    imgre = re.compile(reg, re.S)
    imglist = re.findall(imgre, content)
    x = 0
    for imgurl in imglist:
        print imgurl
        urllib.urlretrieve(imgurl, '%s.png' % x)
        x += 1
except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason
