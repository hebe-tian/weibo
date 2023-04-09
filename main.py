import weibo_hot_band
import local_file


hot_band = weibo_hot_band.weibo_hot_band()
try:
    last_content = local_file.read_content('weibo.json')
    diff = local_file.file_diff(hot_band, last_content)
    print(diff)
except FileNotFoundError as e:
    print(e)

local_file.save_content(hot_band)
print(hot_band)

topic = weibo_hot_band.weibo_topic_band()
print(topic)

