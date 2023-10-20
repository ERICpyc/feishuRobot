import requests
import json
from function import get_tenant_access_token

url = "https://open.feishu.cn/open-apis/contact/v3/users/batch_get_id?user_id_type=open_id"
payload = json.dumps({
    "emails": [
        "pengyc1@xiaopeng.com",
        "liangjc1@xiaopeng.com",
        "luohs@xiaopeng.com",
        "pengke@xiaopeng.com",
        "huc3@xiaopeng.com",
        "chenjq11@xiaopeng.com",
        "liangwy1@xiaopeng.com"
    ]
})

headers = {
    'Content-Type': 'application/json',
    'Authorization': "Bearer %s" % get_tenant_access_token()
}

# response = requests.request("POST", url, headers=headers, data=payload)
# r_json = response.text
# r_dict = json.loads(r_json)
# # print(r_dict)
# print(r_dict.values())
# print(type(r_dict))

def get_uid(name):
    user_dic = {"pengyc1": "ou_ee92b4888a109c9dfdda62c0f7b8bf67", "liangjc1": "ou_937cff47f9ff5fc15b42bac171e18f68",
                "luohs": "ou_8606de8d42110cd1b0b7a11fcd953151", "pengke": "ou_17f53d7b6cebfd9c99bd1e1d18e8b0d1",
                "huc3": "ou_1278252b830b005ec86acf3f868567d3", "chenjq11": "ou_c08a7ec56bbfbf59939d90383d0211d5",
                "liangwy1": "ou_d7549de6af2a49d9b76f473e0f73b0ae"}
    return user_dic[name]
