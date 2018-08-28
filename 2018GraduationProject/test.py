## Author:Xu
## 豆瓣top250，保存记录到movInfo.txt

#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
import requests
from bs4 import BeautifulSoup
import re
import traceback
import sys

def GetHtmlText(url):
    for i in range(0,1):        #尝试两次
        try:
            r=requests.get(url)
            r.encoding = 'utf-8'
            r.raise_for_status();
            return r.text;
        except:
            traceback.print_exc()
            continue
    return 

def GetMovieInfo(url):
    movieDict={}
    for page in range(0,1):
        try:
            page_url = '?start='+str(page*25)
            html = GetHtmlText(url+page_url)
            Soup = BeautifulSoup(html, 'html.parser')
            movie = Soup.find(name="ol",class_='grid_view') #所有电影信息
            # print(movie)
            movieList = movie.find_all(name='li')  #电影信息列表
            # print(movieList)
            for single in movieList:        #循环单页的电影信息
                num = single.find(name='em').string    #电影排名
                # print(num)
                title1 = single.find_all(name='span',class_='title')
                # print(title1)
                title2 = single.find(name='span',class_='other').string
                if len(title1)==2:
                    movieTitle = title1[0].string+title1[1].string+title2.string
                else:
                    movieTitle = title1[0].string+title2.string

                Quote = single.find_all(name='span',class_='inq')
                # print(Quote)
                movieQuote = Quote[0].string
                # print(movieQuote)
                # sys.exit(0)
                classBD = single.find(name='div',class_='bd').contents    #我也不知道为什么bs给我返回7个节点
                # print(classBD)
                movieActor = classBD[1].text
                # print(movieActor)
                movieRating = re.findall(r'\d?\.\d?',str(classBD[3]))[0]
                # print(movieRating)
                movieDict['num'] = num
                movieDict['movieTitle'] = movieTitle
                movieDict['actor'] = movieActor
                movieDict['rating'] = movieRating
                movieDict['quote'] = movieQuote
                print(num+movieTitle+movieActor+movieRating+movieQuote + '\n')
                printMovieInfo(movieDict)
        except:
            traceback.print_exc()


def printMovieInfo(Info):
    try:
        with open('D:/pyworkspace/2018GraduationProject/movieInfo.txt','a',encoding='utf-8') as f:
            f.write(str(Info['num']+Info['movieTitle']+'\n'+Info['actor']+'\n评分:'+Info['rating']+'\n评价：'+Info['quote']+'\n'))
    except:
        traceback.print_exc()


if __name__ == "__main__":
    base_url = 'https://movie.douban.com/top250'
    GetMovieInfo(base_url)
    
