import requests
from lxml import etree
from bs4 import BeautifulSoup


def get_html_text(page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
    params = {
        'p': page
    }
    url = 'http://blog.nogizaka46.com/manatsu.akimoto/'
    r = requests.get(url, headers = headers, params = params, timeout = 30)
    with open('akimoto.manatsu.html', 'w', encoding = 'utf-8') as f:
        f.write(r.text)
        f.close()
    
def main():
    with open('akimoto.manatsu.html', 'rb') as f:
        html_text = f.read()
        f.close()
    doc = etree.HTML(html_text)
    options = doc.xpath('//select/option')[1:]
    for op in options:
        print(op.xpath('./@value'), op.xpath('./text()'))
    
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
  
    
    
    
    



# doc = etree.HTML(r.text) 报错
# ValueError: Unicode strings with encoding declaration are not supported.
# 
# https://www.v2ex.com/t/62863
#
# 因为得到的HTML内容有有一句：<?xml version="1.0" encoding="UTF-8"?>
# 因为是字符串是unicode类型了（转码后的了）, # lxml找到encoding的相关申明还会尝试转到unicode一次，自然会失败，给这些解析器的都该是raw string. 
# 所以请使用 r.content
