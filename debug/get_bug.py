from jsonsearch import JsonSearch

from config.vehicle_config import project_name
import json,requests


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
print(dict_data)
bugname = []
buginfo = []
bugtotal = []
for i in dict_data:
    print(i)
    jsonname = JsonSearch(object=i, mode='j')  # 调用三方JSON处理函数
    namelist = jsonname.search_all_value(key="assignedto")  # 检索json中为{key}的所有值
    bugname = jsonname.search_all_value(key="title")
    if namelist[0] != "closed":
        buginfo = namelist + bugname  # 拼接负责人+ bug名称
        print(buginfo)
        bugtotal += buginfo

print(bugtotal)