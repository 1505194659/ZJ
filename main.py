import requests
s=requests.Session()
headers={'cookie':'stuinfo=stuid=746D617407B8993C&stuxm=2EB177EBAD2D3D30&stubj=7285B8596DEF819F961F13D942957AE819DBB0DE49999A22; ASP.NET_SessionId=yuwyikt3qlvj3kuxdrdmipgg','origin':'https://fyns.eduw.cn','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',"upgrade-insecure-requests": "1",'referer': 'https://fyns.eduw.cn/stu/dk9.aspx'}
r=s.post("https://dk.zjabc.edu.cn/stu/dk.aspx",headers=headers)
data={'Button2':' 当前情况和上次一样，系统直接帮我打卡' ,'jd':'120.76048','wd':'30.122333','__VIEWSTATEGENERATOR': 'CE083383' , '__VIEWSTATE': '/wEPDwUIODQ5MzIxODBkZNojZjs69XW2iGO0Njs6v0utnOAjU04Jt2viA4xY5F7J'}
k=s.post('https://dk.zjabc.edu.cn/stu/dk.aspx',data=data,headers=headers)
h=k.text
data={'title':'健康打卡结果','desp':h}
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
}
requests.post('https://sctapi.ftqq.com/SCT65261TnN9vI4jsKohOHP5aSmxqKo0s.send?',headers=headers,data=data)
