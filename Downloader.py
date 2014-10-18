# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 12:27:41 2014

@author: x
"""

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import DownloaderUI
import cookielib
import urllib2
import urllib
from BeautifulSoup import BeautifulSoup
from threading import Thread
import os
import time

class HeadRequest(urllib2.Request):
    def get_method(self):
        return 'HEAD'
        
class GetSourceThread(Thread):
    def __init__(self,url,filename):
        Thread.__init__(self)
        self.url = url
        self.filename = filename
        
    def run(self):        
        urllib.urlretrieve(self.url,self.filename)
        
class DownloaderDlg(QDialog,DownloaderUI.Ui_DownloaderUI):
    def __init__(self,parent = None):
        super(DownloaderDlg,self).__init__(parent)
        self.setupUi(self)
        self.user = 'shawpan@yeah.net'
        self.pwd = 'xiaopan'
        self.initUrl = "http://www.juming.com/Csdn/"
        self.loginUrl = 'http://www.juming.com/Csdn/index.htm'
        self.codeUrl = 'http://www.juming.com/Csdn/code.htm'
        self.path = os.getcwd()
        self.output = ""
        #self.on_B_changePhoto_clicked()
        #self.updateUi()
    @pyqtSignature("")
    def on_B_changePhoto_clicked(self):
        codepath = os.path.join(self.path,'verify_code.jpg')
        urllib.urlretrieve(self.codeUrl,codepath)
        self.L_photo.setPixmap(QPixmap(codepath))
        
        
        
    
    @pyqtSignature("")
    def on_B_getResource_clicked(self):
        self.output = ""
        #self.E_status.setText()
        sourceUrl = unicode(self.E_resourceURL.text())
        #self.E_status.setText(resourceURL)
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        opener.addheaders = [('User-agent','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')]
        urllib2.install_opener(opener)
        resp = urllib2.urlopen(self.initUrl).read()
        yzm = unicode(self.E_verifyCode.text())
        data = urllib.urlencode({'ziyuandz':sourceUrl,'csdn_zh':self.user,'csdn_mm':self.pwd,'re_yzm':yzm})
        res = opener.open(self.loginUrl,data).read()
        #print zh2unicode(res)
        links = BeautifulSoup(res)('strong')[0]
        linkUrl = ''.join(''.join(links).split(';'))
        #print linkUrl
        desp = linkUrl.split('?')
        downloadUrl = 'http://dldx.csdn.net/fd.php?'+desp[1]
        
        response = urllib2.urlopen(HeadRequest(downloadUrl))
        #print response.info().getheader('Content-Disposition')
        name = response.info().getheader('Content-Disposition').split('filename=')[1].strip('"').strip()
        #filename = os.path.join(self.path,urllib.unquote(name))
        filename = QFileDialog.getSaveFileName(self,"save",self.zh2unicode(urllib.unquote(name)))
        self.output = "Start downloading file to " + filename + "\n"
        self.E_status.setText(self.output)
        t2 = GetSourceThread(downloadUrl,filename)
        t2.start()
        while (t2.isAlive()):
            self.output = self.output + "Downloading...\n"
            self.E_status.setText(self.output)
            time.sleep(1)
        self.output = self.output + "Finish...\n"
        self.E_status.setText(self.output)
        #t2.join()
        
    def zh2unicode(self,text):
        for encoding in ('utf-8', 'gbk', 'big5', 'jp', 'euc_kr','utf16','utf32'):
            try:
                return text.decode(encoding)
            except:
                pass
        return text
        
    
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = DownloaderDlg()
    myapp.show()
    sys.exit(app.exec_())