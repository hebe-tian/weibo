# weibo  

## weibo_hot_band  
* weibo_hot_band方法，获取微博热搜榜单和热度，以字典的形式返回  
* weibo_topic_band方法，获取微博热门话题榜单和简述，以字典的形式返回  
    _topic_band接口调用有问题，count字段没有控制接口返回的数量，需要调整_  

在weibo_hot_band使用requests包调用WB接口  
在main.py中调用
* hot_band`weibo_hot_band()`  
* topic_band先用`weibo_topic_num()`获取总num，然后传page来使用`weibo_topic_band`获取话题榜单  

## local_file  
* read_content方法读取本地文件中的热搜榜单
* save_content方法把获取到的热搜榜单写入本地  
* file_diff方法比较本次榜单和上次所获取的榜单，返回此次消失的热搜名称
