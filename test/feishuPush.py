import json
import requests
from function import get_tenant_access_token
from config.vehicle_getData import get_count_ele, get_ele, get_bug
from config.vehicle_config import version, test_url, veh_prd_url, rid_prd_url, t_sheet, online_time

def batch_create():
    token_url = "https://open.feishu.cn/open-apis/bitable/v1/apps/bascnf1jLcM8Cgwv7aPDKNOeaKo"

    headers = {
        "Authorization": "Bearer %s" % get_tenant_access_token()
    }

    request = requests.get(url=token_url, headers=headers)
    response = json.loads(request.content)
    return response

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
                                       "<font color='yellow'>未开始</font>："
                                       "\n<font color='red'>开发中</font>："
                                       "\n<font color='red'>已提测</font>："
                                       "\n<font color='red'>测试中</font>："
                                       "\n<font color='green'>待上线</font>:",
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
                               "<at id=" "></at>" + "\t"
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