#coding=utf-8
import re
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?[\.jpg|\.png|\.gif])"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl, '%s.png' % x)
        x += 1
    return imglist

html = getHtml("https://www.taobao.com/markets/nvzhuang/taobaonvzhuang")#http://www.xxsy.net/

print getImg(html)
