#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
from bs4 import BeautifulSoup
import traceback
import requests


def agent():
    # 构造http 请求头
    headers = {
        'HOST': 'movie.douban.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:45.0) Gecko/20100101 Firefox/45.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'DNT': '1',
        'Referer': 'https://movie.douban.com/',
        'Connection': 'keep-alive',
    }
    return headers


def get_html(url):
    for i in range(0,1):
        try:
            r = requests.get(url)
            r.encoding = 'utf-8'
            r.raise_for_status();
            return r.text
        except:
            traceback.print_exc()
            continue
    return 


def filter_html(url):
    # 解析html 页面
    html = get_html(url)
    # BS不能直接处理url,因此从urllib2那里获取到页面源码，再由BS解析
    s = BeautifulSoup(html,'lxml')
    movie_dict = {}
    # 获取到页面的div id=screening这个属性的div里面就有当前热门电影,因此我们就获取这整个div
    for i in s.find_all('div', id="screening"):
        # ul标签就是html列表,这个div里面的ul就是电影列表
        li = i.find_all('ul')
        # print i.attrs
        for j in li:
            # print(j)
            # exit()
            # text是获取列表里面的字符
            content = j.text
            # print(content)
            exit()
            # 获取到的字符里面包含大量的空格因此需要处理
            name = content.strip().replace(' ', '').split()[0]
            score = content.strip().replace(' ', '').split()[1]
            # 将其加入字典电影名称作为键,分数作为值,这样做还有一个原因是获取的结果有重复的话,存到字典里面可以去重
            movie_dict[name] = score
            # print '%s  评分:%s' % (name, score)
    for k, v in movie_dict.items():
        print(k, v)

if __name__ == "__main__":
    link = 'https://movie.douban.com/'
    filter_html(link)
