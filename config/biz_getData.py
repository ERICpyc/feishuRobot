import requests
import json
from function import get_tenant_access_token
from config.biz_config import filter, project_name
from jsonsearch import JsonSearch
from collections import Counter


url = "https://open.feishu.cn/open-apis/bitable/v1/apps/bascnf1jLcM8Cgwv7aPDKNOeaKo/tables/tblMivEIRu7MODKk/records?filter=" + filter
headers = {
    "Authorization": "Bearer %s" % get_tenant_access_token()  # 传入token
}
params = {
}

res = requests.request("GET", url, headers=headers, data=params)
data = res.json()  # 返回数据为response格式，转化为json格式
# print(data)

def get_count_ele(key):
    jsonname = JsonSearch(object=data, mode='j')  # 调用三方JSON处理函数
    namelist = jsonname.search_all_value(key=key)  # 检索json中为{key}的所有值
    count_set = set(namelist)  # 去除列表中重复项
    # count_list = list()
    # for i in count_set:
    #     n = count_list.append((i, namelist.count(i)))
    #     print(n)
    # 统计每一种key对应的value总数
    namedict = Counter(namelist)  # 调用计数工具
    for key in count_set:  # 循环遍历按人输出需求数
        print(key, "=", namedict[key])
    v = namedict.items()
    list_v = list(v)  # 转成list方便索引
    return list_v


def get_ele(key):
    jsonname = JsonSearch(object=data, mode='j')  # 调用三方JSON处理函数
    namelist = jsonname.search_all_value(key=key)  # 检索json中为{key}的所有值
    list_j = list(namelist)
    return list_j


def get_total(key):
    jsonall = JsonSearch(object=data, mode='j')
    all = jsonall.search_all_value(key=key)
    return len(all)


def get_bug():
    data = {'obj_name': 'MundoServer.MundoServer',
            'method_name': 'get_bug',
            "project_name": "%s" % project_name,
            "token": "zendao_qianxy1|MTk2MTA0NDI0NS45MjM0MTA3OjZhNjRmZDBkZDAxOGVhYzc0ODYwNzQ4OTViZjg1YWFjYmQ2NWNlZDk="
            }

    data = json.dumps(data)
    headers = {"Content-type": "application/json", "Accept": "*/*"}
    conn = requests.post("http://testcenter.xiaopeng.local:25185", data, headers)
    data = conn.content
    # 格式转换
    data = json.loads(data)
    res_data = json.loads(data["data"])
    str_data = str(res_data).replace("'", '"')  # 转化为字符串格式并且替换所有单引号
    dict_data = json.loads(str_data)
    # print(dict_data)  # 一整个dict_data存放在list中，每个元素是一个bug的所有属性，单个元素可以放入jsonsearch拿取数据
    return dict_data

