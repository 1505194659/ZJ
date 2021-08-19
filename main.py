import requests
headers={'cookie':'stuinfo=stuid=746D617407B8993C&stuxm=2EB177EBAD2D3D30&stubj=7285B8596DEF819F961F13D942957AE819DBB0DE49999A22; ASP.NET_SessionId=yuwyikt3qlvj3kuxdrdmipgg','origin':'https://fyns.eduw.cn','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',"upgrade-insecure-requests": "1",'referer': 'https://fyns.eduw.cn/stu/dk9.aspx'}
r=requests.post("https://dk.zjabc.edu.cn/stu/dk.aspx",headers=headers)
