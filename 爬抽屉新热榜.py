import requests

#爬取数据
# response = requests.get(
#     url = "https://dig.chouti.com/",
#     headers={
#         "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
#     }
# )
#  # response.encoding=''
# print(response.text)

# from bs4 import BeautifulSoup
# soup = BeautifulSoup(response.text,'html.parser')
# #标签对象
# content_list = soup.find(name='div',attrs={'id':'content-list'})
# #列表
# item_list = content_list.find_all(name='div',_class='item')
# for item in item_list:
#     print(item)

#点赞
#1.登陆
    #1.查看首页
# import requests
# r1 = requests.get(
#     url="https://dig.chouti.com/",
#     headers = {
#         "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
#
#     }
#                   )
#
#     #2提交用户名密码
#
# r2 = requests.post(
#     url= "https://dig.chouti.com/login",
#     headers = {
#         "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
#
#     },
#     data={
#         'phone':'8615159251249',
#         'password':'lq361025',
#         'oneMonth':1
#     }
# )
# print(r2.text)


