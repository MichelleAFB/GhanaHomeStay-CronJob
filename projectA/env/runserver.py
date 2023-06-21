


print("hello")

import requests
import json

response=requests.get('https://ghanahomestayserver.onrender.com/')

for data in response.json()['apps']:
    print(data)