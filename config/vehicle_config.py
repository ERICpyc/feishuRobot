"""
filter为多为表格筛选语句的筛选项后缀，在以下链接中app_token中filter后面写入筛选语句，点击开始调试获取真实请求地址，拿取filter后面的字符串放在这里
https://open.feishu.cn/api-explorer/cli_a217cbe48bba100b?apiName=get&from=op_doc&project=bitable&resource=app&version=v1
filter字段用于飞书获取多为标记记录的api，按需填写！！
eg:AND(CurrentValue.[平台]="车管平台",CurrentValue.[需求版本]="12月需求",CurrentValue.[年份]="2022")
    AND(OR(CurrentValue.[平台].contains("卡管平台"),CurrentValue.[平台].contains("车管平台")),CurrentValue.[需求版本]="12月需求",CurrentValue.[年份]="2022")
"""

filter = "AND%28CurrentValue.%5B%E5%B9%B3%E5%8F%B0%5D%3D%22%E8%BD%A6%E7%AE%A1%E5%B9%B3%E5%8F%B0%22%2CCurrentValue.%5B" \
         "%E9%9C%80%E6%B1%82%E7%89%88%E6%9C%AC%5D%3D%222%E6%9C%88%E9%9C%80%E6%B1%82%22%2CCurrentValue.%5B%E5%B9%B4%E4" \
         "%BB%BD%5D%3D%222023%22%29 "

version = "车管2.38.0"  # 可单版本或者多版本填写

'''测试环境机器人地址生产机器人地址，记得切换'''

test_url = 'https://open.feishu.cn/open-apis/bot/v2/hook/925c787f-8485-48b2-8616-e12633983022'  # 测试环境
veh_prd_url = 'https://open.feishu.cn/open-apis/bot/v2/hook/b0c8af0a-77a3-46a9-9505-6eeea86042c3'  # 车管生产
rid_prd_url = 'https://open.feishu.cn/open-apis/bot/v2/hook/8c822185-0a07-4ff6-ad07-6bac3ad88732'  # 云诊断生产

task_ddl = "11月15日"  # 需求收集截止时间，暂时不用
t_sheet = '2月17日'  # 提测截至时间
online_time = '3月2日'  # 上线时间
project_name = "车管（车管，牧师项目）"  # 传入获取bug的方法，可配置的项目名称

