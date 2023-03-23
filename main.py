import logging

import weibo_hot_band


hot_band_content = weibo_hot_band.WeiboApi()
hot_band = hot_band_content.weibo_hot_band()
print(len(hot_band))
print(hot_band)

max_page = hot_band_content.weibo_topic_num()
if type(max_page) == int:
    max_page = max_page//10
    topic = hot_band_content.weibo_topic_band(max_page)
    print(len(topic))
    print(topic)
else:
    print('max_page error')
