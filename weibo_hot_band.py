# -*- encoding: utf-8 -*-
"""
@Author : hebe_tian
"""
import requests
import json
import jsonpath
import logging


class WeiboApi:
    def __init__(self):
        self.url = 'https://weibo.com'

    def weibo_hot_band(self):
        path = '/ajax/statuses/hot_band'
        hot_band_response = requests.get(self.url + path)
        hot_band_response = json.loads(hot_band_response.text)
        band_list = {}
        try:
            note_list = jsonpath.jsonpath(hot_band_response, '$.data.band_list[*].note')
            num_list = jsonpath.jsonpath(hot_band_response, '$.data.band_list[*].num')
            for i in range(len(note_list)):
                band_list[note_list[i]] = num_list[i]
            return band_list

        except Exception as e:
            return logging.exception(e)

        
test = WeiboApi()
print(test.weibo_hot_band())
