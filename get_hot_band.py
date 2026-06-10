# author: hebetian
import requests
import logging
import jsonpath


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
    except requests.RequestException:
        logging.error('status_code: %s' % response.status_code)
        return None


# 检查响应是否有效
def check_response(response_data):
    """
    检查response_data是否为json格式且ok字段为1
    """
    if type(response_data) == dict and response_data['ok'] == 1:
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
        hot_band_allmsg = jsonpath.jsonpath(response, 'data.realtime')
        return hot_band_allmsg
    except Exception as e:
        logging.error('get hot band all msg error: %s' % e)
        return None

# 保存热搜名称、标签、热度
def get_hot_band_list(hot_band_allmsg):
    """
    使用列表保存热搜名称、标签、热度，{
        'note': 名称,
        'tag': 标签,
        'num': 热度
    }
       """
    try:
        hot_band_list = []
        for item in hot_band_allmsg:
            label_name = item.get('label_name', '')
            label_name = None if label_name == '' else label_name

            hot_band = {
                'note': item.get('note', ''),
                'tag': label_name,
                'num': item.get('num', 0)
            }

            hot_band_list.append(hot_band)
            
        return hot_band_list
        
    except Exception as e:
        logging.error('get hot band list error: %s' % e)
        return None

