import requests
import re

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''
        
def parseHTML(goods_list, html):
    try:        
        name_strs = re.findall(r'\"raw_title\":\".*?\"', html)
        price_strs = re.findall(r'\"view_price\":\"[\d\.]*\"', html)
        for i in range(len(name_strs)):        
            name = eval(name_strs[i].split(':')[1])
            price = eval(price_strs[i].split(':')[1])
            goods_list.append([name, price])
    except:
        pass
    
def print_goods_list(goods_list):
    template = '{:4}\t{:8}\t{:16}'
    print(template.format('序号', '价格', '商品名称'))
    count = 0
    for good in goods_list:
        count += 1
        good_name = good[0]
        good_price = good[1]
        print(template.format(count, good_name, good_price))
    
def main():
    url_template = 'https://s.taobao.com/search?q={}&s={}'
    good_name = '书包'
    goods_list = []
    page_count = 3
    for page in range(page_count):        
        url = url_template.format(good_name, page)
        try:
            html = getHTMLText(url)
            parseHTML(goods_list, html)
        except:
            pass
    print_goods_list(goods_list)
    
if __name__ == '__main__':
    main()
