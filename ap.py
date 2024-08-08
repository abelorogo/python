import requests
responce= requests.get('https://fcsapi.com/api-v3/forex/latest?symbol=all_forex&access_key=oGrDqzQFdMs7DXFmnRtNgEqy')
print(responce)
data=responce.json()
#print(data)

r=data['status'][0]['code']
print(r)
