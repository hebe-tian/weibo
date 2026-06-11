# Weibo Hot Search Data Collector

一个轻量级的微博热搜数据采集工具，通过 GitHub Actions 定时执行，自动获取并保存微博热搜榜单数据。

## 功能特性

- 每小时自动采集微博热搜榜单数据
- 提取热搜话题名称、标签和热度值
- 自动保存快照到 snapshot 目录
- 使用 GitHub Actions 实现自动化运行

## 技术栈

- Python 3.12
- requests: HTTP 请求库
- jsonpath: JSON 数据提取（已弃用，改用 dict.get()）
- pytz: 时区处理
- pytest: 单元测试框架

## 核心模块说明

### get_hot_band.py

提供微博热搜数据获取和处理的核心函数：

* get_hot_band_response(): 发送 HTTP 请求获取微博热搜 API 数据  
* check_response(response_data): 验证 API 响应是否有效  
* get_hot_band_allmsg(response): 从响应中提取 realtime 数据列表  
* get_hot_band_list(hot_band_allmsg): 将原始数据转换为结构化格式  

返回的数据格式：
``` json
[
  {
    "note": "热搜话题名称",
    "tag": "标签（热/新/爆等，无标签时为 null）",
    "num": 热度值
  }
]
```

### main.py  

主程序入口，负责：
1. 调用数据采集函数
2. 验证响应数据
3. 转换数据格式
4. 保存为 JSON 文件到 snapshot 目录

## 自动化部署

项目使用 GitHub Actions 实现自动化数据采集：

* 执行频率：每小时整点（cron: '0 * * * '）

* 工作流程：
    1. checkout 代码
    2. 设置 Python 3.12 环境
    3. 安装依赖
    4. 运行 main.py
    5. 提交 snapshot 数据到仓库

* 手动触发：在 GitHub Actions 页面点击 "Run workflow"

## 测试  

运行单元测试： 
``` bash
pytest tests/ -v  
```

查看测试覆盖率：  
``` bash  
pytest tests/ -v --cov=get_hot_band --cov-report=term-missing
```  

## TODO  

增加热搜数据分析功能