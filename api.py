import requests

response = requests.get("https://fcsapi.com/api-v3/forex/latest?symbol=all_forex&access_key=oGrDqzQFdMs7DXFmnRtNgEqy")
data=response.json()

print(data)
# rates= data['response']

# # x=[i for i in rates if "KES" in r["s"]]
# # print(x)