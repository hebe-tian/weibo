# weibo  

## weibo_hot_band  
* weibo_hot_band方法，获取微博热搜榜单和热度，以字典的形式返回  
* weibo_topic_band方法，获取微博热门话题榜单和简述，以字典的形式返回  
    _topic_band接口调用有问题，count字段没有控制接口返回的数量，需要调整_  

使用requests包调用WB接口，在main.py中调用hot_band和topic_band方法  
使用GitHub Actions定时执行main.py，打印weibo返回的数据  
