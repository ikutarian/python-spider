# coding: utf-8

import requests
from lxml import etree
import re
import json


def get_html_text(page):
    try:
        hearders = {       
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        }
        base_url = 'https://movie.douban.com/top250'
        params = {'start': page * 25}
        r = requests.get(base_url, headers = hearders, params = params)
        return r.text
    except Exception as e:
        print(str(e))

def main():
    ranking = 0
    top250 = []
    for page in range(10):
        doc = etree.HTML(get_html_text(page))
        lis = doc.xpath('//ol[@class="grid_view"]/li')
        for li in lis:
            ranking += 1
            pic = li.xpath('.//div[@class="pic"]/a/img/@src')[0]
            url = li.xpath('.//div[@class="hd"]/a/@href')[0]
            title = li.xpath('.//div[@class="hd"]/a/span[1]/text()')[0]            
            star = li.xpath('.//div[@class="star"]/span[@class="rating_num"]/text()')[0]            
            quote = li.xpath('.//p[@class="quote"]/span/text()')[0]
            movie_info = {
                'ranking': ranking,
                'pic': pic,
                'url': url,
                'title': title,                
                'star': star,
                'quote': quote
            }
            top250.append(movie_info)
    str = json.dumps(top250, ensure_ascii = False, indent = 1).replace('\xa0', '')
    with open('douban250.txt', 'w', encoding = 'utf-8') as f:
        f.write(str)
        f.close()
    
      
if __name__ == '__main__':
    main()
