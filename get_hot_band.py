# author: hebetian
import requests
import logging


base_url = 'https://weibo.com'
base_path = '/ajax/side/hotSearch'
base_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Referer': 'https://weibo.com/',
    'Origin': 'https://weibo.com',
    'Connection': 'keep-alive',
}

# 获取热门话题响应
def get_hot_band_response():
    """
    请求热搜列表
    判断response_code是否为200
    """
    try:
        response = requests.get(base_url + base_path, timeout=10, headers=base_headers)
        if response.status_code == 200:
            return response.json()
        else:
            logging.error('status_code: %s' % response.status_code)
            return None
    except requests.RequestException as e:
        logging.error('request error: %s' % e)
        return None


# 检查响应是否有效
def check_response(response_data):
    """
    检查response_data是否为json格式且ok字段为1
    """
    if (isinstance(response_data, dict) 
    and response_data.get('ok') == 1 
    and isinstance(response_data.get('data'), dict) 
    and response_data.get('data').get('realtime') is not None):
        return True
    else:
        logging.error('response data error: %s' % response_data)
        return False

    

# 获取热门话题所有消息
def get_hot_band_allmsg(response):
    """
    从response_data的data.realtime字段中提取热搜列表所有信息
    """
    try:
        hot_band_allmsg = response.get('data').get('realtime')
        return hot_band_allmsg
    except (AttributeError, KeyError) as e:
        logging.error('get hot band all msg error: %s' % e)
        return None

# 保存热搜名称、标签、热度
def get_hot_band_list(hot_band_allmsg):
    """
    使用列表保存热搜排名、名称、标签、热度，{
        'rank': 排名,
        'note': 名称,
        'tag': 标签,
        'num': 热度
    }
       """
    try:
        hot_band_list = []
        if isinstance(hot_band_allmsg, list):        
            for item in hot_band_allmsg:
                if isinstance(item, dict):
                    
                    if item.get('note') is None or item.get('num') is None:
                        logging.error('This item data error: %s' % item)
                        continue

                    if item.get('topic_ad') == 1:
                        logging.warning('This item maybe is a ad: %s, skip it' % item.get('note'))
                        continue
                    
                    logging.info('This item rank: %s \n' % item.get('rank'))
                    logging.info('This item: %s \n' % item)
                    label_name = item.get('label_name', '')
                    if label_name == '':
                        label_name = None

                    hot_band = {
                        'rank': item.get('rank', None),
                        'note': item.get('note', ''),
                        'tag': label_name,
                        'num': item.get('num', 0)
                    }

                    hot_band_list.append(hot_band)
                
                else:
                    logging.error('item type error: %s' % item)
                    continue
        
 
        else:
            logging.error('hot band all msg type error: %s' % hot_band_allmsg)
            return None
        logging.info('hot band list length: %s' % len(hot_band_list))
        return hot_band_list

    except Exception as e:
        logging.error('get hot band list error: %s' % e)
        return None

