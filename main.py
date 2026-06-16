import logging
import get_hot_band
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo
import json
import os


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def main():
    # 获取当前时间
    dt = datetime.now(ZoneInfo('Asia/Shanghai'))
    logging.info(dt)

    response_data = get_hot_band.get_hot_band_response()

    '''
    hot_band_allmsg: response_data的data.realtime字段
    hot_band_info: 热搜列表所有信息，包含名称、标签、热度
    '''
    if get_hot_band.check_response(response_data):
        hot_band_allmsg = get_hot_band.get_hot_band_allmsg(response_data)
        hot_band_info = json.dumps(get_hot_band.get_hot_band_list(hot_band_allmsg), ensure_ascii=False, indent=2)
        logging.info(hot_band_info)
        
        snapshot_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'snapshot')
        os.makedirs(snapshot_dir, exist_ok=True)
        filename = dt.strftime('%Y%m%d-%H%M') + '.json'
        filepath = os.path.join(snapshot_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(hot_band_info)
        logging.info('save hot band info to %s' % filepath)

    else:    
        logging.error('Failed to get hot band. Denied by the Weibo server.')

if __name__ == '__main__':
    main()


# TODO:analyze hot_band_info

