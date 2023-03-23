# -*- encoding: utf-8 -*-
"""
@Author : hebe_tian
"""
import requests
import json
import jsonpath
import logging
import time


class WeiboApi:
    def __init__(self):
        self.url = 'https://weibo.com'

    def weibo_hot_band(self):
        path = '/ajax/statuses/hot_band'
        hot_band_response = requests.get(self.url + path)
        hot_band_response = json.loads(hot_band_response.text)
        band_list = {}
        try:
            # gov hot band->name and gov_tag
            gov_note = jsonpath.jsonpath(hot_band_response, '$.data.hotgov.note')
            # gov_num = jsonpath.jsonpath(hot_band_response, '$.data.hotgov.num')
            band_list[gov_note[0]] = 'gov'
            # social hot band->name and hot_num
            note_list = jsonpath.jsonpath(hot_band_response, '$.data.band_list[*].note')
            num_list = jsonpath.jsonpath(hot_band_response, '$.data.band_list[*].num')
            for i in range(len(note_list)):
                band_list[note_list[i]] = num_list[i]
            return band_list

        except Exception as e:
            return logging.exception(e)

    def weibo_topic_num(self):
        path = '/ajax/statuses/topic_band'
        params = {
            'sid': 'v_weibopro',
            'category': 'all'
        }
        topic_response = requests.get(self.url + path, params=params)
        topic_response = json.loads(topic_response.text)
        try:
            topic_num = jsonpath.jsonpath(topic_response, '$.data.total_data_num')[0]
            return topic_num
        except Exception as e:
            return logging.exception(e)

    def weibo_topic_band(self, max_page):
        path = '/ajax/statuses/topic_band'
        params = {
            'sid': 'v_weibopro',
            'category': 'all'
        }
        hot_topic = {}
        for page in range(1, max_page):
            params['page'] = page

            try:
                topic_response = requests.get(self.url + path, params=params)
                topic_response = json.loads(topic_response.text)
                topic_list = jsonpath.jsonpath(topic_response, '$.data.statuses[*].topic')
                summary_list = jsonpath.jsonpath(topic_response, '$.data.statuses[*].summary')

                for i in range(len(topic_list)):
                    if summary_list[i] == '':
                        summary_list[i] = False
                    hot_topic[topic_list[i]] = summary_list[i]

                page += 1

            except Exception as e:
                return logging.exception(e)

            time.sleep(2)

        return hot_topic
