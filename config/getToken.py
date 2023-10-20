import json
import requests


# 颜值侠带权限接口获取token
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