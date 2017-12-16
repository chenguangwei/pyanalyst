import time
import random
import requests
from lxml import etree
from lxml import html
absolute = 'https://movie.douban.com/subject/26322642/comments'
page1_url = 'https://movie.douban.com/subject/26322642/comments?start=0&limit=20&sort=new_score&status=P&percent_type='
absolute_url = 'https://movie.douban.com/subject/26322642/comments?start=20&limit=20&sort=new_score&status=P&percent_type='
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0','Connection':'keep-alive'}
f_cookies = open('cookies.txt', 'r')
cookies = {}
for line in f_cookies.read().split(';'):
    name, value = line.strip().split('=', 1)
    cookies[name] = value
next_page_list = []

def next_page(url):
    r = requests.get(url=url,cookies=cookies,headers=header).content
    soup = etree.HTML(r)
    return soup.xpath('//*[@id="paginator"]/a[3]/@href')
def html_prase(url):
    r = requests.get(url=url,cookies=cookies,headers=header).content
    return etree.HTML(r)
next_page_url = next_page(absolute_url)
print(page1_url)
page1 = html_prase(page1_url)
print("正在打印第1页面")
for i in range(1, 21):
    comment = ''.join(page1.xpath('//*[@id="comments"]/div[%s]/div[2]/p/text()' %i)).strip().replace('\n',',')
    date = page1.xpath('//*[@id="comments"]/div[%s]/div[2]/h3/span[2]/span[3]/text()' %i)
    if date:
        date = ''.join(page1.xpath('//*[@id="comments"]/div[%s]/div[2]/h3/span[2]/span[3]/text()' %i)).strip()
    else:
        date = ''.join(page1.xpath('//*[@id="comments"]/div[%s]/div[2]/h3/span[2]/span[2]/text()' %i)).strip()
    rate = page1.xpath('//*[@id="comments"]/div[%s]/div[2]/h3/span[2]/span[2]/@title' %i)
    for i in rate:
        if u'\u4e00' <= i <= u'\u9fff':
            rate = i.strip()
        else:
            rate = '还行'
    with open('date_rate_comment.txt', 'a', encoding='utf-8')as f:
        f.write(date + ',' + rate + ',' + comment + '\n')
    #处理第二页以后页面
    page = 2
    while (next_page_url !=[]):
        print('正在打印第%s页' %page)
        print(absolute + ''.join(next_page_url))
        html = html_prase(absolute + ''.join(next_page_url))
        next_page_url = next_page(absolute + ''.join(next_page_url))
        page = 2
        while (next_page_url != []):
            print('正在打印第%s页' % page)
            print(absolute + ''.join(next_page_url))
            html = html_prase(absolute + ''.join(next_page_url))
            next_page_url = next_page(absolute + ''.join(next_page_url))
            for i in range(1, 21):
                comment = ''.join(html.xpath('//*[@id="comments"]/div[%s]/div[2]/p/text()' %i)).strip().replace('\n',',')
                date = html.xpath('//*[@id="comments"]/div[%s]/div[2]/h3/span[2]/span[3]/text()' %i)
                if date:
                    date = ''.join(html.xpath('//*[@id="comments"]/div[%s]/div[2]/h3/span[2]/span[3]/text()' %i)).strip()
                else:
                    date = ''.join(html.xpath('//*[@id="comments"]/div[%s]/div[2]/h3/span[2]/span[2]/text()' %i)).strip()
                rate = html.xpath('//*[@id="comments"]/div[%s]/div[2]/h3/span[2]/span[2]/@title' %i)
                for i in rate:
                    if u'\u4e00' <= i <= u'\u9fff':
                        rate = i.strip()
                    else:
                        rate = '还行'
                with open('date_rate_comment.txt', 'a', encoding='utf-8')as f:
                    f.write(date + ',' + rate + ',' + comment + '\n')
            time.sleep(1 + float(random.randint(1, 100)) / 20)
            page = page + 1