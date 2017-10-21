import re
import requests


res = requests.get(r"http://news.ncu.edu.cn/")
res.encoding = "utf-8"
news_titles1 = re.findall(r'<li.*?><a.*?>(.*)<\/a><span.*?>.*?<\/span><\/li>',str(res.text))
for news_title in news_titles1:
    if not "img" in news_title:
        with open('新闻标题.txt','a+',encoding = "utf-8") as f:
            news_title = news_title + '\n'
            f.write(news_title)                   
                            
