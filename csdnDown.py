# -*- coding: utf-8 -*-
"""
Created on Tue Jun 10 23:01:11 2014

@author: x
"""

import cookielib
import urllib2
import urllib
from BeautifulSoup import BeautifulSoup
from threading import Thread
import os

class HeadRequest(urllib2.Request):
    def get_method(self):
        return 'HEAD'
        
class GetSourceThread(Thread):
    def __init__(self,url,path):
        Thread.__init__(self)
        self.url = url
        self.path = path
        
    def run(self):
        response = urllib2.urlopen(HeadRequest(self.url))
        print response.info().getheader('Content-Disposition')
        name = response.info().getheader('Content-Disposition').split('filename=')[1].strip('"').strip()
        filename = os.path.join(self.path,urllib.unquote(name))
        print filename
        urllib.urlretrieve(self.url,filename)

def zh2unicode(text):
    """
    Auto converter encodings to unicode
    It will test utf8, gbk, big5, jp, kr to converter"""
    for encoding in ('utf-8', 'gbk', 'big5', 'jp', 'euc_kr','utf16','utf32'):
        try:
            return text.decode(encoding)
        except:
            pass
    return text

path = os.getcwd()
user = '***********'
pwd = '******'
initUrl = "http://www.juming.com/Csdn/"
loginUrl = 'http://www.juming.com/Csdn/index.htm'
codeUrl = 'http://www.juming.com/Csdn/code.htm'
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')]
urllib2.install_opener(opener)
resp = urllib2.urlopen(initUrl).read()

user = 'shawpan@yeah.net'
pwd = 'xiaopan'
#sourceUrl = 'http://download.csdn.net/download/geo_zhao/1630368'
sourceUrl = 'http://download.csdn.net/download/geo_zhao/1630368'
#sourceUrl = raw_input('Please enter the source Url: ')
urllib.urlretrieve(codeUrl,os.path.join(path,'verify_code.jpg'))
yzm = raw_input('Please enter the verify code: ')
data = urllib.urlencode({'ziyuandz':sourceUrl,'csdn_zh':user,'csdn_mm':pwd,'re_yzm':yzm})
res = opener.open(loginUrl,data).read()
print zh2unicode(res)
hrefs = BeautifulSoup(res)('a')
for a in hrefs:
    href = a.get('href')
    print href
crackUrl = initUrl + href
if BeautifulSoup(res)('strong'):
    
    links = BeautifulSoup(res)('strong')[0]
    linkUrl = ''.join(''.join(links).split(';'))
    #print linkUrl
    desp = linkUrl.split('?')
    downloadUrl = 'http://dldx.csdn.net/fd.php?'+desp[1]
    print downloadUrl
    t2 = GetSourceThread(downloadUrl,path)
    t2.start()
    t2.join()
    print 'finished!'
else:
    resourceName = zh2unicode(res).split('<br>')[1]
    print resourceName
    



