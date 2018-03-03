import requests
from lxml import etree
import re
import json


def get_html_text(url):
    headers = {
        'Referer': 'Referer:http://www.dytt8.net/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
    r = requests.get(url, headers = headers)
    r.encoding = 'gbk'
    return r.text

url_tlpt = 'http://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'
html_text = get_html_text(url_tlpt.format(1))
page_info = re.findall(r'共\d+页', html_text)[0]
page_total = int(page_info[1:-1])
for page in range(1, page_total + 1):
    url = url_tlpt.format(page)
    html_text = get_html_text(url)
    a_tags = etree.HTML(html_text).xpath('//a[@class="ulink"]')
    result = []
    for tag in a_tags:
        url_list = tag.xpath('./@href')
        name_list =  tag.xpath('./text()')
        if len(url_list) == 0  or len(name_list) == 0:
            print('---->' + str(page), url_list, name_list)
            continue
        url = url_list[0]
        name = name_list[0]
        movie = {
            'url': url,
            'name': name
        }
        result.append(movie)
        with open('dy2018.json', 'a') as f:
            f.write(json.dumps(result, ensure_ascii = False, indent = 1))
            f.close()


