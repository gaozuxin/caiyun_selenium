import requests, json

from common.my_mysql import mysql


class Requests(object):
    def __init__(self):
        requests.get('http://httpbin.org/get')
        requests.post('http://httpbin.org/post')
        requests.put('http://httpbin.org/put')
        requests.delete('http://httpbin.org/delete')
        requests.head('http://httpbin.org/get')
        requests.options('http://httpbin.org/get')

    def request_get(self, url, data):
        headers = {
            "Host": data['Host'],
            "Cookie": data['Cookie'],
            "Content-type": "application/json",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",

        }
        res = requests.get(url=url, headers=headers)
        return res

    def request_post(self, url, data):
        r = requests.post(url=url, json=data, headers={"Content-Type": "application/json"})  # 发送请求
        data_eval = json.loads(r.text)  # 字符串转成字典类型
        return data_eval


def get_rule_interface(post_data):
    url = 'http://172.16.20.15/caiyun/rule/onlinetest'
    headers = {
        "Content-type": "text/html; charset=UTF-8",
        # "X-Requested-With": 'XMLHttpRequest',
        "Cookie": "PHPSESSID=b0np7jukti03o0us3r1594rfet; Hm_lvt_dcc20f80ebc33a7af639f4b0c774367b=1544753097,1544758942,1544772799,1545009471; Hm_lpvt_dcc20f80ebc33a7af639f4b0c774367b=1545016034",
    }
    response = requests.post(url, data=post_data,headers=headers)
    print(response)

    print(response.text)


if __name__ == '__main__':
    sql = 'select rid, rule_name, rule_type, url, is_ajax, rule_config from task_rule'
    sql_data = mysql.select_all(sql)

    for index in range(len(sql_data)):
        rid = sql_data[index][0]
        rule_name = sql_data[index][1]
        rule_type = sql_data[index][2]
        url = sql_data[index][3]
        is_ajax = sql_data[index][4]
        if is_ajax == '1':
            ajax_str = 'TRUE'
        elif is_ajax == '2':
            ajax_str = 'FLASE'
        else:
            ajax_str =''
        rule_config = sql_data[index][5]
        data = {
            'url': url,
            'is_ajax': ajax_str,
            'rule_type': rule_type,
            'rule_config': rule_config

        }
        get_rule_interface(data)
