import requests
import json

response = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')

items = response.json()['items']
for data in items:
    print(data)
print("Total items:", len(items))
for data in items:
    if data['is_answered']:
        print("Answered/Solved")
        print("Title:", data['title'])
        print("Link:", data['link'])
        print(f"Answer count: {data['answer_count']}")
        print('---------------------------------')
    else:
        print("Not answered")
        print("Title:", data['title'])
        print("Link:", data['link'])
        print('---------------------------------')
