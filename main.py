import weibo_hot_band


hot_band_content = weibo_hot_band.WeiboApi()
print(hot_band_content.weibo_hot_band())
print('\n')
print(hot_band_content.weibo_topic_band())