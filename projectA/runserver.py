


print("hello")

import requests
import json

response=requests.get('https://ghanahomestayserver.onrender.com/')

print(response)

response2=requests.post('https://leetcodetracker.onrender.com/remove-duplicates')

for data in response.json()['apps']:
    print(data)