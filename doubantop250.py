# coding:utf-8 
import requests 
from lxml import html 
import sys 
# reload(sys) 
# sys.setdefaultencoding( "utf-8" ) 

k = 1 
for i in range(10): 
    url = 'https://movie.douban.com/top250?start={}&filter='.format(i*25) 
    con = requests.get(url).content 
    sel = html.fromstring(con) 

    # 所有的信息都在class属性为info的div标签里，可以先把这个节点取出来 
    for i in sel.xpath('//div[@class="info"]'): 

        # 影片名称 
        title = i.xpath('div[@class="hd"]/a/span[@class="title"]/text()')[0] 
    
        info = i.xpath('div[@class="bd"]/p[1]/text()') 
        # 导演演员信息 
        info_1 = info[0].replace(" ", "").replace("\n", "") 
        # 上映日期 
        date = info[1].replace(" ", "").replace("\n", "").split("/")[0] 
        # 制片国家 
        country = info[1].replace(" ", "").replace("\n", "").split("/")[1] 
        # 影片类型 
        geners = info[1].replace(" ", "").replace("\n", "").split("/")[2] 
        # 评分 
        rate = i.xpath('//span[@class="rating_num"]/text()')[0] 
        # 评论人数 
        comCount = i.xpath('//div[@class="star"]/span[4]/text()')[0] 

        # 打印结果看看 
        print("TOP%s" % str(k))
        print(title, info_1, rate, date, country, geners, comCount)

        # 写入文件 
        with open("top250.txt", "a") as f: 
            f.write("TOP%s\n影片名称：%s\n评分：%s %s\n上映日期：%s\n上映国家：%s\n%s\n" % (k, title, rate, comCount, date, country, info_1)) 

            f.write("==========================\n") 
    
        k += 1
