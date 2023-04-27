import weibo_hot_band
import datetime
import pytz


dt = datetime.datetime.now()
print(dt.astimezone(tz=pytz.timezone('Asia/Shanghai')))

hot_band = weibo_hot_band.weibo_hot_band()
print(hot_band)

topic = weibo_hot_band.weibo_topic_band()
print(topic)

