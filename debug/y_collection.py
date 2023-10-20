import json
import requests
from config.vehicle_config import url, version,task_ddl
from config.vehicle_getData import get_total
from function import get_tenant_access_token

total = get_total('需求标题')
print(get_total)
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
            "wide_screen_mode": False
        },
        "elements": [
            {

                "tag": "div",
                "text": {
                    "content": "**📚[需求跟进表](https://xiaopeng.feishu.cn/base/bascnf1jLcM8Cgwv7aPDKNOeaKo?table"
                               "=tblMivEIRu7MODKk&view=vew2Ci4gCV)**"
                    ,
                    "tag": "lark_md"
                }
            },

            {
                "tag": "hr"  # 分割线模块
            },
            {
                "fields": [
                    {
                        "is_short": True,  # 多列展示
                        "text": {
                            "content": "📋目前需求数：" +  str(total),
                            "tag": "lark_md"
                        }
                    },
                    {
                        "is_short": True,
                        "text": {
                            "content": " 🕐需求录入截至日期：" + task_ddl,
                            "tag": "lark_md"
                        }
                    }

        ],
            "tag": "div"
            }
            ],
        "header": {
            "template": "green",
            "title": {
                "content": "📢 车管" + version + "版本 -- 需求收集阶段",
                "tag": "plain_text"
            }
        }
    }
}

headers = {
    'Content-Type': 'application/json'
}

# url从config文件引入，注意环境正确！！！！
message = requests.request("POST", url, headers=headers, data=json.dumps(message))
