#!/usr/bin/env
#coding=utf-8


import requests
import time
import random
import string
import hashlib
import config.config
from urllib import urlencode


PARAMS = {'app_id': config.config.APP_ID,
         'text': '今天天气不错呀',
         'time_stamp': str(int(time.time())),
         'nonce_str': ''.join(random.sample(string.ascii_lowercase + string.digits, 10)),
         'sign': ''}


def getReqSgin(params):
    '''
    计算鉴权签名
    '''
    sort_dict = sorted(params.items(), key=lambda item:item[0])  # 对key按字母升序排列
    sort_dict.remove(('sign', ''))  # 暂时删除空值键sign
    sort_dict.append(config.config.APP_KEY)  # 添加app_key
    req_parms = urlencode(sort_dict).encode()  # 把列表转化为url请求参数key=value参数形式
    # print req_parms
    # 把请求参数字符串求md5,并转为大写
    sha = hashlib.md5()
    sha.update(req_parms)
    md5text = sha.hexdigest().upper()
    sign = md5text  # 最终获得签名
    return sign

def analysis(url, params):
    '''
    分析情感语义
    '''
    r = requests.post(url, params)
    return r



if __name__ == '__main__':
    req_url = 'https://api.ai.qq.com/fcgi-bin/nlp/nlp_textpolar'
    req_text = '编程了一晚，终于完成，哈哈哈'

    PARAMS['text'] = req_text
    PARAMS['sign'] = getReqSgin(PARAMS)
    response = analysis(req_url, PARAMS)
    # print response
    print response.text