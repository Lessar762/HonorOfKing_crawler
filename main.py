import urllib.request
import re
import numpy as np
import os

class get_html(object):
    heroname=[]
    strlist=[]
    def __init__(self,URL,HEAD):
        self.url=URL
        self.head_request=HEAD
        
    def get_flie(self):
        self.request =urllib.request.Request(self.url)
        self.request.add_header("user-agent",self.head_request)
        self.response=urllib.request.urlopen(self.request)
        return self.response.read()#返回字节型字符串
    
    def get_list(self):
        HTML=self.get_flie()
        self.list=re.findall(b"game.gtimg.cn.{29,35}/(\d{3}).jpg",HTML)
        self.name=re.findall(b"game.gtimg.cn.{34,40}jpg.*\n.*>(.*?)</a></li>",HTML)
        
        for i in self.name:
            self.heroname.append(str(i,encoding="gbk"))
        for i in self.list:
            self.strlist.append(str(i,encoding="utf8"))

    
    def get_img(self):
        self.get_list()
        List=self.strlist
        number=0
        os.mkdir("download_pic/")
        for i in List:
            os.mkdir("download_pic/"+self.heroname[number]+"/")
            for num in range(15):#真的会有英雄有14个皮肤吗
                num+=1
                try:
                    self.url="https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/"+i+"/"+i+"-bigskin-"+str(num)+".jpg"
                    img=self.get_flie()
                    with open("download_pic/"+self.heroname[number]+"/"+self.heroname[number]+str(num)+".jpg","wb") as f:
                        f.write(img)
                except urllib.error.HTTPError:
                    number+=1 
                    break
            
    
  
                
        
#downloadurl=https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/508/508-bigskin-1.jpg|先代码审计找到一条例子
head_google="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"    
URLL="https://pvp.qq.com/web201605/herolist.shtml"
html=get_html(URLL,head_google)
html.get_img()
