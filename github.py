######################自动登陆GitHub##########################
# 1.GET访问登陆页面
'''
去html找到隐藏的input框  获取csrf_token
获取cookie
'''
import requests
from bs4 import BeautifulSoup

r1 = requests.get(
    url='https://github.com/login',
    headers={
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
)
cookie = r1.cookies.get_dict()
print(cookie)
# print(r1.text)

# 发送POST请求,用户名和密码
'''
-发送数据
    -csrf
    -用户名
    -密码
-携带cookie
'''

# r2 = requests.get(
#     url="https://github.com/login",
#     headers={
#         'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
#     },
#     data={
#         'commit': '登入',
#         'authenticity_token': 'aerG5V1j3WqLHDSlY0m0lU7IrSR7K64+zfYoQR+mE/nI64Dyw54yKsjyfCdT9V7vkKEGo90qJW4T8WuSvaac4w==',
#         'ga_id': 'ga_id',
#         'login': 'LiQ0112',
#         'password': 'LiQ1515085405asd@',
#         'webauthn-support:': 'supported',
#         'webauthn-iuvpaa-support': 'unsupported',
#         'return_to': '',
#         'required_field_0feb': '',
#         'timestamp': '1592575408742',
#         'timestamp_secret': 'a78067667552ae6fc4eb8c6549ea5534ddf7e3f568b30398030777cc0f703b95'
#     },
#     cookies=r1.cookies.get_dict()
# )
#
# print(r2.text)
