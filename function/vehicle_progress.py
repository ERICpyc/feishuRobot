import json
import requests
from jsonsearch import JsonSearch
from tools.getUser import get_uid
from function import get_tenant_access_token
from config.vehicle_getData import get_count_ele, get_ele, get_bug
from config.vehicle_config import version, test_url, veh_prd_url, rid_prd_url, t_sheet, online_time

# 从需求表获取到所有key为进展的值
list_progress = get_count_ele('进展')
print(list_progress)
list_type = get_ele('类型')
print(list_type)
print(type(list_progress))
# 初始化各种进展参数的值
online = 0
deve = 0
todo = 0
debug = 0
tobetest = 0
testing = 0
ready = 0
delay = 0
others = 0
plan = 0

# 汇总每一种状态的需求总数
for i in list_progress:
    for j in i:
        if j == '已上线':
            online = i[1]
        elif j == '开发中':
            deve = i[1]
        elif j == '未开始':
            todo = i[1]
        elif j == '联调中':
            debug = i[1]
        elif j == '已提测':
            tobetest = i[1]
        elif j == '测试中':
            testing = i[1]
        elif j == '待上线':
            ready = i[1]
        elif j == '延期':
            delay = i[1]
        elif j == '规划中':
            plan = i[1]
        elif j == '待联调':
            tobedebug = i[1]
        else:
            others = i[1]

dict_data = get_bug()
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


# 飞书推送鉴权
def batch_create():
    token_url = "https://open.feishu.cn/open-apis/bitable/v1/apps/bascnf1jLcM8Cgwv7aPDKNOeaKo"

    headers = {
        "Authorization": "Bearer %s" % get_tenant_access_token()
    }

    request = requests.get(url=token_url, headers=headers)
    response = json.loads(request.content)
    return response


# 消息卡片消息体
message = {
    "msg_type": "interactive",
    "card": {
        "config": {
            "wide_screen_mode": True
        },
        "elements": [
            {
                "fields": [
                    {
                        "is_short": True,  # 多列展示
                        "text": {
                            "content": "**📚[需求跟进表](https://xiaopeng.feishu.cn/base/bascnf1jLcM8Cgwv7aPDKNOeaKo?table"
                                       "=tblMivEIRu7MODKk&view=vew2Ci4gCV)**"
                                       "\n版本计划上线时间:" + online_time +  # 这两个数据在config中配置，时间未定前不需要该列可以注释掉
                                       "\n\n提测截止时间:" + t_sheet +
                                       "\n\n目前加塞需求:0",
                            "tag": "lark_md"
                        }
                    },
                    {
                        "is_short": True,
                        "text": {
                            "content": "**目前需求进度**\n"
                                       "<font color='yellow'>未开始</font>：" + str(todo + plan) +
                                       "\n<font color='red'>开发中</font>：" + str(deve + debug) +
                                       "\n<font color='red'>已提测</font>：" + str(tobetest) +
                                       "\n<font color='red'>测试中</font>：" + str(testing) +
                                       "\n<font color='green'>待上线</font>:" + str(ready),
                            "tag": "lark_md"
                        }
                    }

                ],
                "tag": "div"
            },
            {
                "tag": "hr"  # 分割线模块
            },
            # {
            #
            #     "tag": "div",
            #     "text": {
            #         "content": "**在测需求**\n\t组件导入导出优化\n\t同一车型可在不同工厂生产\n\t组件允许跨车型复制而不丢失已配资源"
            #         "<at id=" + get_uid("chenjq11") + "></at>"
            #         ,
            #         "tag": "lark_md"
            #     }
            # },
            {
                "tag": "hr"
            },
            {

                "tag": "div",
                "text": {

                    "content": "**💪以下同学还有问题需解决哦，请关注并尽快处理**\n"
                               "<at id=" + get_uid(bugtotal[0]) + "></at>" + "\t"+ bugtotal[1]
                               # + "\n<at id=" + get_uid(bugtotal[2]) + "></at>" + bugtotal[3]
                    # 每个bug负责人+bug,需要添加一个,+ "\n<at id=" + get_uid(bugtotal[2]) + "></at>" + bugtotal[3]
                    ,

                    "tag": "lark_md"
                }
            }
        ],
        "header": {
            "template": "wathet",
            "title": {
                "content": "📢 " + version + "版本 -- 研发&测试阶段"
                ,
                "tag": "plain_text"
            }
        }
    }
}

headers = {
    'Content-Type': 'application/json'
}

# 【url从config.config文件引入，注意环境正确！！！！】
message = requests.request("POST", test_url, headers=headers, data=json.dumps(message))
