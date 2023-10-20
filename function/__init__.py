from collections import Counter
import requests
import json
from jsonsearch import JsonSearch

filter = "AND%28CurrentValue.%5B%E5%B9%B3%E5%8F%B0%5D%3D%22%E8%BD%A6%E7%AE%A1%E5%B9%B3%E5%8F%B0%22%2CCurrentValue.%5B%E9%9C%80%E6%B1%82%E7%89%88%E6%9C%AC%5D%3D%2210%E6%9C%88%E9%9C%80%E6%B1%82%22%2CCurrentValue.%5B%E5%B9%B4%E4%BB%BD%5D%3D%222022%22%29"

def get_tenant_access_token():
    token_url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/"
    headers = {"Content-Type": "application/json"}

    # 橙行智动
    data = {
        "app_id": "cli_a1fa75a4dabcd00b",
        "app_secret": "0p27zWpHCetvHgEeg5LYpedUjZkokUQy"
    }

    request = requests.get(url=token_url, headers=headers, json=data)
    response = json.loads(request.content)['tenant_access_token']
    return response




url = "https://open.feishu.cn/open-apis/bitable/v1/apps/bascnf1jLcM8Cgwv7aPDKNOeaKo/tables/tblMivEIRu7MODKk/records?filter=" + filter
headers = {
    "Authorization": "Bearer %s" % get_tenant_access_token()  # 传入token
}
params = {
}

res = requests.request("GET", url, headers=headers, data=params)
data = res.json()  # 返回数据为response格式，转化为json格式
print(data)


def get_ele(key):
    jsonname = JsonSearch(object=data, mode='j')  # 调用三方JSON处理函数
    namelist = jsonname.search_all_value(key=key)  # 检索json中为{key}的所有值
    count_set = set(namelist)  # 去除列表中重复项
    # count_list = list()
    # for i in count_set:
    #     n = count_list.append((i, namelist.count(i)))
    #     print(n)

    namedict = Counter(namelist)  # 调用计数工具
    # for key in count_set:  # 循环遍历按人输出需求数
    #     print(key, "=", namedict[key])
    v = namedict.items()
    list_v = list(v)  # 转成list方便索引
    return list_v

version = "2.34.0"

