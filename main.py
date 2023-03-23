import logging

import weibo_hot_band


hot_band_content = weibo_hot_band.WeiboApi()
hot_band = hot_band_content.weibo_hot_band()
print(len(hot_band))
print(hot_band)

topic = hot_band_content.weibo_topic_band()
print(len(topic))
print(topic)

