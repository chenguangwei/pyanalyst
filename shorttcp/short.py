#-*- coding = utf-8 -*-
import requests


# url="https://weibo.com/chinaetfs?profile_ftype=1&is_all=1#_loginLayer_1513910015464";
# header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0','Connection':'keep-alive'}
# response = requests.get(url,header)
# response.encoding = 'gb2312'
# print(response.text)


sss = requests.Session()

response1  = sss.get("https://st.im/")


print (response1.headers)




url="https://st.im/api/shorturl/create"
params={}
params['longurl']='http://ykzj.linkedmama.com'
params['type']=201

# print (params)
response = sss.post(url,data=params)

print(response.text)


