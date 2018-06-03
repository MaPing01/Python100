#!usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Ma Ping

import requests
import json

url  = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_551816010?csrf_token='
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Referer':'http://music.163/song?id=551816010',
    'Origin':'http://music.163.com',
    'Host':'music.163.com'
}
user_data = {
    'params': 'Cf42uWrjARs/LnoNtwCCTaOVE85gk3O8qpQTgQ1sQOiWWgTsQz8oFXBmt7ngUNHVk1jqzkwjfNl5iuzv/qJg4Nw0X1EkhYTcDbwuSblhwNpJQaUt614PtdBEqyYRAUrRykIXkN0lSnjrmvIdJwTsz+XhT5WlcJg8c6BqOoiKhBe8dHQEMqLwE9XlrH8W4tAs',
    'encSecKey':'5cf7fa957c27b16455a5d55fdb5a74e8467f9c27b9ebc99b17997bfb305151db1ce9cc53751207ad574defbb8e425db490a7c4ecd1adc6b8577293082dc2d28fde5dceb8ba626059af42133466b4de37836c71b9882d8f51e6ca11e9eb68e37c84e2ee0a146eaff356ff625fc72d9cb37bf1cc2c5951adc837073d233ab3ffc0'
}
response = requests.post(url,headers=headers,data=user_data)
data = json.loads(response.text)
hotcomments = []
for hotcommen in data['hotComments']:
    item = {
        'nickname':hotcommen['user']['nickname'],
        'content':hotcommen['content'],
        'likedCount':hotcommen['likedCount']
    }
    hotcomments.append(item)
content_list = [content['content'] for content in hotcomments]
nickname = [content['nickname'] for content in hotcomments]
liked_count = [content['likedCount'] for content in hotcomments]
print(content_list)
print(nickname)
print(liked_count)
for content in content_list:
    print()
    print(content)
for name in nickname:
    print()
    print(name)
