# encoding: utf-8

import requests
import json
import os


def sign(tieba_name):
    url = 'http://tieba.baidu.com/sign/add'
    params = {
        'ie': 'utf-8',
        'kw': tieba_name
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
    cookies = {
        'BDUSS': '不给看'
    }
    r = requests.post(url, params = params, headers = headers, cookies = cookies)
    r_json = json.loads(r.text)
    code = r_json['no']
    error = r_json['error']
    data = r_json['data']
    if code == 0:
        print(tieba_name + '签到成功')
    elif code == 1010:
        print('贴吧不存在')
    else:
        print(code, error)
    
if __name__ == '__main__':
    file_name = 'tieba.txt'
    if os.path.join(os.getcwd(), file_name):        
        tieba_names = []    
        with open('tieba.txt', encoding = 'utf-8') as f:
            for name in f.readlines():
                tieba_names.append(name.strip())
        for name in tieba_names:
            sign(name)
    else:
        print('请添加一个' + file_name + '文件放在当前目录下')
        
