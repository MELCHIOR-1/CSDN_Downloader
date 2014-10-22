CSDN Downloader
===========================
使用python和pyQt将网上流行的[鬼哥CSDN免积分在线下载](http://www.juming.com/Csdn/ "http://www.juming.com/Csdn/")页面封装到了一个QT程序中。还有些bug有待修复。

*******
###             Author: shawpan
###             Email:  shawpan@yeah.net
*********
#依赖
1. python2.7  
2. BeautifulSoup库，已在仓库中  
3. pyQT4的库函数  
4. urllib、urllib2库  

*********
#使用说明：
直接双击Downloader.pyw，若能弹出程序界面，则说明不缺少库.初始界面如下：  
![](https://github.com/MELCHIOR-1/CSDN_Downloader/blob/master/pic/init.png)  
输入你在CSDN的资源下载页的地址，如：http://download.csdn.net/detail/leixiaohua1020/8054395  
点击换一张，获取验证码  
如下图：  
![](https://github.com/MELCHIOR-1/CSDN_Downloader/blob/master/pic/step3.png)
  
输入验证码，然后点击获取资源按钮。  
等程序获取到资源地址后，会弹出保存文件的对话框，如下图：  
![](https://github.com/MELCHIOR-1/CSDN_Downloader/blob/master/pic/step4.png)  
  
选择保存位置，点击OK  
等待程序下载完毕，如下图：  

![](https://github.com/MELCHIOR-1/CSDN_Downloader/blob/master/pic/step5.png)

***********
#BUG
有时候下载会出现需要到一个[网址](http://www.juming.com/Csdn/csdnyzm.htm)上重新输入验证码的情况，还在调试中。。
