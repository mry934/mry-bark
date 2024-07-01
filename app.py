import json

from flask import Flask, request, jsonify
import requests

from entity.RawMsgBean import RawMsgBean

app = Flask(__name__)

# Bark 推送 URL 基础地址
BARK_BASE_URL = 'https://api.day.app/you-api/'


@app.route('/send_notification', methods=['POST'])
def send_notification():

    data = request.json
    print(data)
    response = build_send_msg(data)

    if response.status_code == 200:
        return jsonify({'code': 200, 'message': 'success', 'timestamp': 1719420238}), 200
    else:
        return jsonify({'code': 500, 'message': 'error', 'timestamp': 1719420238}), 500


def extract_msg(body):
    message = ""
    # 解析消息内容，假设消息格式固定
    # 具体消息内容是 '慎微姐: test03' 这一行的内容
    lines = body.split('\n')
    if lines[2] in load_group_name_from_file('name.txt'):
        sender, content = lines[1].split(':')
        message = f'{sender}: 在群聊{lines[2]}里说 {content}'
    else:
        message = f"{lines[2]}说了{lines[1].split(':')[-1]}"
    print(message)
    return message


def load_group_name_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        strings = [line.strip() for line in file]
    return strings

def test_private_chat():
    test_str=('{"title": "com.tencent.mm", "body": "com.tencent.mm\\n[2条]慎微姐: test13\\n慎微姐\\nUID：10234\\n2024-06-29 15:34:18",'
              ' "isArchive": 1, "level": "active"}')
    raw_json_data = json.loads(test_str)
    response = build_send_msg(raw_json_data)
    if response.status_code == 200:
        print(200)
    else:
        print(500)

def test_group_chat():
    test_str=('{"title": "com.tencent.mm", "body": "com.tencent.mm\\n张: 发之前再对其一下颗粒度，辛苦一下赶紧整理\\n开发室A2\\nUID：10234\\n2024-06-29 15:34:18",'
              ' "isArchive": 1, "level": "active"}')
    raw_json_data = json.loads(test_str)
    response = build_send_msg(raw_json_data)
    if response.status_code == 200:
        print(200)
    else:
        print(500)


def build_send_msg(raw_json_data):
    bean = RawMsgBean(raw_json_data['title'], raw_json_data['body'], raw_json_data['isArchive'], raw_json_data['level'])
    processed_title = '微信'
    processed_content = extract_msg(bean.body)
    # 构建 Bark 推送 URL
    bark_url = f'{BARK_BASE_URL}{processed_title}/{processed_content}'
    # 发送推送通知
    response = requests.get(bark_url)
    print(response)
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5020)
    test_private_chat()
    test_group_chat()