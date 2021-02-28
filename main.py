import requests
s=requests.Session()
headers={'cookie':'stuinfo=stuid=746D617407B8993C&stuxm=2EB177EBAD2D3D30&stubj=7285B8596DEF819F961F13D942957AE819DBB0DE49999A22; ASP.NET_SessionId=jx0wrfkhzn4afmf5vqopqkf5','origin':'https://fyns.eduw.cn','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',"upgrade-insecure-requests": "1",'referer': 'https://fyns.eduw.cn/stu/dk9.aspx'}
r=s.post("https://fyns.eduw.cn/stu/dk9.aspx",headers=headers)
data={'Button2':' 当前情况和上次一样，系统直接帮我打卡' , '__VIEWSTATEGENERATOR': 'BEBF4070' , '__VIEWSTATE': '/wEPDwUKLTk3MjYyNTU4NGRkbQwAF57GOqyjzXoXKqZTAftYIH3j/SOdUxlgAK6g7Oc='}
k=s.post('https://fyns.eduw.cn/stu/dk9.aspx',data=data,headers=headers)
h=k.text
data={'text':'健康打卡结果','desp':h}
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
}
requests.post('https://sc.ftqq.com/SCU162308Tf0a5313c2ad0c45158a4f7bb0002a9c26038bc39782c1.send',headers=headers,data=data)
