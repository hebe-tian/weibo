import json


def save_content(content):
    filename = 'weibo.json'
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(json.dumps(content, indent=2, ensure_ascii=False))


def read_content(file):
    with open(file, 'r') as f:
        content = f.read()
        return content


def file_diff(response, last_content):
    diff_list = []
    last_content = json.loads(last_content)
    for name in response.keys():
        if name not in last_content.keys():
            diff_list.append(name)

    return diff_list
