import requests
url="https://api.github.com/users/priyankawadkar30"

res=requests.get(url)
print(res.content)