import requests
import re
from bs4 import BeautifulSoup
import traceback
from lxml import etree


def get_html_text(url):
    try:
        r = requests.get(url, timeout = 30, headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'})
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''

def read_file():
    with open('eastmoney.html') as f:
        html_text = f.read()
        f.close()
    return html_text

def get_stock_code_list():
    result = []
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    html_text = get_html_text(stock_list_url)
    stock_url_list = re.findall(r'http://quote.eastmoney.com/s[hz]\d{6}\.html', html_text)
    stock_code_pattern = re.compile(r's[hz]\d{6}')
    for stock_url in stock_url_list:
        stock_code = stock_code_pattern.findall(stock_url)[0]
        result.append(stock_code)
    return result

def get_stock_info(stock_code_list):
    stock_info_url_template = 'https://gupiao.baidu.com/stock/{}.html'
    for stock_code in stock_code_list:
        url = stock_info_url_template.format(stock_code)
        html_text = get_html_text(url)
        if html_text == '':
            print('url={} is empty'.format(url))
            continue
        soup = BeautifulSoup(html_text, 'html.parser')
        stock_info = soup.find('div', {'class':'stock-bets'})
        name = stock_info.find('a', {'class': 'bets-name'}).text.split()[0]
        with open('stock.txt', 'a') as f:
            f.write(stock_code + ',' + name)
            f.close()

def main():
    stock_code_list = get_stock_code_list()
    getStockInfo(stock_code_list)

if __name__ == '__main__':
    stock_code_list = get_stock_code_list()
    get_stock_info(stock_code_list)
