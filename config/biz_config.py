"""
filter为多为表格筛选语句的筛选项后缀，在以下链接中app_token中filter后面写入筛选语句，点击开始调试获取真实请求地址，拿取filter后面的字符串放在这里
https://open.feishu.cn/api-explorer/cli_a217cbe48bba100b?apiName=get&from=op_doc&project=bitable&resource=app&version=v1
filter字段用于飞书获取多为标记记录的api，按需填写！！
"""


# 多为表格筛选语句，当前为AND(CurrentValue.[平台]="车控基础服务",CurrentValue.[需求版本]="12月需求",CurrentValue.[年份]="2022")， 在飞书文档中可以获得如下链接
filter = "AND%28CurrentValue.%5B%E5%B9%B3%E5%8F%B0%5D%3D%22%E8%BD%A6%E6%8E%A7%E5%9F%BA%E7%A1%80%E6%9C%8D%E5%8A%A1%22" \
         "%2CCurrentValue.%5B%E9%9C%80%E6%B1%82%E7%89%88%E6%9C%AC%5D%3D%2212%E6%9C%88%E9%9C%80%E6%B1%82%22" \
         "%2CCurrentValue.%5B%E5%B9%B4%E4%BB%BD%5D%3D%222022%22%29 "

version = "2.36.0"

#test -- https://open.feishu.cn/open-apis/bot/v2/hook/925c787f-8485-48b2-8616-e12633983022
#prd --
test_url = 'https://open.feishu.cn/open-apis/bot/v2/hook/925c787f-8485-48b2-8616-e12633983022'
prd_url = 'https://open.feishu.cn/open-apis/bot/v2/hook/5b7df1b4-754f-4d5d-a3fc-22a19edcbb03'
task_ddl = "12月15日"  # 需求收集截止时间
t_sheet = '12月28日'  # 提测截至时间
online_time = '1月1日'  # 上线时间
project_name = "OTA_后台_V4.5.1"  # 传入获取bug的方法，可配置的项目名称,关联禅道bug编辑中的，所属项目