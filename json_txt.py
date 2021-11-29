import json

with open('datas.json','r') as f:
    datas = json.load(f)
    
username = []

for i in datas:
    try:
        username.append(i['username'])
    except:
        pass

data_txt = open('data.txt','w+')

for i in username:
    data_txt.write(i +'\n')
